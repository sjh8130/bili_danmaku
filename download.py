#!/usr/bin/python3
import json
import re
import ssl
import sys
import time

from dataclasses import dataclass
from typing import Optional

import dm_pb2
from my_lib.bvav import BV2AV, AV2BV
from my_lib.gen_wib import gen_w_rid
from my_lib.file_writer import write_file

from google.protobuf.json_format import MessageToDict
import bs4
import requests

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

AE = "gzip, deflate, bzip2, br, zstd"
RETRIES = 2
RETRY_SIZE = 2048
SLEEP_TIME = 0.5
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"


@dataclass
class _Video:
    def __init__(self, avid: int, bvid: str, avid_n: str):
        self.avid = avid
        self.bvid = bvid
        self.avid_n = avid_n


@dataclass
class _VideoPart(_Video):
    def __init__(self, V: _Video, cid: int, oid: Optional[int]):
        super().__init__(V.avid, V.bvid, V.avid_n)
        self.cid = cid if cid is not None else oid
        if oid is not None and cid is not None and cid != oid:
            raise ValueError("CID and OID must be the same or one must be None.")


def _downloader(url: str, headers: dict, session: requests.Session) -> bytes:
    url = url.replace("http://", "https://")
    for _ in range(RETRIES):
        time.sleep(SLEEP_TIME)
        try:
            response = session.get(url, headers=headers, verify=False, timeout=10)
            return response.content
        except requests.RequestException as e:
            print(f"下载错误: {e}")
    def to_dict():
        return json.loads(response)
    raise Exception("下载失败")


