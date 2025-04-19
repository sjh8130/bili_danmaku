#!/usr/bin/python3
import glob
import json
import os
import ssl
import sys
import time

import requests
from loguru import logger
from tqdm import tqdm

from my_lib.xx_util import OPR, del_keys, replace_str, sort_list_dict, sort_p6_emoji, sort_str_list

log = logger.bind(user="X1")
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with open("config.json", "r", -1, "utf-8") as fp:
    config = json.load(fp)
del fp
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
_M: str = config["x1"]["bp"]
P = "properties"
S = "suit_items"
_a: int = 0


def _E(b: requests.Session, d):
    global _a
    a = 0
    while a < 5:
        try:
            _a += 1
            c = b.get(_L.format(q=d), headers=_A, verify=False, timeout=20)
            c.raise_for_status()
            return c.content
        except requests.RequestException as e:
            a += 1
            # print(" ")
            # log.error(e)
            log.error(f"Failed to fetch {d},{e}, retry:{a}")
            time.sleep(1)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
    raise Exception(f"Failed to fetch {d}")


def _F(a: str, b: str):
    if os.path.isfile(a):
        with open(a, "r", 1048576, "utf-8") as fp:
            if b == fp.read():
                return
    with open(a, "w", 1048576, "utf-8") as fp:
        fp.write(b)


def _G(a: str, b: str):
    if os.path.isfile(a):
        with open(a, "r", 1048576, "utf-8") as fp:
            if (c := b + "\n") in (x := fp.readlines()) or b in x:
                return
    with open(a, "a", 1048576, "utf-8") as fp:
        fp.write(c)


def _H(a: int | str, item: dict) -> None:
    c = item["part_id"]
    d = _G
    d(f"{_M}\\ids.csv", f"{a},{item['name']},{item['group_id']},{c}")
    e = None
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
            e = "\t"
            d = _F
            f = f"PART_5_表情包\\{a}.json"
            if isinstance(item.get(P), dict):
                if isinstance(item[P].get("item_ids"), str):
                    item[P]["item_ids"] = sort_str_list(item[P]["item_ids"])
            if isinstance(item.get(S), dict):
                if isinstance(item[S].get("emoji"), list):
                    sort_list_dict(item[S]["emoji"])
        case 6:
            e = "\t"
            d = _F
            f = f"PART_6_main\\{a}.json"
            if isinstance(item.get(P), dict):
                if isinstance(item[P].get("fan_item_ids"), str):
                    item[P]["fan_item_ids"] = sort_str_list(item[P]["fan_item_ids"])
            if isinstance(item.get(S), dict):
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
                    item[S]["emoji_package"] = sort_p6_emoji(item[S]["emoji_package"])
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
    replace_str(item, "http://", "https://")
    replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "fasle", "false")
    b = json.dumps(item, ensure_ascii=False, separators=(",", ":"), indent=e)
    d(os.path.join(_M, f), b)


def _I(a: str) -> None:
    b = _K()
    c = 1
    d = 100
    match a:
        case "2":
            e = 100000001
            f = 140000102
        case "3":
            e = 200000001
            # e = 232434101
            f = 250000002
        case "4":
            e = 300000001
            e = 309000001
            f = 311000002
        case "0" | "1" | _:
            d = 1
            e = 72500
            f = 73000
    with (
        requests.Session() as g,
        tqdm(
            total=int((f - e) / d) + 1,
            initial=0,
            bar_format="{desc}{percentage:3.0f}%|{bar}| {n_fmt}->{total_fmt} [{elapsed}->{remaining}]",
        ) as h,
    ):
        for i in range(e, f + d, d):
            h.update()
            if i in b:
                pass
                continue
            if 7000 < i < 23330:
                continue
            h.set_description(str(i))
            time.sleep(c)
            j = _E(g, i)
            if j == _B:
                continue
                print(f"{i:<12}N", end="\r")
            else:
                try:
                    k: dict = json.loads(j)["data"]
                except json.JSONDecodeError as e:
                    print(j)
                    raise e
                _H(i, k)
                h.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{i:<12}{k['name']:20}{len(j):>8}")


def _N() -> None:
    a = _K()
    b = 1
    with (
        requests.Session() as c,
        tqdm(
            total=len(a),
            initial=0,
            bar_format="{percentage:3.0f}%|{bar}| {n_fmt}->{total_fmt} [{elapsed}->{remaining}]",
        ) as d,
    ):
        for g in a:
            time.sleep(b)
            e = _E(c, g)
            d.update()
            if e == _B:
                d.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{g:<12}🟥🟩🟦🟨⬛⬜ NOT Found")
                continue
            else:
                try:
                    f: dict = json.loads(e)["data"]
                except json.JSONDecodeError as e:
                    print(e)
                    raise e
                _H(g, f)
                d.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{g:<12}{f['name']:20}{len(e):>8}")


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
                    e: dict = json.loads(d)["data"]
                except json.JSONDecodeError as f:
                    print(d)
                    raise f
                _H(c, e)
                print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{c:<12}{e['name']:20}{len(d):>8}")
            time.sleep(a)


def _K() -> set[int]:
    A: list[int] = []
    for a in ["PART_5_表情包", "PART_6_main"]:
        for b in glob.glob("*.json", root_dir=os.path.join(_M, a)):
            A.append(int(b.split(".")[0]))
    for a in glob.glob("PART*.jsonl", root_dir=_M):
        with open(os.path.join(_M, a), "r", encoding="utf-8") as c:
            for d in c.readlines():
                f = json.loads(d)
                A.append(int(f["item_id"]))
    return set(A)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1 and sys.argv[1] not in ["0", "1", "2", "3", "4", "U", "u"]:
            _J()
        elif sys.argv[1] in ["0", "1", "2", "3", "4"]:
            _I(sys.argv[1])
        elif sys.argv[1] in "Uu":
            _N()
        else:
            _I("0")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)
    finally:
        log.error(f"📦 {_a}")
