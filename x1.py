#!/usr/bin/python3
import json
import os
import ssl
import sys
import time
from enum import StrEnum, auto

import requests
from loguru import logger
from tqdm import tqdm

log = logger.bind(user="X1")
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
_A = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, bzip2, br, zstd",
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
with open("config.json", "r", -1, "utf-8") as fp:
    config = json.load(fp)
del fp
_L: str = config["x1"]["url"]
_M: str = config["x1"]["bp"]


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
            log.exception(e)
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


def _sort_str_list(s: str, /) -> str:
    """example: '1,3,2,4,5' -> '1,2,3,4,5'"""
    if s.count(",") == 0:
        return s
    a = json.loads(f"[{s}]")
    b = sorted(a)
    return ",".join(str(c) for c in b)


def _sort_list_dict(
    ld: list[dict],
    k1: str = "item_id",
    k2: str = "name",
    /,
) -> list[dict]:
    items_with_k1 = [item for item in ld if item[k1] not in {0, "0"}]
    items_with_k2 = [item for item in ld if item[k1] in {0, "0"}]
    items_with_k1.sort(key=lambda x: x[k1])
    items_with_k2.sort(key=lambda x: x[k2])
    return items_with_k1 + items_with_k2


def _sort_p6_emoji(ld: list[dict], /) -> list[dict]:
    for i in range(len(ld)):
        if isinstance(ld[i].get("properties"), dict):
            if isinstance(ld[i]["properties"].get("item_ids"), str):
                ld[i]["properties"]["item_ids"] = _sort_str_list(
                    ld[i]["properties"]["item_ids"]
                )
        ld[i]["items"] = _sort_list_dict(ld[i]["items"])
    return ld


class OPR(StrEnum):
    EQ = auto()
    NEQ = auto()
    GT = auto()
    LT = auto()
    GEQ = auto()
    LEQ = auto()
    ANY = auto()
    IN = auto()
    INEQ = auto()
    NIN = auto()
    IS = auto()
    NIS = auto()


