#!/usr/bin/python3
import contextlib
import csv
import os
import ssl
import sys
import time
from pathlib import Path
from typing import TypedDict

import requests
from loguru import logger
from tqdm import tqdm

try:
    import simdjson as json
except ImportError:
    import json

from my_lib.xx_util import OPR, del_keys, replace_str, sort_list_dict, sort_p6_emoji, sort_str_list

log = logger.bind(user="X1")
ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
config = json.loads(Path("config.json").read_text(encoding="utf-8"))
_A = {
    "User-Agent": config["ua"],
    "Connection": "keep-alive",
    "Accept-Encoding": config["ae"],
}
_B = b'{"code":0,"message":"0","ttl":1,"data":{"suit_items":null,"fan_user":{"mid":0,"nickname":"","avatar":""},"unlock_items":null,"activity_entrance":null}}'
_EMPTY_FAN_USER = {"mid": 0, "nickname": "", "avatar": ""}
_EMPTY_ACTIVITY_ENTRANCE = {
    "id": 0,
    "item_id": 0,
    "title": "",
    "image_cover": "",
    "jump_link": "",
}
_L: str = config["x1"]["url"]
_M = str(Path(config["x1"]["bp"]).resolve()) + "/"
P = "properties"
S = "suit_items"
_a: int = 0
Properties = dict[str, str]
TRASH: str = "🗑"
IDCSV: str = "ids.csv"
Z = {
    "2060,2:3,19,1",
    "67055,豆泥大陆收藏家勋章,106,2",
    '1882,("▔□▔)/,7,4',
    "206537601,-Yu酱-婚纱主题装扮,47,6",
    "69105,-ASAKI-动态表情包,8,5",
}


def read_text(path, encoding=None, errors=None):
    with open(path, encoding=encoding, errors=errors) as f:  # noqa: FURB101
        return f.read()


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


def __():
    [] and _I  # type: ignore  # noqa: B018, SIM223


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
    while retry < 5:
        try:
            _a += 1
            c = b.get(_L.format(q=d), headers=_A, verify=False, timeout=20)
            c.raise_for_status()
            return c.content
        except requests.RequestException as e:
            retry += 1
            log.error(f" {d} {retry=}")
            # log.exception(e)
            time.sleep(1)
        except KeyboardInterrupt:
            raise KeyboardInterrupt  # noqa: B904
    raise Exception(f"Failed to fetch {d}")


def _F(a: str, b: X1) -> None:
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    e = ""
    if os.path.isfile(a):
        e = open(a, encoding="utf-8").read()
        if d == e:
            return
        c: X1 = json.loads(e)
        if isinstance(b.get(P), dict):
            if isinstance(b[P].get("item_ids"), str) and isinstance(c[P].get("item_ids"), str):
                b[P]["item_ids"] = sort_str_list(b[P]["item_ids"] + "," + c[P]["item_ids"])
            if isinstance(b[P].get("fan_item_ids"), str) and isinstance(c[P].get("fan_item_ids"), str):
                b[P]["fan_item_ids"] = sort_str_list(b[P]["fan_item_ids"] + "," + c[P]["fan_item_ids"])
        # ============================
        for i in c.get(S, {}):
            if i in c[S]:
                if i not in b[S]:
                    b[S][i] = c[S][i]
                else:
                    for g in c[S][i]:
                        if (h := json.dumps(g, ensure_ascii=False)) not in (f := {json.dumps(j, ensure_ascii=False) for j in b[S][i]}):
                            b[S][i].append(g)
                            f.add(h)
            if i in b[S]:
                sort_list_dict(b[S][i], "item_id", "name")  # type: ignore
    # ============================
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if e and d == e:
        return
    open(a, "w", encoding="utf-8").write(d)


def _G(a: str, b: str) -> None:
    if isinstance(b, dict):
        b = json.dumps(b, ensure_ascii=False, separators=(",", ":"))
    """Csv / jsonl."""
    if b in Z or (os.path.isfile(a) and b in open(a, encoding="utf-8").read()):
        return
    with open(a, "a", encoding="utf-8") as fp:
        fp.write(b + "\n")


