import contextlib
import json
import os
import ssl
import sys
import time
from pathlib import Path
from typing import TypedDict

import requests
from loguru import logger
from tqdm import tqdm

from my_lib.xx_util import OPR, del_keys, replace_str, sort_list_dict, sort_p6_emoji, sort_str_list

log = logger.bind(user="X1")
ssl._create_default_https_context = ssl._create_unverified_context  # noqa: SLF001
requests.packages.urllib3.disable_warnings()  # pyright: ignore[reportAttributeAccessIssue]
config = json.loads(open("config.json", encoding="utf-8").read())  # noqa: PTH123, SIM115
_A = {"User-Agent": config["ua"], "Connection": "keep-alive", "Accept-Encoding": config["ae"]}
_BF = config["bar_format"]
_B = b'{"code":0,"message":"0","ttl":1,"data":{"suit_items":null,"fan_user":{"mid":0,"nickname":"","avatar":""},"unlock_items":null,"activity_entrance":null}}'
_C = b'{"code":-500,"message":"\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x99\xa8\xe9\x94\x99\xe8\xaf\xaf","ttl":1,"data":{"suit_items":null,"fan_user":{"mid":0,"nickname":"","avatar":""},"unlock_items":null,"activity_entrance":null}}'
_D = b'{"code":0,"message":"OK","ttl":1,"data":{"suit_items":null,"fan_user":{"mid":0,"nickname":"","avatar":""},"unlock_items":null,"activity_entrance":null}}'
config = config["x1"]
_EMPTY_FAN_USER = {"mid": 0, "nickname": "", "avatar": ""}
_EMPTY_ACTIVITY_ENTRANCE = {"id": 0, "item_id": 0, "title": "", "image_cover": "", "jump_link": ""}
_L: str = config["url"]
BP: str = config["bp"]
P = "properties"
S = "suit_items"
_a: int = 0
Properties = dict[str, str]
TRASH: str = "🗑"
IDCSV: str = BP + "ids.csv"
z: set = set(config["z"])


class SuitItems(TypedDict):
    desc: str
    item_id: int
    suit_item_id: int
    fan_id: str
    sale_type: str
    suit_card_type: str
    timing_online_unix: str
    type: str
    properties: Properties


class CurrentNextActivity(TypedDict):
    type: int
    time_limit: bool
    time_left: str
    tag: int
    price_bp_month: int
    price_bp_forever: int
    type_month: int
    tag_month: int
    time_limit_month: bool
    time_left_month: str


class FanUser(TypedDict):
    mid: int
    nickname: str
    avatar: str


class X1(TypedDict):
    item_id: int
    name: str
    group_id: int
    group_name: str
    part_id: int
    state: str
    properties: Properties | dict
    current_activity: CurrentNextActivity
    next_activity: CurrentNextActivity
    current_sources: int
    finish_sources: int
    sale_left_time: int
    sale_time_end: int
    sale_surplus: int
    sale_count_desc: str
    total_count_desc: str
    tag: str
    jump_link: str
    sales_mode: int
    suit_items: dict[str, list[SuitItems]]
    fan_user: FanUser
    unlock_items: int
    activity_entrance: int


def _E(b: requests.Session, d: int | str) -> bytes:
    global _a  # noqa: PLW0603
    retry = 0
    if d in z:
        return _D
    while retry < 10:
        try:
            _a += 1
            c = b.get(_L.format(q=d), headers=_A, verify=False, timeout=20)
            c.raise_for_status()
            if c.content == _C:
                raise requests.HTTPError("-500", response=c)
        except requests.RequestException as e:  # noqa: PERF203
            retry += 1
            log.error(f" {d} {retry=} {e}")
            # log.exception(e)
            time.sleep(retry)
        except KeyboardInterrupt:
            raise KeyboardInterrupt from None
        else:
            return c.content
    raise requests.RequestException(f"Failed to fetch {d}")


def _F(a: str, b: X1) -> bool:
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    e = ""
    if os.path.isfile(a):  # noqa: PTH113
        e = open(a, encoding="utf-8").read()  # noqa: PTH123, SIM115
        if d == e:
            return False
        c: X1 = json.loads(e)
        if isinstance(b.get(P), dict):
            if isinstance(b[P].get("item_ids"), str) and isinstance(c[P].get("item_ids"), str):
                b[P]["item_ids"] = sort_str_list(b[P]["item_ids"] + "," + c[P]["item_ids"])
            if isinstance(b[P].get("fan_item_ids"), str) and isinstance(c[P].get("fan_item_ids"), str):
                b[P]["fan_item_ids"] = sort_str_list(b[P]["fan_item_ids"] + "," + c[P]["fan_item_ids"])
        # ============================
        for i in c.get(S, {}):
            if i in c.get(S):
                if i not in b.get(S):
                    b[S][i] = c[S][i]
                else:
                    for g in c[S][i]:
                        if (h := json.dumps(g, ensure_ascii=False)) not in (f := {json.dumps(j, ensure_ascii=False) for j in b[S][i]}):
                            b[S][i].append(g)
                            f.add(h)
            if i in b[S]:
                sort_list_dict(b[S][i], "item_id", "name")
    # ============================
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if e and d == e:
        return False
    while True:
        try:
            with open(a, "w", encoding="utf-8") as fp:  # noqa: PTH123
                fp.write(d)
                break
        except PermissionError:
            log.error("PermissionError")
            time.sleep(10)
    return True


