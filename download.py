#!/usr/bin/python3
import contextlib
import dataclasses
import json
import math
import ssl
import sys
import time

import requests
from google.protobuf.json_format import MessageToDict

import dm_pb2
from my_lib.bvav import av2bv, bv2av
from my_lib.file_writer import write_file
from my_lib.gen_wib import gen_w_rid

ssl._create_default_https_context = ssl._create_unverified_context  # noqa: S323, SLF001
requests.packages.urllib3.disable_warnings()  # pyright: ignore[reportAttributeAccessIssue]
MAX_RETRIES = 2
RETRY_SIZE = 2048
SLEEP_TIME = 1.0
with open("config.json", encoding="utf-8") as fp:
    config = json.load(fp)
del fp
UA: str = config["ua"]
AE = config["ae"]


@dataclasses.dataclass
class _Video:
    def __init__(self, avid: str, bvid: str, avid_n: int) -> None:
        self.avid = avid
        self.bvid = bvid
        self.avid_n = avid_n


@dataclasses.dataclass
class _VideoPart(_Video):
    def __init__(self, V: _Video, cid: int, oid: int) -> None:
        super().__init__(V.avid, V.bvid, V.avid_n)
        self.cid = cid if cid is not None else oid
        if oid is not None and cid is not None and cid != oid:
            raise ValueError("CID and OID must be the same or one must be None.")


def _downloader(url: str, headers: dict[str, str], session: requests.Session, *, _json: bool = False) -> bytes:
    url = url.replace("http://", "https://")
    for _ in range(MAX_RETRIES):
        time.sleep(SLEEP_TIME)
        try:
            response = session.get(url, headers=headers, verify=False, timeout=10)
            if _json:
                return response.json()
            return response.content
        except requests.RequestException as e:
            print(f"下载错误: {e}")
    raise Exception("下载失败")


def _get_danmaku(vp: _VideoPart, duration: float, session: requests.Session) -> list[bytes]:
    seg = math.ceil(duration / 360) + 1
    danmakus: list[bytes] = []
    HEADERS = {
        "Accept-Encoding": AE,
        "Accept": "application/json, text/plain, */*",
        "Connection": "keep-alive",
        # "Cookie" : "",
        "Host": "api.bilibili.com",
        "Origin": "https://www.bilibili.com",
        "Referer": f"https://www.bilibili.com/video/{vp.bvid}/",
        "User-Agent": UA,
    }
    for segment in range(seg):
        filename = f"[{vp.bvid}]_[{vp.cid}]_[Danmaku]_[{segment}].bin"
        if segment == 0:
            # "?type=1&oid=XXX&pid=XXX&segment_index=1&pull_mode=1&ps=0&pe=120000&web_location=1315873&w_rid=XXX&wts=XXX"
            PARAMS = {
                "type": "1",
                "oid": str(vp.cid),
                "pid": str(vp.avid_n),
                "segment_index": "1",
                "pull_mode": "1",
                "ps": "0",
                "pe": "120000",
                "web_location": "1315873",
            }
        elif segment == 1:
            # "?type=1&oid=XXX&pid=XXX&segment_index=1&pull_mode=1&ps=120000&pe=360000&web_location=1315873&w_rid=XXX&wts=XXX"
            PARAMS = {
                "type": "1",
                "oid": str(vp.cid),
                "pid": str(vp.avid_n),
                "segment_index": "1",
                "pull_mode": "1",
                "ps": "120000",
                "pe": "360000",
                "web_location": "1315873",
            }
        else:
            # "?type=1&oid=XXX&pid=XXX&segment_index=3&web_location=1315873&w_rid=XXX&wts=XXX"
            PARAMS = {
                "type": "1",
                "oid": str(vp.cid),
                "pid": str(vp.avid_n),
                "segment_index": str(segment),
                "web_location": "1315873",
            }
        url = "https://api.bilibili.com/x/v2/dm/wbi/web/seg.so?" + gen_w_rid(PARAMS)
        file_content = _downloader(url, HEADERS, session)
        danmakus.append(bytes(file_content))
        write_file(filename, file_content)
    return danmakus


def _get_special_danmaku(vp: _VideoPart, spdm: dm_pb2.DmWebViewReply, session: requests.Session) -> list[bytes]:
    HEADERS = {
        "Accept-Encoding": AE,
        "Origin": "https://www.bilibili.com",
        "Referer": f"https://www.bilibili.com/{vp.bvid}",
        "User-Agent": UA,
        "Connection": "keep-alive",
    }
    bas_danmakus = []
    for url in spdm.special_dms:
        bas_data = _downloader(url, HEADERS, session)
        filename = f"[{vp.bvid}]_[{vp.cid}]_[BAS]_[{url[27:67]}].bin"
        bas_danmakus.append(bas_data)
        write_file(filename, bas_data)
    return bas_danmakus


