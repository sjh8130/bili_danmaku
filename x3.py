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

from my_lib.xx_util import OPR, del_keys, replace_str, sort_list_dict

log = logger.bind(user="X3")
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with open("config.json", "r", -1, "utf-8") as a:
    config = json.load(a)
del a
_A = {
    "User-Agent": config["ua"],
    "Connection": "keep-alive",
    "Accept-Encoding": config["ae"],
}
_B = b'{"code":0,"message":"0","ttl":1,"data":{"packages":null}}'
_C = config["x3"]["url"]
_D = config["x3"]["bp"]
_O = [{}, {"no_access": True, "unlocked": False}, {"no_access": True}]
_a = 0


def _E(a, b, c):
    global _a
    d = 0
    while d < 5:
        try:
            _a += 1
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


def _F(a, b):
    e = ""
    if os.path.exists(a) and True:
        with open(a, "r", -1, "utf-8") as fp:
            e = fp.read()
            c = json.loads(e)
        if "emote" in c:
            if "emote" not in b:
                b["emote"] = c["emote"]
            else:
                f = {json.dumps(item, sort_keys=True) for item in b["emote"]}
                for g in c["emote"]:
                    h = json.dumps(g, sort_keys=True)
                    if h not in f:
                        b["emote"].append(g)
                        f.add(h)
    if "emote" in b:
        sort_list_dict(b["emote"], "id", "text")
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if d == e:
        return
    open(a, "w", -1, "utf-8").write(d)


def _G(a, b):
    "csv"
    if os.path.isfile(a):
        with open(a, "r", 1048576, "utf-8") as fp:
            if (c := b + "\n") in (x := fp.readlines()) or b in x:
                return
    with open(a, "a", 1048576, "utf-8") as fp:
        fp.write(c)


def _K(a, item):
    del_keys(item, "suggest", [""])
    del_keys(item, "flags", _O, OPR.IN)
    del_keys(item, "activity", None, OPR.ANY)
    del_keys(item, "label", None)
    del_keys(item, "attr", 0)
    del_keys(item, "package_sub_title", "")
    del_keys(item, "ref_mid", 0)
    del_keys(item, "resource_type", 0)
    replace_str(item, "http://", "https://")
    replace_str(item, "https://i1.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "https://i2.hdslb.com", "https://i0.hdslb.com")
    replace_str(item, "fasle", "false")
    c = os.path.join(_D, f"{a}.json")
    _F(c, item)
    _G(os.path.join(_D, "ids.csv"), f"{a},{item['text']}")


def _L(j=False):
    a = _N()
    b = 1
    c: int = 7800 if not j else 1
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
            if g in a and not j:
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


def _M():
    a = 1
    if sys.argv[1].lower() in "main":
        _L()
        return
    elif sys.argv[1] in "uU":
        _L(True)
        return
    with requests.Session() as b:
        while True:
            c = input("item_id:")
            time.sleep(a)
            d = _E(b, c, a)
            if d == _B:
                continue
            elif not c.isdigit():
                continue
            else:
                for e in json.loads(d)["data"]["packages"]:
                    _K(c, e)


def _N():
    a = []
    try:
        for b in glob.glob("*.json", root_dir=_D):
            c = b.split(".")[0]
            a.append(int(c))
        a.sort()
        return list(set(a))
    except Exception as e:
        log.exception(e)
        return a


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
    finally:
        log.error(f"📦 {_a}")
