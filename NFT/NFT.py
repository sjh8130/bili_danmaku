#!/usr/bin/python3
import json
import os
import ssl
import time

import brotli  # type: ignore[import-untyped]
import requests
from loguru import logger

log = logger.bind(user="NFT")
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
_HEADERS = {
    "Accept-Encoding": "gzip, deflate, bzip2, br, zstd",
    "Origin": "https://www.bilibili.com",
    "Referer": "https://www.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
}
_A: bytes = (
    b'{"code":12003003,"message":"\xe6\x9c\xaa\xe6\x89\xbe\xe5\x88\xb0\xe8\xaf\xa5\xe6\x94\xb6\xe8\x97\x8f\xe5\x93\x81","ttl":1,"data":null}'
)
_b: bytes = (
    b'\xb1Hn\x00aq`\xdb\x12\xca\xcf\xc4\xc1\xce\xdeE\xd8-\xd3\xc9C\x06\xe7\xd4\xdf\xa8\x8c T\xa2\xb11\xe7\xa4\x98B\xda\x11\t\xe1o\xcco\xff\xb6\x8d}u\x89S\xd0\xe1\x12\x11\xbc\x9e\x82\x88(@R\xc1\xb9|kL}\xaf^\xd5\xe8\xaa\n\xb7$\xff%\x92cPD\x1f(\xa1\x1a{vl75cg"\x9d\x03\x10\x15\xc9\xf5\x07Z|\xb0\x85\xce\x124F\x02\xc2\xf1\x19s\x0b\xa2\x95Z\r\xc1\xca\x07p#\x0f\xb1\xc9\x9b\xbc\x8ce$ar\xb8>\x96\xe7\xb7\x90>A\xfa\xa8\xcd\xe8\x9e.\xe20\xb2\x18lI\x065\x1di\xce2\xd5W\x8c\x90\x01\xd5+\xf60K\xc8.z%\x0b\xc8\x9fm_\xd6\xd3\xec\xa6\xe2\xbd\xe3SD\xa6\xe5\x9f\x9f\x1bCHM\x8b\xa5}S}\x95\xe3p\x9aRw+\xc8VM\n*\x10\x7fO\x97\xfa\xafu\x00\x02.J\xb1\x85\xf2\x1bB\x1bS\xe9\xc6\xcb\xa1\x0f\x89\x93\x9d:\x86\xcb\xf7\x97\x9dT\xa9\xa8"\xb4\xbaW\xf3\xf1\xb9\r\xb9\x88\xea\x16\x1f5=\x85.E\xe2\x84j\xa14\xd6\x8a5\xdf|\xe3P7\x8eNz\x13\xac\xeet\x89\xaa\xc6OP\xd1{\x80\x00\x02\xa0\xea\xf2\xf8\xf5\x1c\x9e\x19oh\x17\xceVBF\x9b\x8a\xa68E\x8b\xf1\xd4\xd7\xedL(\xde\xed\xaa}\xca\xbc h_\x17\x9dXx\xcfR\x8b5\xc9m\x98@\xd1Eb\x0c\xe0C\xffx\xaa\x1bwq\xc4\xd3\x90Yb\xa7\x01\x9dr6\xd3\xa1o2\xd33C|?;wg\xe1wO=]\xb1K\xcb;\xa3G\xfbv#\xb6\x99N\xf9\x87{Q\xd2\xab\xc0\xb6v\xfc\xa4\xbf \x8b\xbc\xa8\xae\x9c]An\xa2j\xa6\x9d\x19\xfar\x1a\xeb%^\x1f\xe9[{\xc1\xf7\xbbd\x14\x19r\x1e8V\x1e\xc2kW\xa6Gz\x1a\xd9\xf5\xda__\xa2JMrY\x14Qk\x14\x038D\x1b\xfb\xe8^adO\xe9k\xc1N\x92&\xc9M\x06`<m\t\x9bI\xbc\x92\xc7\xe0l+\x8b\xf6%\xff\xdb\x1e\t\x817`g$\xc5\xc2\xb6\x85#\xb1?\x9c2\x04i\xe2f\n\xdd\xbe}\xe9v\x00f\\\xd7\x806~\xfa!\xf9\xb43\x88\xfa\xf8\xa5\x80i\xd5\xcb\xe1\x83\xa9}S\xe1\x10\xe8\xf2\x8f\x18Q\xbc\x16\x81\n\xba\x97\xa3(\x90~L\xa1\xabtz\xc9t\xb5O\x9f\x07\xf0\xaa\xd3\x16\xd3\xd4\xbe\xae\x93\xa6\xddK\x10\x86\x02\x84\xb8\x8c\xf745\x7f\xe7\xc9\x1e\xef\xe38\xc2e\x9db\xcd\xe0T\x14\x8e\x89w\x88\xa2\xd6D\xb5\t\xa2\x8c<\x82s!\x8b\xb8d\x8b\x8aL\x01$G4OQd"\x05\x0b$q\x0cA:\xf1\x1e\x83AKs\xa5<\xec\xdc<\xf7\xc0J\xf0\\"4\xc9\xe8-#\xad\xf1\x87\x185\xd9l\x15\xba\xc6J~\xce\x895\\\x11\x9bF\x04\x12\xb2\xf0\\O\xe1v\x88c]\x92\xc5\x12\xc4\xe3\x82\xff\xc3\x89\xc9\r\xc3$\x942\xcd0\xa8n\xaaJh\x12\x9ah\x9c\xd3\x88\x98\x89i\xab\x89\x15\xd1(\x01\xa4\x82\x0c\x06"\xb4\n\x1eF\xdb\n \x9dM\xb2$%\xf9.\x88\xfe\x80\xa9@\xabU\xc8\x0f2IC6\x08\xe2\xe8\x96\x18|FwB\xe3\xf4\xd1#\xbfq@n\x0f3\x11.\xa9\xd5s\xf4t\xc5\xe7?\xad\x17M\x1c\x15\x93)\xb3d3\x85\x1fy\xc3@\x81s\xe6u,\xf0\xbb\xb88T\xac\xf1Z\x97\xbf\x08\x8d\xfe\xd8\xec#\xe4e)U\xde\xb5K9\xc4_\xf5\xe8h5\xac\xff\x7f\xfc\xac\xc3\x89\xe3\xb3<\x02\xc9\x84\xdb\xcf\xfe\xe4\x0f\x07\xdc^q\xa5-A\x1aX\xcbg\xe38\x9a\xb8\xc6[\xf5\xa4\x9c\xa8\xbb3\x91;\xce\x91\xe4\x9a#\x82\xec?\xc0o@?\x83q]%\x00'
)