def _G(a: str, b: str) -> bool:
    """Csv / jsonl."""
    if isinstance(b, dict):
        b = json.dumps(b, ensure_ascii=False, separators=(",", ":"))
    while True:
        try:
            if b in z or (os.path.isfile(a) and b in open(a, encoding="utf-8").read()):  # noqa: PTH113, PTH123, SIM115
                return False
            with open(a, "a", encoding="utf-8") as fp:  # noqa: PTH123
                fp.write(b + "\n")
                break
        except PermissionError:
            # log.error("PermissionError")
            time.sleep(10)
    return True


def _H(a: int, item: X1) -> bool:
    if a in z:
        return 1 != 1
    c = item["part_id"]
    d = _G
    g = d(IDCSV, f"{a},{item['name']},{item['group_id']},{c}")
    if isinstance(item.get(P), dict):
        if isinstance(item[P].get("item_ids"), str):
            item[P]["item_ids"] = sort_str_list(item[P]["item_ids"])
        if isinstance(item[P].get("fan_item_ids"), str):
            item[P]["fan_item_ids"] = sort_str_list(item[P]["fan_item_ids"])
    if isinstance(item.get(S), dict):
        if isinstance(item[S].get("emoji"), list):
            sort_list_dict(item[S]["emoji"])
        if isinstance(item[S].get("card"), list):
            sort_list_dict(item[S]["card"])
        if isinstance(item[S].get("card_bg"), list):
            sort_list_dict(item[S]["card_bg"])
        if isinstance(item[S].get("loading"), list):
            sort_list_dict(item[S]["loading"])
        if isinstance(item[S].get("pendant"), list):
            sort_list_dict(item[S]["pendant"])
        if isinstance(item[S].get("play_icon"), list):
            sort_list_dict(item[S]["play_icon"])
        if isinstance(item[S].get("skin"), list):
            sort_list_dict(item[S]["skin"])
        if isinstance(item[S].get("space_bg"), list):
            sort_list_dict(item[S]["space_bg"])
        if isinstance(item[S].get("thumbup"), list):
            sort_list_dict(item[S]["thumbup"])
        if isinstance(item[S].get("emoji_package"), list):
            sort_p6_emoji(item[S]["emoji_package"])  # pyright: ignore[reportArgumentType]
    match c:
        case 1:
            f = "PART_1_头像框.jsonl"
        case 2:
            f = "PART_2_动态卡片.jsonl"
            if (
                item[P].get("image", "") == "https://i0.hdslb.com/bfs/activity-plat/static/20240223/3334b2daefb8be78dcc25a7ec37d60fe/sVvHUQ5IPV.png"
                and item[P].get("image_preview_small", "") == "https://i0.hdslb.com/bfs/garb/item/edfb01bd0fa7de7c7e3f516a16a16e8b0cde9ef5.png"
                and item[P].get("sale_type", "") == "collect_card"
            ):
                item[P].pop("image")
                item[P].pop("image_preview_small")
                item[P].pop("sale_type")
                item[P]["X_Part2_collect_card"] = 1  # pyright: ignore[reportArgumentType]
        case 3:
            f = "PART_3_点赞效果.jsonl"
        case 4:
            f = "PART_4_表情.jsonl"
        case 5:
            d = _F
            f = f"\\PART_5_表情包\\{a}.json"
        case 6:
            d = _F
            f = f"\\PART_6_main\\{a}.json"
        case 7:
            f = "PART_7_空间背景.jsonl"
        case 8:
            f = "PART_8_勋章.jsonl"
            if (
                item[P].get("image", "") == "https://i0.hdslb.com/bfs/garb/item/bb95a716723fa17354aa18ae10323903747c79ec.png"
                and item[P].get("image_preview_small", "") == "https://i0.hdslb.com/bfs/garb/item/edfb01bd0fa7de7c7e3f516a16a16e8b0cde9ef5.png"
                and item[P].get("sale_type", "") == "collect_card"
            ):
                item[P].pop("image")
                item[P].pop("image_preview_small")
                item[P].pop("sale_type")
                item[P]["X_Part8_collect_card"] = 1  # pyright: ignore[reportArgumentType]
        case 9:
            f = "PART_9_皮肤.jsonl"
        case 10:
            f = "PART_10_加载动画.jsonl"
        case 11:
            f = "PART_11_进度条装扮.jsonl"
        case 12:
            f = "PART_12_test.jsonl"
        case 13:
            f = "PART_13_NFT.jsonl"
        case _:
            f = "UNKNOWN_IDs.jsonl"
    del_keys(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, recursive=False)
    del_keys(item, "activity_entrance", None, recursive=False)
    del_keys(item, "addable", operator=OPR.ANY)
    del_keys(item, "associate_words", "")
    del_keys(item, "associate", operator=OPR.ANY)
    del_keys(item, "current_activity", operator=OPR.ANY)
    del_keys(item, "current_sources", operator=OPR.ANY)
    del_keys(item, "fan_user", _EMPTY_FAN_USER, recursive=False)
    del_keys(item, "finish_sources", None)
    del_keys(item, "gray_rule_type", operator=OPR.ANY)
    del_keys(item, "gray_rule", operator=OPR.ANY)
    del_keys(item, "hot", operator=OPR.ANY)
    del_keys(item, "is_hide", operator=OPR.ANY)
    del_keys(item, "is_symbol", operator=OPR.ANY)
    del_keys(item, "item_stock_surplus", operator=OPR.ANY)
    del_keys(item, "items", None)
    del_keys(item, "jump_link", "")
    del_keys(item, "next_activity", operator=OPR.ANY)
    del_keys(item, "non_associate", operator=OPR.ANY)
    del_keys(item, "open_platform_vip_discount", operator=OPR.ANY)
    del_keys(item, "permanent", operator=OPR.ANY)
    del_keys(item, "preview", operator=OPR.ANY)
    del_keys(item, "rank_investor_show", operator=OPR.ANY)
    del_keys(item, "realname_auth", operator=OPR.ANY)
    del_keys(item, "recently_used", operator=OPR.ANY)
    del_keys(item, "recommend", operator=OPR.ANY)
    del_keys(item, "ref_mid", "0")
    del_keys(item, "removable", operator=OPR.ANY)
    del_keys(item, "sale_count_desc", operator=OPR.ANY)
    del_keys(item, "sale_left_time", operator=OPR.ANY)
    del_keys(item, "sale_promo", operator=OPR.ANY)
    del_keys(item, "sale_quantity_limit", operator=OPR.ANY)
    del_keys(item, "sale_reserve_switch", operator=OPR.ANY)
    del_keys(item, "sale_surplus", operator=OPR.ANY)
    del_keys(item, "sale_time_end", 0, OPR.LEQ)
    del_keys(item, "sale_time_end", operator=OPR.ANY, recursive=False)
    del_keys(item, "sales_mode", 0)
    del_keys(item, "setting_pannel_not_show", operator=OPR.ANY)
    del_keys(item, "sortable", operator=OPR.ANY)
    del_keys(item, "state", operator=OPR.ANY)
    del_keys(item, "suit_item_id", 0)
    del_keys(item, "tab_id", 0)
    del_keys(item, "tag", operator=OPR.ANY)
    del_keys(item, "total_count_desc", operator=OPR.ANY)
    del_keys(item, "tracking_info", "")
    del_keys(item, "unlock_items", None)
    del_keys(item, "user_vas_order", operator=OPR.ANY)
    del_keys(item, "properties", {})
    del_keys(item, "suit_items", {})
    with contextlib.suppress(KeyError):
        del item["fan_user"]["avatar"]  # pyright: ignore[reportGeneralTypeIssues]
    replace_str(item, "http://", "https://")
    replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    # replace_str(item, "fasle", "false")
    h = d(BP + f, item)  # pyright: ignore[reportArgumentType]
    return g or h


