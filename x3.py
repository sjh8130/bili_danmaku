#!/usr/bin/python3
import json
import ssl
import sys
import time
from pathlib import Path
from typing import TypedDict

import requests
from loguru import logger
from tqdm import tqdm

from my_lib.xx_util import OPR, del_keys, replace_str, sort_list_dict

log = logger.bind(user="X3")
ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
config = json.loads(Path("config.json").read_text(encoding="utf-8"))
_A = {
    "User-Agent": config["ua"],
    "Connection": "keep-alive",
    "Accept-Encoding": config["ae"],
}
_B = b'{"code":0,"message":"0","ttl":1,"data":{"packages":null}}'
_C: str = config["x3"]["url"]
_D: Path = Path(config["x3"]["bp"]).resolve()
_O = [{}, {"no_access": True, "unlocked": False}, {"no_access": True}]
_a = 0


class EmoteMeta(TypedDict):
    size: int
    item_id: int
    alias: str
    label_text: str
    label_color: str


class Emote(TypedDict):
    id: int
    package_id: int
    text: str
    url: str
    gif_url: str
    webp_url: str
    mtime: int
    type: int
    meta: EmoteMeta


class EmoteMain(TypedDict):
    id: int
    text: str
    url: str
    mtime: int
    type: int
    meta: EmoteMeta
    emote: list[Emote]


def _E(a: requests.Session, b: int | str, c: int) -> bytes:
    global _a  # noqa: PLW0603
    d = 0
    while d < 5:
        try:
            _a += 1
            e = a.get(_C.format(q=b), headers=_A, verify=False, timeout=20)
            e.raise_for_status()
            return e.content
        except requests.RequestException as e:
            d += 1
            print(" ")
            log.exception(e)
            time.sleep(c + d)
        except KeyboardInterrupt:
            raise KeyboardInterrupt  # noqa: B904
    raise Exception(f"Failed to fetch {b}")


def _F(a: Path, b: EmoteMain) -> None:
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    e = ""
    if a.is_file():
        e = a.read_text(encoding="utf-8")
        if d == e:
            return
        if "emote" in (c := json.loads(e)):
            if "emote" not in b:
                b["emote"] = c["emote"]
            else:
                for g in c["emote"]:
                    if (h := json.dumps(g, ensure_ascii=False, sort_keys=True)) not in (f := {json.dumps(item, ensure_ascii=False, sort_keys=True) for item in b["emote"]}):
                        b["emote"].append(g)
                        f.add(h)
    if "emote" in b:
        sort_list_dict(b["emote"], "id", "text")
    d = json.dumps(b, ensure_ascii=False, separators=(",", ":"), indent="\t")
    if d == e:
        return
    a.write_text(d, encoding="utf-8")


def _G(a: Path, b: str) -> None:
    """csv"""
    if a.is_file() and b in a.read_text(encoding="utf-8"):
        return
    with a.open("a", 1048576, "utf-8") as fp:
        fp.write(b)


def _K(a: int | str, item: dict) -> None:
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
    # replace_str(item, "fasle", "false")
    _F(_D / f"{a}.json", item)  # type: ignore
    _G(_D / "ids.csv", f"{a},{item['text']}\n")


def _L(*, j: bool = False) -> None:
    a = _N()
    b = 1
    c: int = 8400 if not j else 1
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
            for i in json.loads(h)["data"]["packages"]:
                _K(g, i)
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()):<32}{g:<12}{i['text']:20}")


def _M() -> None:
    a = 1
    if sys.argv[1].lower() in {"main", "0"}:
        _L()
        return
    if sys.argv[1] in "uU":
        _L(j=True)
        return
    with requests.Session() as b:
        while True:
            c: str = input("item_id:")
            time.sleep(a)
            d = _E(b, c, a)
            if d == _B or not c.isdigit():
                continue
            for e in json.loads(d)["data"]["packages"]:
                _K(c, e)


def _N() -> list[int]:
    a = []
    try:
        for b in _D.rglob("*.json"):
            a.append(int(b.stem))
        a.sort()
        return list(set(a))
    except Exception as e:
        log.exception(e)
        return a


if __name__ == "__main__":
    try:
        if (len(sys.argv)) > 1:
            _M()
        else:
            _L()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        log.exception(e)
    finally:
        log.error(f"📦 {_a}")
