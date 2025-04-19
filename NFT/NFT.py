#!/usr/bin/python3
import base64
import binascii
import json
import os
import ssl
import time

import requests
from loguru import logger

log = logger.bind(user="NFT")
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with open("..\\config.json", "r", -1, "utf-8") as fp:
    config = json.load(fp)
del fp
URL: str = config["nft"]["url"]
_BP: str = config["nft"]["bp"]
_HEADERS = {
    "Accept-Encoding": config["ae"],
    "Origin": "https://www.bilibili.com",
    "Referer": "https://www.bilibili.com",
    "User-Agent": config["ua"],
}
_A: bytes = binascii.a2b_base64(config["nft"]["a"])
"not found"
_B: bytes = base64.b85decode(config["nft"]["b"])
"anti ddos"
_C: bytes = binascii.a2b_base64(config["nft"]["c"])
"?"
_a = 0


def _downloader(pn: int | str, item_id: int | str, ps: int | str) -> bytes:
    global _a
    retries = 0
    item_id = str(item_id)
    while retries < 3:
        try:
            time.sleep(2)
            x: requests.Response = session.get(
                URL.format(ps=ps, pn=pn, item_id=item_id),
                headers=_HEADERS,
                verify=False,
                timeout=20,
            )
            _a += 1
            if isinstance(x.content, bytes):
                if x.content != _B:
                    return x.content
        except requests.exceptions.Timeout:
            retries += 1
        if retries == 3:
            # raise Exception("请求超时次数达到上限")
            ...
        retries += 1
    return _A


def _clean_it(ld: list[dict]):
    for d in ld:
        if True:
            d.pop("item_name")
        if True:
            d.pop("token_id")
        if True:
            d.pop("avatar")
        if True:
            d.pop("detail_jump")
        if True:
            d.pop("mid")
        if True:
            d.pop("username")
        if True:
            d.pop("like_number")
        if True:
            d.pop("like_status")
        if True:
            d.pop("is_show")


def _get_data(item_id: int | str) -> int:
    item_id = str(item_id)
    pn = 1
    ps = 100
    run = True
    issuer_name: str = ""
    item_name: str = ""
    d0 = {}
    while run:
        data = _downloader(pn, item_id, ps)
        if data == _A and pn > 1:
            log.info(f"{item_id}:Done")
            run = False
        elif data == _A:
            log.debug(f"{item_id}:未找到该收藏品")
            return 404
        elif data == b"":
            log.warning(f"{item_id}_{pn}:403 服务器正在休息")
            continue
        elif data == _C:
            log.warning(f"{item_id}_{pn}:未知错误")
            return 500
        else:
            response_d: dict = json.loads(data.decode("utf-8"))["data"]
            if pn == 1:
                d0 = response_d
                item_name = str(response_d.get("item_name", "")).strip()
                issuer_name = str(response_d.get("issuer_name", "")).strip()
            else:
                try:
                    d0["nft_list"] += response_d["nft_list"]
                except Exception:
                    pass
            log.info(f"{item_id=:<8}size={len(data):<8}{pn}/{float(response_d['total']/ps).__ceil__()}")
            pn += 1
    _clean_it(d0["nft_list"])
    d0.pop("private", "")
    with open(_BP + f"\\NFT_{item_id}.json", "a", 8192, "utf-8") as fp:
        json.dump(d0, fp, ensure_ascii=False, indent="\t", separators=(",", ":"))
    with open(_BP + "\\..\\" + "NFT_ID.tsv", "a", 4096, "utf-8") as f:
        f.write(f"{item_id}\t{issuer_name}\t{item_name}\n")
    return 200


def _main():
    for item_id in range(2000, 3000):
        if os.path.exists(_BP + f"\\NFT_{item_id}.json"):
            continue
        _get_data(item_id)


if __name__ == "__main__":
    session = requests.Session()
    try:
        _main()
    except KeyboardInterrupt:
        print()
    except Exception as e:
        log.exception(e)
    finally:
        log.error(f"📦 {_a}")
    session.close()