def _I(a: str) -> None:
    b = set(_K())
    c = 1.2
    d = 100
    skip_1 = range(7000, 23300)
    match a:
        case "2":
            e = 100000001
            f = 140000001
        case "3":
            e = 200000001
            e = 232434101
            f = 250000001
        case "4":
            e = 300000001
            e = 336000001
            f = 337000001
        case "5":
            e = 400000001
            e = 407000001
            f = 409000001
        case "0" | "1" | _:
            d = 1
            e = 75500
            f = 76000
    with requests.Session() as g, tqdm(total=int((f - e) / d) + 1, initial=0, bar_format=_BF) as h:
        for i in range(e, f + d, d):
            h.update()
            if i in b:
                continue
            if i in z:
                continue
            if i in skip_1:
                continue
            h.set_description(str(i))
            time.sleep(c)
            j = _E(g, i)
            if j in {_D, _B}:
                continue
                print(f"{i:<12}N", end="\r")
            try:
                k: X1 = json.loads(j)["data"]
            except json.JSONDecodeError as e:
                print(j)
                raise
            if _H(i, k):
                h.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{i:<12}{k['name']:20}{len(j):>8}")
        h.write(f"{e} -> {f}")


def _N(j: str) -> None:
    a = _K()
    match j:
        case "0":
            k = range(1, 9999)
            m = 4424
        case "2":
            k = range(100000000, 199999999)
            m = 1722
        case "3":
            k = range(200000000, 299999999)
            m = 1069
        case "4":
            k = range(300000000, 399999999)
            m = 550
        case "5":
            k = range(400000000, 499999999)
            m = 80
        case "1":
            k = range(10000, 100000000 - 1)
            m = 30000
        case _:
            k = range(2**32)
            m = len(a) - 660
    h: list[int] = json.loads(open(BP + f"{TRASH}.json", encoding="utf-8").read())  # noqa: PTH123, SIM115
    h = []
    b = 1
    with requests.Session() as c, tqdm(total=m, initial=0, bar_format=_BF) as d:
        for g in a:
            # g += 1
            if g not in k:
                continue
            d.update()
            if g in h or str(g) in h:
                continue
            if g in z:
                continue
            time.sleep(b)
            n = _E(c, g)
            d.set_description(str(g))
            if n in {_D, _B}:
                if _G(IDCSV, f"{g},{TRASH},0,0"):
                    d.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{g:<12}🟥🟩🟦🟨⬛⬜ NOT Found")
                continue
            try:
                f: X1 = json.loads(n)["data"]
            except json.JSONDecodeError as e:
                print(e)
                raise
            try:
                if _H(g, f):
                    d.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{g:<12}{f['name']:20}{len(n):>8}")
            except KeyError:
                d.write(n.decode())
                raise