_b = brotli.decompress(_b)
_C: bytes = b'{"code":12006047,"message":"12006047","ttl":1,"data":null}'


def _downloader(pn: int | str, item_id: int | str, ps: int | str) -> bytes:
    retries = 0
    while retries < 3:
        try:
            time.sleep(2)
            response = session.get(
                f"https://baselabs.bilibili.com/x/gallery/nft/collect/list?ps={ps}&pn={pn}&item_id={item_id}",
                headers=_HEADERS,
                verify=False,
                timeout=20,
            )
            if isinstance(response.content, bytes):
                print(
                    f"{item_id=:<8}{pn=:<4}{len(response.content):<8}{retries=:<4}",
                    end=" ",
                )
                if response.content != _b:
                    return response.content
        except requests.exceptions.Timeout:
            retries += 1
        if retries == 3:
            # raise Exception("请求超时次数达到上限")
            ...
        retries += 1
    return _A


def _get_data(item_id: int | str, base_path: str) -> int:
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
            with open(base_path + f"\\NFT_{item_id}.json", "a") as fp:
                fp.write(w_d + "\n")
    with open(base_path + "\\..\\" + "NFT_ID.tsv", "a", 4096, "utf-8") as f:
        f.write(f"{item_id}\t{issuer_name}\t{item_name}\n")
    return 200


def _main(base_path: str):
    for item_id in range(2500, 10000):
        if os.path.exists(base_path + f"\\NFT_{item_id}.json"):
            continue
        _get_data(item_id, base_path)


if __name__ == "__main__":
    session = requests.Session()
    base_path = os.path.abspath(
    )
    try:
        _main(base_path)
    except KeyboardInterrupt:
        print()
    except Exception as e:
        log.exception(e)
    session.close()