def _del_keys(d: dict, k: str, v=None, operator: OPR = OPR.EQ, recursive=True):
    if (
        k in d
        and isinstance(d, dict)
        and (type(d[k]) is type(v) or operator in (OPR.IN, OPR.INEQ, OPR.ANY))
    ):
        match operator:
            case OPR.EQ:
                if d[k] == v:
                    d.pop(k)
            case OPR.IN | OPR.INEQ:
                if d[k] in v:  # type: ignore
                    d.pop(k)
            case OPR.ANY:
                d.pop(k)
            case OPR.GT:
                if isinstance(d[k], (int, float)) and d[k] > v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.LT:
                if isinstance(d[k], (int, float)) and d[k] < v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.GEQ:
                if isinstance(d[k], (int, float)) and d[k] >= v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.LEQ:
                if isinstance(d[k], (int, float)) and d[k] <= v:
                    del d[k]
                else:
                    raise ValueError(f"{d}|{k}|{operator}|{v}")
            case OPR.NEQ:
                if d[k] != v:
                    d.pop(k)
            case OPR.NIN:
                if d[k] not in v:
                    d.pop(k)
            case OPR.IS:
                if d[k] is v:
                    d.pop(k)
            case OPR.NIS:
                if d[k] is not v:
                    d.pop(k)
            case _:
                raise Exception("*ToDo")
    if not recursive:
        return
    for key in d:
        if isinstance(d[key], dict):
            _del_keys(d[key], k, v, operator)
        elif isinstance(d[key], list):
            for item in d[key]:
                if isinstance(item, dict):
                    _del_keys(item, k, v, operator)


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
            if isinstance(b.get("properties"), dict):
                if isinstance(b["properties"].get("item_ids"), str):
                    b["properties"]["item_ids"] = _sort_str_list(
                        b["properties"]["item_ids"]
                    )
            elif isinstance(b.get("suit_items"), dict):
                if isinstance(b["suit_items"].get("emoji"), list):
                    b["suit_items"]["emoji"] = _sort_list_dict(b["suit_items"]["emoji"])
        case 6:
            e = "\t"
            d = _F
            f = f"PART_6_main\\{a}.json"
            if isinstance(b.get("properties"), dict):
                if isinstance(b["properties"].get("fan_item_ids"), str):
                    b["properties"]["fan_item_ids"] = _sort_str_list(
                        b["properties"]["fan_item_ids"]
                    )
            elif isinstance(b.get("suit_items"), dict):
                if isinstance(b["suit_items"].get("card"), list):
                    b["suit_items"]["card"] = _sort_list_dict(b["suit_items"]["card"])
                elif isinstance(b["suit_items"].get("card_bg"), list):
                    b["suit_items"]["card_bg"] = _sort_list_dict(
                        b["suit_items"]["card_bg"]
                    )
                elif isinstance(b["suit_items"].get("loading"), list):
                    b["suit_items"]["loading"] = _sort_list_dict(
                        b["suit_items"]["loading"]
                    )
                elif isinstance(b["suit_items"].get("pendant"), list):
                    b["suit_items"]["pendant"] = _sort_list_dict(
                        b["suit_items"]["pendant"]
                    )
                elif isinstance(b["suit_items"].get("play_icon"), list):
                    b["suit_items"]["play_icon"] = _sort_list_dict(
                        b["suit_items"]["play_icon"]
                    )
                elif isinstance(b["suit_items"].get("skin"), list):
                    b["suit_items"]["skin"] = _sort_list_dict(b["suit_items"]["skin"])
                elif isinstance(b["suit_items"].get("space_bg"), list):
                    b["suit_items"]["space_bg"] = _sort_list_dict(
                        b["suit_items"]["space_bg"]
                    )
                elif isinstance(b["suit_items"].get("thumbup"), list):
                    b["suit_items"]["thumbup"] = _sort_list_dict(
                        b["suit_items"]["thumbup"]
                    )
                elif isinstance(b["suit_items"].get("emoji_package"), list):
                    b["suit_items"]["emoji_package"] = _sort_p6_emoji(
                        b["suit_items"]["emoji_package"]
                    )
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
    _del_keys(b, "current_activity", operator=OPR.ANY)
    _del_keys(b, "current_sources", operator=OPR.ANY)
    _del_keys(b, "gray_rule_type", operator=OPR.ANY)
    _del_keys(b, "gray_rule", operator=OPR.ANY)
    _del_keys(b, "hot", operator=OPR.ANY)
    _del_keys(b, "is_symbol", operator=OPR.ANY)
    _del_keys(b, "item_stock_surplus", operator=OPR.ANY)
    _del_keys(b, "next_activity", operator=OPR.ANY)
    _del_keys(b, "open_platform_vip_discount", operator=OPR.ANY)
    _del_keys(b, "sale_count_desc", operator=OPR.ANY)
    _del_keys(b, "sale_left_time", operator=OPR.ANY)
    _del_keys(b, "sale_promo", operator=OPR.ANY)
    _del_keys(b, "sale_surplus", operator=OPR.ANY)
    _del_keys(b, "sale_time_end", recursive=False, operator=OPR.ANY)
    _del_keys(b, "state", operator=OPR.ANY)
    _del_keys(b, "tag", operator=OPR.ANY)
    _del_keys(b, "total_count_desc", operator=OPR.ANY)
    _del_keys(b, "activity_entrance", _D, recursive=False)
    _del_keys(b, "activity_entrance", None, recursive=False)
    _del_keys(b, "associate_words", "")
    _del_keys(b, "fan_user", _C, recursive=False)
    _del_keys(b, "finish_sources", None)
    _del_keys(b, "items", None)
    _del_keys(b, "jump_link", "")
    _del_keys(b, "ref_mid", "0")
    _del_keys(b, "sale_time_end", 0, OPR.LEQ)
    _del_keys(b, "sales_mode", 0)
    _del_keys(b, "suit_item_id", 0)
    _del_keys(b, "suit_items", {})
    _del_keys(b, "unlock_items", None)
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
            e = 305547001
            f = 310000002
        case "1" | _:
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
