import json
import ssl
import time
import urllib.parse
from functools import lru_cache, reduce
from hashlib import md5

import requests

ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # type: ignore[attr-defined]
with open("config.json", encoding="utf-8") as fp:
    config = json.load(fp)
del fp

_mixin_key_enc_tab = [
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


def getMixinKey(orig: str) -> str:
    """对 imgKey 和 subKey 进行字符顺序打乱编码."""
    return reduce(lambda s, i: s + orig[i], _mixin_key_enc_tab, "")[:32]


def encWbi(params: dict[str, str], img_key: str, sub_key: str) -> dict[str, str]:
    """为请求参数进行 wbi 签名."""
    mixin_key = getMixinKey(img_key + sub_key)
    # print("[mixin_key]",  mixin_key)
    curr_time = round(time.time())
    params["wts"] = curr_time  # 添加 wts 字段
    params = dict(sorted(params.items()))  # 按照 key 重排参数
    # 过滤 value 中的 "!'()*" 字符
    params = {k: "".join(filter(lambda chr_: chr_ not in "!'()*", str(v))) for k, v in params.items()}
    query = urllib.parse.urlencode(params)  # 序列化参数
    wbi_sign = md5((query + mixin_key).encode()).hexdigest()  # 计算 w_rid  # noqa: S324
    params["w_rid"] = wbi_sign
    return params


@lru_cache
def getWbiKeys() -> tuple[str, str]:
    """获取最新的 img_key 和 sub_key."""
    headers = {"User-Agent": config["ua"]}
    resp = requests.get("https://api.bilibili.com/x/web-interface/nav", headers=headers, verify=False)  # noqa: S113, S501
    resp.raise_for_status()
    json_content = resp.json()
    img_url: str = json_content["data"]["wbi_img"]["img_url"]
    sub_url: str = json_content["data"]["wbi_img"]["sub_url"]
    img_key = img_url.rsplit("/", 1)[1].split(".")[0]
    sub_key = sub_url.rsplit("/", 1)[1].split(".")[0]
    return img_key, sub_key


def gen_w_rid(query: dict[str, str]) -> str:
    img_key, sub_key = getWbiKeys()
    signed_params = encWbi(params=query, img_key=img_key, sub_key=sub_key)
    ret = urllib.parse.urlencode(signed_params)
    if __name__ == "__main__":
        print(signed_params)
        print(ret)
    return ret


if __name__ == "__main__":
    gen_w_rid({"foo": "114", "bar": "514", "baz": 1919810})