def _main(video: _Video) -> None:
    if video is None:
        return
    session = requests.Session()
    headers = {
        "Accept-Encoding": AE,
        "Origin": "https://www.bilibili.com",
        "Referer": f"https://www.bilibili.com/{video.bvid}",
        "User-Agent": UA,
        "Connection": "keep-alive",
    }
    # video_info_0 = _get_json(video, session)
    # ================================ 视频信息1
    video_info_1: dict = _downloader(f"https://api.bilibili.com/x/web-interface/view?bvid={video.bvid}", headers, session, _json=True)
    with contextlib.suppress(KeyError):
        video_info_1["data"]["ugc_season"]["sections"] = []
    write_file(f"[{video.bvid}]_[0]_[Video]_[INFO].json", video_info_1)
    # ================================ 视频信息2
    video_info_2: dict = _downloader(f"https://api.bilibili.com/x/web-interface/view/detail?bvid={video.bvid}", headers, session, _json=True)
    video_info_2["data"]["Related"] = []
    video_info_2["data"]["Reply"]["replies"] = []
    with contextlib.suppress(KeyError):
        video_info_2["data"]["View"]["ugc_season"]["sections"] = []
    write_file(f"[{video.bvid}]_[0]_[Video]_[INFO_2].json", video_info_2)
    # ================================ 视频信息3
    video_info_3: dict = _downloader("https://api.bilibili.com/x/web-interface/wbi/view?" + gen_w_rid({"aid": video.avid_n}), headers, session, _json=True)
    write_file(f"[{video.bvid}]_[0]_[Video]_[INFO_3].json", video_info_3)
    # ================================ 加载
    json_info: dict = video_info_1["data"]
    # ================================ bvid aid 检查
    if json_info["bvid"] != video.bvid:
        print(f"[bvid]: bvid mismatch {json_info['bvid']}|{video.bvid}")
    if json_info["aid"] != video.bvid:
        print(f"[avid]: avid mismatch av{json_info['aid']}|{video.bvid}")
    # ================================ 字幕
    if json_info["subtitle"] is not None:
        for subs in json_info["subtitle"]["list"]:
            data = _downloader(subs["subtitle_url"], headers, session)
            write_file(f"[{video.bvid}]_[Subtitle]_[{subs['id']}]_[{subs['lan']}].bcc", data)
            del data
    # ================================ 首映
    if json_info.get("premiere") is not None:
        print(f"[{video.bvid}]: 首映 premiere")
    # ================================ 分集处理
    for _part, this in enumerate(json_info["pages"]):
        oid = int(this["cid"])
        vp = _VideoPart(V=video, cid=oid, oid=oid)
        v_url = f"https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={vp.cid}&pid={vp.avid_n}&duration={this['duration']}"
        extra_info_proto_binary = _downloader(v_url, headers, session)
        write_file(f"[{video.bvid}]_[{vp.cid}]_[BAS]_[INFO].bin", extra_info_proto_binary)
        extra_info_proto = dm_pb2.DmWebViewReply()
        extra_info_proto.ParseFromString(extra_info_proto_binary)
        # extra_info_json = MessageToDict(extra_info_proto)
        danmaku_binary_list = _get_danmaku(vp, this["duration"], session)
        danmaku_list = []
        danmakuColorful_list = []
        for dm_bin in danmaku_binary_list:
            dms = dm_pb2.DmSegMobileReply()
            dms.ParseFromString(dm_bin)
            dms_j = MessageToDict(dms)
            for dm in dms_j["elems"]:
                danmaku_list.append(dm)
            for dmc in dms_j["colorfulSrc"]:
                danmakuColorful_list.append(dmc)
        final_json = {"elems": danmaku_list, "colorfulSrc": danmakuColorful_list}
        final_string = json.dumps(final_json, ensure_ascii=False, separators=(",", ":")).replace('{"id":', '\n\t{"id":')
        write_file(f"[{video.bvid}]_[{video.avid}].json", final_string)


def _process_args(vid: str) -> _Video:
    vid = vid.replace("http://", "https://")
    if vid.startswith("https://www.bilibili.com/video/"):
        vid = vid.removeprefix("https://www.bilibili.com/video/")
    elif vid.startswith(("https://b23.tv/BV1", "https://b23.tv/av")):
        vid = vid.removeprefix("https://b23.tv/")
    vid = vid.split("?")[0].split("/")[0]
    if vid.startswith("BV"):
        bvid = vid[0:12]
        avid_n = bv2av(bvid)
        avid = f"av{avid_n}"
    elif vid.startswith("av"):
        avid_n = int(vid.removeprefix("av"))
        avid = f"av{avid_n}"
        bvid = av2bv(avid_n)
    else:
        raise Exception(vid)
    return _Video(avid, bvid, avid_n)


if __name__ == "__main__":
    for i in sys.argv[1:]:
        _main(_process_args(i))