def _H(a: int | str, item: X1) -> None:
    c = item["part_id"]
    d = _G
    d(_M + IDCSV, f"{a},{item['name']},{item['group_id']},{c}")
    if isinstance(item.get(P), dict):
        if isinstance(item[P].get("item_ids"), str):
            item[P]["item_ids"] = sort_str_list(item[P]["item_ids"])
        if isinstance(item[P].get("fan_item_ids"), str):
            item[P]["fan_item_ids"] = sort_str_list(item[P]["fan_item_ids"])
    if isinstance(item.get(S), dict):
        if isinstance(item[S].get("emoji"), list):
            sort_list_dict(item[S]["emoji"])  # type: ignore
        if isinstance(item[S].get("card"), list):
            sort_list_dict(item[S]["card"])  # type: ignore
        if isinstance(item[S].get("card_bg"), list):
            sort_list_dict(item[S]["card_bg"])  # type: ignore
        if isinstance(item[S].get("loading"), list):
            sort_list_dict(item[S]["loading"])  # type: ignore
        if isinstance(item[S].get("pendant"), list):
            sort_list_dict(item[S]["pendant"])  # type: ignore
        if isinstance(item[S].get("play_icon"), list):
            sort_list_dict(item[S]["play_icon"])  # type: ignore
        if isinstance(item[S].get("skin"), list):
            sort_list_dict(item[S]["skin"])  # type: ignore
        if isinstance(item[S].get("space_bg"), list):
            sort_list_dict(item[S]["space_bg"])  # type: ignore
        if isinstance(item[S].get("thumbup"), list):
            sort_list_dict(item[S]["thumbup"])  # type: ignore
        if isinstance(item[S].get("emoji_package"), list):
            sort_p6_emoji(item[S]["emoji_package"])  # type: ignore
    match c:
        case 1:
            f = "PART_1_头像框.jsonl"
        case 2:
            f = "PART_2_动态卡片.jsonl"
        case 3:
            f = "PART_3_点赞效果.jsonl"
        case 4:
            f = "PART_4_表情.jsonl"
        case 5:
            d = _F
            f = f"PART_5_表情包\\{a}.json"
        case 6:
            d = _F
            f = f"PART_6_main\\{a}.json"
        case 7:
            f = "PART_7_空间背景.jsonl"
        case 8:
            f = "PART_8_勋章.jsonl"
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
    del_keys(item, "associate", operator=OPR.ANY)
    del_keys(item, "current_activity", operator=OPR.ANY)
    del_keys(item, "current_sources", operator=OPR.ANY)
    del_keys(item, "gray_rule_type", operator=OPR.ANY)
    del_keys(item, "gray_rule", operator=OPR.ANY)
    del_keys(item, "hot", operator=OPR.ANY)
    del_keys(item, "is_symbol", operator=OPR.ANY)
    del_keys(item, "item_stock_surplus", operator=OPR.ANY)
    del_keys(item, "next_activity", operator=OPR.ANY)
    del_keys(item, "non_associate", operator=OPR.ANY)
    del_keys(item, "open_platform_vip_discount", operator=OPR.ANY)
    del_keys(item, "realname_auth", operator=OPR.ANY)
    del_keys(item, "sale_count_desc", operator=OPR.ANY)
    del_keys(item, "sale_left_time", operator=OPR.ANY)
    del_keys(item, "sale_promo", operator=OPR.ANY)
    del_keys(item, "sale_surplus", operator=OPR.ANY)
    del_keys(item, "sale_time_end", recursive=False, operator=OPR.ANY)
    del_keys(item, "state", operator=OPR.ANY)
    del_keys(item, "tag", operator=OPR.ANY)
    del_keys(item, "total_count_desc", operator=OPR.ANY)
    del_keys(item, "user_vas_order", operator=OPR.ANY)
    del_keys(item, "activity_entrance", _EMPTY_ACTIVITY_ENTRANCE, recursive=False)
    del_keys(item, "activity_entrance", None, recursive=False)
    del_keys(item, "associate_words", "")
    del_keys(item, "fan_user", _EMPTY_FAN_USER, recursive=False)
    del_keys(item, "finish_sources", None)
    del_keys(item, "items", None)
    del_keys(item, "jump_link", "")
    del_keys(item, "ref_mid", "0")
    del_keys(item, "sale_time_end", 0, OPR.LEQ)
    del_keys(item, "sales_mode", 0)
    del_keys(item, "suit_item_id", 0)
    del_keys(item, "tab_id", 0, OPR.EQ)
    del_keys(item, "unlock_items", None)
    del_keys(item, "properties", {})
    del_keys(item, "suit_items", {})
    with contextlib.suppress(KeyError):
        del item["fan_user"]["avatar"]  # type: ignore
    replace_str(item, "http://", "https://")
    replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    # replace_str(item, "fasle", "false")
    d(_M + f, item)  # type: ignore


