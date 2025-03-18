#!/usr/bin/python3
import json
import os
import ssl
import sys
import time

import requests
from loguru import logger
from tqdm import tqdm

from my_lib.xx_util import OPR, del_keys, sort_list_dict

log = logger.bind(user="X3")
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
_B = b'{"code":0,"message":"0","ttl":1,"data":{"packages":null}}'
_C: str = config["x3"]["url"]
_D: str = config["x3"]["bp"]
_O = [{}, {"no_access": True, "unlocked": False}, {"no_access": True}]


def _E(
    a: requests.Session,
    b: int | str,
    c: int | float,
) -> bytes:
    d = 0
    while d < 5:
        try:
            e = a.get(_C.format(q=b), headers=_A, verify=False, timeout=20)
            return e.content
        except requests.RequestException as e:
            d += 1
            print(" ")
            log.error(e)
            time.sleep(c)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
    raise Exception(f"Failed to fetch {b}")


def _F(a: str, b: str):
    open(a, "w", -1, "utf-8").write(b)


def _G(a: str, b: str):
    open(a, "a", -1, "utf-8").write(b + "\n")


def _K(a: int | str, b: dict) -> None:
    del_keys(b, "suggest", [""])
    del_keys(b, "flags", _O, OPR.IN)
    del_keys(b, "activity", None, OPR.ANY)
    del_keys(b, "label", None)
    del_keys(b, "attr", 0)
    del_keys(b, "package_sub_title", "")
    del_keys(b, "ref_mid", 0)
    del_keys(b, "resource_type", 0)
    if "emote" in b:
        b["emote"] = sort_list_dict(b["emote"], "id", "text")
    c = os.path.join(_D, f"{a}.json")
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    _F(c, d)
    _G(os.path.join(_D, "ids.csv"), f"{a},{b['text']}")


def _L() -> None:
    a = _N()
    b = 1
    c = 7800
    d = 10000
    with (
        requests.Session() as e,
        tqdm(
            total=d - c + 1,
            initial=0,
            bar_format="{desc}{percentage:3.0f}%|{bar}| {n_fmt}->{total_fmt} [{elapsed}->{remaining}]",
        ) as f,
    ):
        for g in range(c, d + 1):
            f.set_description(str(g))
            f.update()
            if g in a:
                pass
                continue
            if 6000 < g < 6800:
                continue
            time.sleep(b)
            h = _E(e, g, b)
            if h == _B:
                continue
            else:
                for i in json.loads(h)["data"]["packages"]:
                    _K(g, i)
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()):<32}{g:<12}{i['text']:20}")


def _M() -> None:
    a = 1
    with requests.Session() as b:
        while True:
            c = input("item_id:")
            time.sleep(a)
            d = _E(b, c, a)
            if d == _B:
                continue
            if c == "main":
                _L()
                break
            elif not c.isdigit():
                continue
            else:
                for e in json.loads(d)["data"]["packages"]:
                    _K(c, e)


def _N() -> list:
    try:
        a = []
        for b in os.listdir(_D):
            if b.endswith(".json") or b != "ids.csv":
                c = b.split(".")[0]
                a.append(int(c))
        a.sort()
        return list(set(a))
    except Exception:
        return []


if __name__ == "__main__":
    try:
        if sys.argv.__len__() > 1:
            _M()
        else:
            _L()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)