def _P(a: Path) -> None:
    # for b in a.iterdir():
    for b in tqdm(list(a.iterdir()), leave=False):
        if b.is_dir():
            _P(b)
            continue
        # log.warning(b)
        f = b.read_text("utf-8")
        if str(b).endswith(".jsonl"):
            for c in f.splitlines():
                d: X1 = json.loads(c)
                _H(d["item_id"], d)
        elif str(b).endswith(".json"):
            d: X1 = json.loads(f)
            try:
                _H(d["item_id"], d)
            except KeyError:
                _H(d["data"]["item_id"], d["data"])  # pyright: ignore[reportGeneralTypeIssues]


def _J() -> None:
    a = 1.2
    with requests.Session() as b:
        while True:
            c = input().strip()
            if c in "eeeeeeeexitEEEEEEEExit":
                return
            if not c or not c.isdigit():
                print(":(")
                continue
            c = int(c)
            d = _E(b, c)
            if d in {_D, _B}:
                print(f"{c:<12}None")
            else:
                try:
                    f: X1 = json.loads(d)["data"]
                except json.JSONDecodeError:
                    print("JSONDecodeError", d)
                    raise
                _H(c, f)
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{c:<12}{f['name']:20}{len(d):>8}")
            time.sleep(a)


def _K() -> list[int]:
    d: list[int] = []
    for a in ["PART_5_表情包", "PART_6_main"]:
        d.extend(int(b.stem) for b in Path(BP + a).rglob("*.json") if int(b.stem) not in z)
    for a in Path(BP).rglob("PART*.jsonl"):
        c = a.read_text(encoding="utf-8")
        d.extend(int(json.loads(b)["item_id"]) for b in c.splitlines())
    return d


if __name__ == "__main__":
    try:
        if len(sys.argv) > 2 and sys.argv[1] not in {"0", "1", "2", "3", "4", "5", "U", "u", "X", "x"}:
            _J()
        elif sys.argv[1] in {"0", "1", "2", "3", "4", "5"}:
            _I(sys.argv[1])
        elif sys.argv[1] in "Uu":
            _N(sys.argv[2])
        elif sys.argv[1] in "Xx":
            _P(Path(sys.argv[2]).resolve())
        else:
            _J()
    except IndexError:
        print("(script name)", "usage:")
        print("(script name)", "any input: repr")
        print("(script name)", "[0,1,2,3,4]: dl")
        print("(script name)", "u", "[0,1,2,3,4]", ": sync")
        print("(script name)", "x", "path-to-dir", ": sync with local files")
    except KeyboardInterrupt:
        pass
    except Exception as e_:
        log.exception(e_)
    finally:
        log.error(f"📦 {_a}")