def _I(a: str) -> None:
    b = set(_K())
    c = 1
    d = 100
    match a:
        case "2":
            e = 100000001
            f = 140000001
        case "3":
            e = 200000001
            # e = 232434101
            f = 250000001
        case "4":
            e = 300000001
            e = 321000001
            f = 322000001
        case "0" | "1" | _:
            d = 1
            e = 73700
            f = 73900
    with (
        requests.Session() as g,
        tqdm(total=int((f - e) / d) + 1, initial=0, bar_format="{desc}{percentage:3.0f}%|{bar}| {n_fmt}->{total_fmt} [{elapsed}->{remaining}]") as h,
    ):
        for i in range(e, f + d, d):
            h.update()
            if i in b:
                continue
            if 7000 < i < 23330:
                continue
            h.set_description(str(i))
            time.sleep(c)
            j = _E(g, i)
            if j == _B:
                continue
                print(f"{i:<12}N", end="\r")
            try:
                k: X1 = json.loads(j)["data"]
            except json.JSONDecodeError as e:  # type: ignore
                print(j)
                raise e
            _H(i, k)
            h.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{i:<12}{k['name']:20}{len(j):>8}")


def _N(j) -> None:
    a = _K()
    match j:
        case "0":
            k = range(1, 9999)
            m = 4450
        case "2":
            k = range(100000000, 199999999)
            m = 1691 - 431
        case "3":
            k = range(200000000, 299999999)
            m = 1061 - 166
        case "4":
            k = range(300000000, 399999999)
            m = 400 - 5
        case "1":
            k = range(10000, 100000000 - 1)
            m = 30000
        case _:
            k = range(2**32)
            m = len(a) - 660
    # h: list[int] = json.loads(open(_M + f"{TRASH}.json", encoding="utf-8").read())
    h = []
    b = 1
    with (
        requests.Session() as c,
        tqdm(total=m, initial=0, bar_format="{percentage:3.0f}%|{bar}| {n_fmt}->{total_fmt} [{elapsed}->{remaining}]") as d,
    ):
        for g in a:
            if g in h or str(g) in h or (g not in k):
                continue
            time.sleep(b)
            e = _E(c, g)
            if e == _B:
                _G(_M + IDCSV, f"{g},{TRASH},0,0")
                d.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{g:<12}🟥🟩🟦🟨⬛⬜ NOT Found")
                continue
            try:
                f: X1 = json.loads(e)["data"]
            except json.JSONDecodeError as n:  # type: ignore
                print(n)
                raise n
            _H(g, f)
            d.update()
            d.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{g:<12}{f['name']:20}{len(e):>8}")


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
                _H(d["data"]["item_id"], d["data"])  # type: ignore


def _J() -> None:
    a = 2
    with requests.Session() as b:
        while True:
            c = input()
            d = _E(b, c)
            if d == _B:
                print(f"{c:<12}None")
            else:
                try:
                    e: X1 = json.loads(d)["data"]
                except json.JSONDecodeError as f:  # type: ignore
                    print(d)
                    raise f
                _H(c, e)
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{c:<12}{e['name']:20}{len(d):>8}")
            time.sleep(a)


def _K() -> list[int]:
    g: list[int] = []
    for a in ["PART_5_表情包", "PART_6_main"]:
        for b in Path(_M + a).rglob("*.json"):
            g.append(int(b.stem))
    for a in Path(_M).rglob("PART*.jsonl"):
        c = a.read_text(encoding="utf-8")
        for d in c.splitlines():
            f = json.loads(d)
            g.append(int(f["item_id"]))
    return g


def _O():
    a = []
    b = []
    c = _M + IDCSV
    d = csv.reader(open(c, encoding="utf-8").read())
    next(d)
    for f in d:
        if f[1] == TRASH:
            b.append(int(f[0]))
        else:
            a.append(int(f[0]))
    return a, b


if __name__ == "__main__":
    try:
        if len(sys.argv) > 2 and sys.argv[1] not in "0u1U2x3X4":
            _J()
        elif sys.argv[1] in {"0", "1", "2", "3", "4"}:
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
    except Exception as e:
        log.exception(e)
    finally:
        log.error(f"📦 {_a}")
