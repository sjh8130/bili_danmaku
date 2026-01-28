import json
import ssl
import time
from pathlib import Path
from typing import TypedDict

import requests
from loguru import logger
from tqdm import tqdm

from my_lib.xx_util import OPR, del_keys

log = logger.bind(user="X4")
ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # pyright: ignore[reportAttributeAccessIssue]
_A = json.loads(Path("config.json").read_text(encoding="utf-8"))
_B = {"User-Agent": _A["ua"], "Connection": "keep-alive", "Accept-Encoding": _A["ae"]}
_C: str = _A["x4"]["url"]
_D = Path(_A["x4"]["bp"]).resolve()
_E = _A["bar_format"]
_a: int = 0
LIST = list


class _F(TypedDict):
    current_activity: dict
    current_sources: int | None
    finish_sources: int | None
    group_id: int
    group_name: str
    item_id: int
    jump_link: str
    name: str
    next_activity: dict
    part_id: int
    properties: dict
    sale_count_desc: str
    sale_left_time: int
    sale_surplus: int
    sale_time_end: int
    sales_mode: int
    state: str
    tag: str
    total_count_desc: str


class _G(TypedDict):
    total: int
    pn: int
    ps: int


class _H(TypedDict):
    group: str
    has_more: int
    list: LIST[_F]
    offset_info: str
    page: _G


def _X(b: requests.Session, d: int | str) -> bytes:
    global _a  # noqa: PLW0603
    retry = 0
    while retry < 10:
        try:
            _a += 1
            c = b.get(_C.format(q=d), headers=_B, verify=False, timeout=20)
            c.raise_for_status()
            return c.content
        except requests.RequestException as e:  # noqa: F841, PERF203
            retry += 1
            log.error(f" {d} {retry=}")
            # log.exception(e)
            time.sleep(retry)
        except KeyboardInterrupt:
            raise KeyboardInterrupt from None
    raise Exception(f"Failed to fetch {d}")


def _Y(a, b) -> bool:
    if isinstance(b, (dict, list)):
        b = json.dumps(b, ensure_ascii=False, separators=(",", ":"))
    while True:
        try:
            a.write(b + "\n")
            break
        except PermissionError:
            log.error("PermissionError")
            time.sleep(10)
    return True


def _Z():
    a = 1.2
    b = 500
    c = 1
    d = 20
    e = 0
    n = 0
    with requests.Session() as f, open(_D, "a", encoding="utf-8") as g, tqdm(bar_format=_E) as h:
        while ((e < b) or (c * d > b + 1)) and n < 4:
            i = _X(f, c)
            try:
                j: _H = json.loads(i)["data"]
            except json.JSONDecodeError as m:
                print(i.decode("utf-8").encode())
                raise m
            if len(j["list"]) == 0:
                n += 1
                h.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<22}{'empty':8}{n}")
            n = 0
            b = max(b, j["page"]["total"])
            h.total = j["page"]["total"]
            e += len(j["list"])
            h.n += len(j["list"])
            for k in j["list"]:
                del_keys(j, "activity_entrance", operator=OPR.FALSE_CMP)
                del_keys(j, "associate_words", operator=OPR.FALSE_CMP)
                del_keys(j, "associate", operator=OPR.ANY)
                del_keys(j, "current_activity", operator=OPR.ANY)
                del_keys(j, "current_sources", operator=OPR.ANY)
                del_keys(j, "fan_item_ids", operator=OPR.ANY)
                del_keys(j, "finish_sources", operator=OPR.FALSE_CMP)
                del_keys(j, "gray_rule_type", operator=OPR.ANY)
                del_keys(j, "gray_rule", operator=OPR.ANY)
                del_keys(j, "hot", operator=OPR.ANY)
                del_keys(j, "is_symbol", operator=OPR.ANY)
                del_keys(j, "item_stock_surplus", operator=OPR.ANY)
                del_keys(j, "items", operator=OPR.FALSE_CMP)
                del_keys(j, "jump_link", operator=OPR.FALSE_CMP)
                del_keys(j, "next_activity", operator=OPR.ANY)
                del_keys(j, "non_associate", operator=OPR.ANY)
                del_keys(j, "open_platform_vip_discount", operator=OPR.ANY)
                del_keys(j, "properties", operator=OPR.FALSE_CMP)
                del_keys(j, "realname_auth", operator=OPR.ANY)
                del_keys(j, "ref_mid", "0")
                del_keys(j, "sale_count_desc", operator=OPR.ANY)
                del_keys(j, "sale_left_time", operator=OPR.ANY)
                del_keys(j, "sale_promo", operator=OPR.ANY)
                del_keys(j, "sale_surplus", operator=OPR.ANY)
                del_keys(j, "sale_time_end", OPR.ANY)
                del_keys(j, "sales_mode", operator=OPR.FALSE_CMP)
                del_keys(j, "state", operator=OPR.ANY)
                del_keys(j, "suit_item_id", operator=OPR.FALSE_CMP)
                del_keys(j, "suit_items", operator=OPR.FALSE_CMP)
                del_keys(j, "tab_id", operator=OPR.FALSE_CMP)
                del_keys(j, "tag", operator=OPR.ANY)
                del_keys(j, "time_left", operator=OPR.ANY)
                del_keys(j, "total_count_desc", operator=OPR.ANY)
                del_keys(j, "unlock_items", operator=OPR.FALSE_CMP)
                del_keys(j, "user_vas_order", operator=OPR.ANY)
                _Y(g, k)
                h.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<22}{k['item_id']:<10}{k['name']}")
            c += 1
            time.sleep(a)


if __name__ == "__main__":
    try:
        _Z()
    except IndexError:
        print(":(")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)
    finally:
        log.error(f"📦 {_a}")
