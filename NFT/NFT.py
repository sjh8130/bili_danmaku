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


def _downloader(pn: int | str, item_id: int | str, ps: int | str) -> bytes:
    retries = 0
    item_id = str(item_id)
    while retries < 3:
        try:
            time.sleep(2)
            response = session.get(
                URL.format(ps=ps, pn=pn, item_id=item_id),
                headers=_HEADERS,
                verify=False,
                timeout=20,
            )
            if isinstance(response.content, bytes):
                print(
                    f"\r{item_id=:<8}{pn=:<4}{len(response.content):<8}{retries=:<4}",
                    end=" ",
                )
                if response.content != _B:
                    return response.content
        except requests.exceptions.Timeout:
            retries += 1
        if retries == 3:
            # raise Exception("请求超时次数达到上限")
            ...
        retries += 1
    return _A


def _get_data(item_id: int | str) -> int:
    item_id = str(item_id)
    pn = 1
    ps = 100
    run = True
    issuer_name: str = ""
    item_name: str = ""
    while run:
        data = _downloader(pn, item_id, ps)
        if data == _A:
            print(f"[NFT]{item_id}:未找到该收藏品", end="\r")
            if pn == 1:
                return 404
            else:
                run = False
        elif data == b"":
            print(f"[NFT]{item_id}_{pn}:403 服务器正在休息")
            continue
        elif data == _C:
            print(f"[NFT]{item_id}_{pn}:未知错误")
            return 500
        else:
            pn += 1
            response_d: dict = json.loads(data.decode("utf-8"))["data"]
            item_name = str(response_d.get("item_name", ""))
            issuer_name = str(response_d.get("issuer_name", ""))
            print(item_name)
            w_d = json.dumps(response_d, ensure_ascii=False)
            with open(_BP + f"\\NFT_{item_id}.json", "a", 8192, "utf-8") as fp:
                fp.write(w_d + "\n")
    with open(_BP + "\\..\\" + "NFT_ID.tsv", "a", 4096, "utf-8") as f:
        f.write(f"{item_id}\t{issuer_name}\t{item_name}\n")
    return 200


def _main():
    for item_id in range(1, 3000):
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
    session.close()
