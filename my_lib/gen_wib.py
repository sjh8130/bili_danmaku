import json
import ssl
import time
import urllib.parse
from functools import reduce
from hashlib import md5

import requests

ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with open("config.json", encoding="utf-8") as fp:
    config = json.load(fp)
del fp

MIXIN_KEY_ENC_TAB = [
    46,
    47,
    18,
    2,
    53,
    8,
    23,
    32,
    15,
    50,
    10,
    31,
    58,
    3,
    45,
    35,
    27,
    43,
    5,
    49,
    33,
    9,
    42,
    19,
    29,
    28,
    14,
    39,
    12,
    38,
    41,
    13,
    37,
    48,
    7,
    16,
    24,
    55,
    40,
    61,
    26,
    17,
    0,
    1,
    60,
    51,
    30,
    4,
    22,
    25,
    54,
    21,
    56,
    59,
    6,
    63,
    57,
    62,
    11,
    36,
    20,
    34,
    44,
    52,
]


def get_wbi_keys() -> tuple[str, str]:
    headers = {"User-Agent": config["ua"]}
    resp = requests.get("https://api.bilibili.com/x/web-interface/nav", headers=headers, verify=False)  # noqa: S113, S501
    resp.raise_for_status()
    data = resp.json()
    img_url: str = data["data"]["wbi_img"]["img_url"]
    sub_url: str = data["data"]["wbi_img"]["sub_url"]
    img_key = img_url.rsplit("/", 1)[1].split(".")[0]
    sub_key = sub_url.rsplit("/", 1)[1].split(".")[0]
    return img_key, sub_key


def get_mixin_key(orig: str) -> str:
    return reduce(lambda s, i: s + orig[i], MIXIN_KEY_ENC_TAB, "")[:32]


def wbi_sign(params: dict, img_key: str, sub_key: str) -> dict:
    params["wts"] = int(time.time())
    mixin_key = get_mixin_key(img_key + sub_key)
    # 过滤 value 中的 "!'()*" 字符
    params = {k: "".join(filter(lambda chr_: chr_ not in "!'()*", str(v))) for k, v in params.items()}
    params = dict(sorted(params.items()))  # 按照 key 重排参数
    query = urllib.parse.urlencode(params)  # 序列化参数
    w_rid = md5((query + mixin_key).encode()).hexdigest()  # noqa: S324
    params["w_rid"] = w_rid
    return params


def gen_w_rid(query: dict[str, str]) -> str:
    img_key, sub_key = get_wbi_keys()
    signed_params = wbi_sign(params=query, img_key=img_key, sub_key=sub_key)
    ret = urllib.parse.urlencode(signed_params)
    if __name__ == "__main__":
        print(signed_params)
        print(ret)
    return ret


if __name__ == "__main__":
    gen_w_rid({"foo": "114", "bar": "514", "baz": 1919810})  # pyright: ignore[reportArgumentType]
