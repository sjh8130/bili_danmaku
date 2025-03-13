#!/usr/bin/python3
import json
import os
import ssl
import sys
import time

import requests
from loguru import logger
from tqdm import tqdm

from my_lib.xx_util import OPR, del_keys, sort_list_dict, sort_p6_emoji, sort_str_list

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
_C = {"mid": 0, "nickname": "", "avatar": ""}
_D = {
    "id": 0,
    "item_id": 0,
    "title": "",
    "image_cover": "",
    "jump_link": "",
}
_L: str = config["x1"]["url"]
_M: str = config["x1"]["bp"]
_N = "properties"
_O = "suit_items"


def _E(b: requests.Session, d: int | str) -> bytes:
    a = 0
    while a < 5:
        try:
            c = b.get(_L.format(q=d), headers=_A, verify=False, timeout=20)
            c.raise_for_status()
            return c.content
        except requests.RequestException as e:
            a += 1
            print(" ")
            log.error(e)
            time.sleep(1)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
    raise Exception(f"Failed to fetch {d}")


def _F(a: str, b: str):
    with open(a, "w", 1048576, "utf-8") as fp:
        fp.write(b)


def _G(a: str, b: str):
    with open(a, "a", 1048576, "utf-8") as fp:
        fp.write(b + "\n")


def _H(a: int | str, b: dict) -> None:
    c = b["part_id"]
    d = _G
    d(f"{_M}\\ids.csv", f"{a},{b['name']},{b['group_id']},{c}")
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
            if isinstance(b.get(_N), dict):
                if isinstance(b[_N].get("item_ids"), str):
                    b[_N]["item_ids"] = sort_str_list(b[_N]["item_ids"])
            elif isinstance(b.get(_O), dict):
                if isinstance(b[_O].get("emoji"), list):
                    b[_O]["emoji"] = sort_list_dict(b[_O]["emoji"])
        case 6:
            e = "\t"
            d = _F
            f = f"PART_6_main\\{a}.json"
            if isinstance(b.get(_N), dict):
                if isinstance(b[_N].get("fan_item_ids"), str):
                    b[_N]["fan_item_ids"] = sort_str_list(b[_N]["fan_item_ids"])
            elif isinstance(b.get(_O), dict):
                if isinstance(b[_O].get("card"), list):
                    b[_O]["card"] = sort_list_dict(b[_O]["card"])
                elif isinstance(b[_O].get("card_bg"), list):
                    b[_O]["card_bg"] = sort_list_dict(b[_O]["card_bg"])
                elif isinstance(b[_O].get("loading"), list):
                    b[_O]["loading"] = sort_list_dict(b[_O]["loading"])
                elif isinstance(b[_O].get("pendant"), list):
                    b[_O]["pendant"] = sort_list_dict(b[_O]["pendant"])
                elif isinstance(b[_O].get("play_icon"), list):
                    b[_O]["play_icon"] = sort_list_dict(b[_O]["play_icon"])
                elif isinstance(b[_O].get("skin"), list):
                    b[_O]["skin"] = sort_list_dict(b[_O]["skin"])
                elif isinstance(b[_O].get("space_bg"), list):
                    b[_O]["space_bg"] = sort_list_dict(b[_O]["space_bg"])
                elif isinstance(b[_O].get("thumbup"), list):
                    b[_O]["thumbup"] = sort_list_dict(b[_O]["thumbup"])
                elif isinstance(b[_O].get("emoji_package"), list):
                    b[_O]["emoji_package"] = sort_p6_emoji(b[_O]["emoji_package"])
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
    del_keys(b, "current_activity", operator=OPR.ANY)
    del_keys(b, "current_sources", operator=OPR.ANY)
    del_keys(b, "gray_rule_type", operator=OPR.ANY)
    del_keys(b, "gray_rule", operator=OPR.ANY)
    del_keys(b, "hot", operator=OPR.ANY)
    del_keys(b, "is_symbol", operator=OPR.ANY)
    del_keys(b, "item_stock_surplus", operator=OPR.ANY)
    del_keys(b, "next_activity", operator=OPR.ANY)
    del_keys(b, "open_platform_vip_discount", operator=OPR.ANY)
    del_keys(b, "sale_count_desc", operator=OPR.ANY)
    del_keys(b, "sale_left_time", operator=OPR.ANY)
    del_keys(b, "sale_promo", operator=OPR.ANY)
    del_keys(b, "sale_surplus", operator=OPR.ANY)
    del_keys(b, "sale_time_end", recursive=False, operator=OPR.ANY)
    del_keys(b, "state", operator=OPR.ANY)
    del_keys(b, "tag", operator=OPR.ANY)
    del_keys(b, "total_count_desc", operator=OPR.ANY)
    del_keys(b, "activity_entrance", _D, recursive=False)
    del_keys(b, "activity_entrance", None, recursive=False)
    del_keys(b, "associate_words", "")
    del_keys(b, "fan_user", _C, recursive=False)
    del_keys(b, "finish_sources", None)
    del_keys(b, "items", None)
    del_keys(b, "jump_link", "")
    del_keys(b, "ref_mid", "0")
    del_keys(b, "sale_time_end", 0, OPR.LEQ)
    del_keys(b, "sales_mode", 0)
    del_keys(b, "suit_item_id", 0)
    del_keys(b, _N, {})
    del_keys(b, _O, {})
    del_keys(b, "unlock_items", None)
    g = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent=e)
    d(os.path.join(_M, f), g)


def _I(a: str) -> None:
    b: set[int] = _K()
    c = 1
    d = 100
    match a:
        case "2":
            e = 100000001
            f = 140000102
        case "3":
            e = 200000001
            e = 232434101
            f = 250000002
        case "4":
            e = 300000001
            e = 305848101
            f = 310000002
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
                h.write(
                    f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{i:<12}{k['name']:20}{len(j):>8}"
                )


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
                print(
                    f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{c:<12}{e['name']:20}{len(d):>8}"
                )
            time.sleep(a)


def _K() -> set[int]:
    d: list[int] = []
    a: list[str] = ["PART_5_表情包", "PART_6_main"]
    for b in a:
        i = os.path.join(_M, b)
        for c in os.listdir(i):
            if c.endswith(".json"):
                d.append(int(c.split(".")[0]))
    for c in os.listdir(_M):
        if (c.endswith(".jsonl") or c.endswith(".json")) and c != "UNKNOWN_IDs.jsonl":
            e = os.path.join(_M, c)
            with open(e, "r", encoding="utf-8") as f:
                for g in f:
                    h = json.loads(g)
                    d.append(int(h["item_id"]))
    d.sort()
    return set(d)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1 and sys.argv[1] not in ["0", "1", "2", "3", "4"]:
            _J()
        elif sys.argv[1] in ["0", "1", "2", "3", "4"]:
            _I(sys.argv[1])
        else:
            _I("0")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)