def _get_danmaku(vp: _VideoPart, segments: int, session: requests.Session) -> list[bytes]:
    """
    获取弹幕
    """
    danmakus = []
    headers = {
        "Accept-Encoding": AE,
        "Accept": "application/json, text/plain, */*",
        "Connection": "keep-alive",
        # "Cookie" : "",
        "Host": "api.bilibili.com",
        "Origin": "https://www.bilibili.com",
        "Referer": f"https://www.bilibili.com/video/{vp.bvid}/",
        "User-Agent": UA,
    }

    for segment in range(segments):
        filename = f"[{vp.bvid}]_[{vp.cid}]_[Danmaku]_[{segment}].bin"
        if segment == 0:
            # "?type=1&oid=XXX&pid=XXX&segment_index=1&pull_mode=1&ps=0&pe=120000&web_location=1315873&w_rid=XXX&wts=XXX"
            params = {
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
            params = {
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
            # "?type=1&oid=XXX&pid=XXX&segment_index=3&web_location=1315873&w_rid=XXX&wts=XXX"
            params = {
                "type": "1",
                "oid": str(vp.cid),
                "pid": str(vp.avid_n),
                "segment_index": str(segment),
                "web_location": "1315873",
            }
        url = "https://api.bilibili.com/x/v2/dm/wbi/web/seg.so?" + gen_w_rid(params)
        file_content = _downloader(url, headers, session)
        danmakus.append(bytes(file_content))
        write_file(filename, file_content)
    return danmakus


def _get_special_danmaku(vp: _VideoPart, input: dm_pb2.DmWebViewReply, session: requests.Session) -> list[bytes]:
    """
    获取特殊弹幕
    """
    headers = {
        "Accept-Encoding": AE,
        "Origin": "https://www.bilibili.com",
        "Referer": f"https://www.bilibili.com/{vp.bvid}",
        "User-Agent": UA,
        "Connection": "keep-alive",
    }

    bas_danmakus = []
    for url in input.special_dms:
        bas_data = _downloader(url, headers, session)
        filename = f"[{vp.bvid}]_[{vp.cid}]_[BAS]_[{url[27:67]}].bin"
        bas_danmakus.append(bas_data)
        write_file(filename, bas_data)
    return bas_danmakus


def _get_json(v: _Video, session: requests.Session):
    headers = {
        "Accept-Encoding": AE,
        "Origin": "https://www.bilibili.com",
        "Referer": f"https://www.bilibili.com/{v.bvid}",
        "User-Agent": UA,
        "Connection": "keep-alive",
    }

    html: str = session.get(f"", headers=headers)
    soup = bs4.BeautifulSoup(html, "lxml")

    json_dict: dict = None
    for script in soup.find_all("script"):
        if "window.__INITIAL_STATE__=" in str(script):
            json_line = re.findall(r"window.__INITIAL_STATE__=(.*);", script.string)[0]
            json_dict = json.loads(json_line)
            break
    return json_dict


def _main(video: _Video):
    if video == None:
        return
    url_info_1n = f"https://api.bilibili.com/x/web-interface/view?bvid={video.bvid}"
    url_info_1e = "https://api.bilibili.com/x/web-interface/wbi/view?" + gen_w_rid({"aid": video.avid_n})
    url_info_2n = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={video.bvid}"
    session = requests.Session()
    headers = {
        "Accept-Encoding": AE,
        "Origin": "https://www.bilibili.com",
        "Referer": f"https://www.bilibili.com/{video.bvid}",
        "User-Agent": UA,
        "Connection": "keep-alive",
    }
    video_info_0 = _get_json(video)
    # ================================ 视频信息1
    video_info_1 = _downloader(url_info_1n, headers, session)
    video_info_1_load = json.loads(video_info_1)
    try:
        video_info_1_load["data"]["ugc_season"]["sections"] = []
    except:
        pass
    write_file(f"[{video.bvid}]_[0]_[Video]_[INFO].json", video_info_1_load)
    # ================================ 视频信息2
    video_info_2 = _downloader(url_info_2n, headers, session)
    video_info_2_load = json.loads(video_info_2)
    video_info_2_load["data"]["Related"] = []
    video_info_2_load["data"]["Reply"]["replies"] = []
    try:
        video_info_2_load["data"]["View"]["ugc_season"]["sections"] = []
    except:
        pass
    write_file(f"[{video.bvid}]_[0]_[Video]_[INFO_2].json", video_info_2_load)
    # ================================ 视频信息3
    video_info_3 = _downloader(url_info_1e, headers, session)
    video_info_3_load = json.loads(video_info_3)
    write_file(f"[{video.bvid}]_[0]_[Video]_[INFO_3].json", video_info_3_load)
    # ================================ 加载
    json_info = video_info_1_load["data"]
    # ================================ bvid aid 检查
    if json_info["bvid"] != video.bvid:
        print(f"[bvid]: bvid mismatch {json_info['bvid']}|{video.bvid}")
    if json_info["aid"] != video.bvid:
        print(f"[avid]: avid mismatch av{json_info['aid']}|{video.bvid}")
    # ================================ 字幕
    if json_info["subtitle"] != None:
        for subs in json_info["subtitle"]["list"]:
            _data = _downloader(subs["subtitle_url"], headers, session)
            write_file(f"[{video.bvid}]_[Subtitle]_[{subs['id']}]_[{subs['lan']}].bcc", _data)
            del _data
    # ================================ 首映
    try:
        if json_info["premiere"] is not None:
            print(f"[{video.bvid}]: 首映 premiere")
    except:
        pass
    # ================================ 分集处理
    part = 0
    for this in json_info["pages"]:
        part += 1
        oid = int(this["cid"])
        vp = _VideoPart(V=video, cid=oid)

        segment_count = (int(this["duration"]) / 360).__ceil__() + 1
        v_url = f"https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={vp.cid}&pid={vp.avid}&duration={this['']}"
        extra_info_proto_binary = _downloader(v_url, headers, session)
        write_file(f"[{video.bvid}]_[{vp.cid}]_[BAS]_[INFO].bin", extra_info_proto_binary)

        extra_info_proto = dm_pb2.DmWebViewReply()
        extra_info_proto.ParseFromString(extra_info_proto_binary)
        extra_info_json = MessageToDict(extra_info_proto)

        danmaku_binary_list = _get_danmaku(vp, segment_count, session)
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


def _process_args(vid: str):
    if vid.find("https://www.bilibili.com/video/") == 0:
        vid = vid.lstrip("https://www.bilibili.com/video/")
    elif vid.find("http://www.bilibili.com/video/") == 0:
        vid = vid.lstrip("http://www.bilibili.com/video/")
    elif vid.find("https://b23.tv/BV1") == 0 or vid.find("https://b23.tv/av") == 0:
        vid = vid.lstrip("https://b23.tv/")
    vid = vid.split("?")[0].split("/")[0]
    if vid.find("BV") == 0:
        bvid = vid[vid.find("BV") : vid.find("BV") + 12]
        avid_n = BV2AV(bvid)
        avid = f"av{avid_n}"
    elif vid.find("av") == 0:
        avid_n = int(vid.lstrip("av"))
        avid = f"av{avid_n}"
        bvid = AV2BV(avid_n)
    else:
        raise Exception(vid)
    return _Video(avid, bvid, avid_n)


if __name__ == "__main__":
    for i in sys.argv[1:]:
        _main(_process_args(i))
