#!/usr/bin/python3
import gzip
import ssl
import requests
import time
import json
import sys

import dm_pb2
from my_lib.bvav import BV2AV, AV2BV
from my_lib.gen_wib import gen_w_rid

from google.protobuf.json_format import MessageToJson

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
SLEEP_TIME = 0.5
RETRIES = 2
RETRY_SIZE = 2048


class Video:
	avid: int
	bvid: str

	def __init__(self, avid, bvid, avid_n):
		self.avid = avid
		self.bvid = bvid
		self.avid_n = avid_n


class VideoPart(Video):
	cid: int

	def __init__(self, V:Video, cid):
		super().__init__(V.avid,V.bvid, V.avid_n)
		self.cid = cid


def downloader(url: str, headers: dict, session: requests.Session) -> bytes:
	"""
	下载
	"""
	url = url.replace("http://", "https://")
	retry_count = 0
	while True:
		time.sleep(SLEEP_TIME)
		try:
			response = session.get(url, headers=headers, verify=False, timeout=10)
			return response.content
		except Exception as e:
			retry_count += 1
			if retry_count > RETRIES:
				raise e
			else:
				continue


def getDanmaku(vp: VideoPart, segments: int, session: requests.Session) -> list[bytes]:
	"""
	获取弹幕
	"""
	danmakus = []
	headers = {
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Accept" : "application/json, text/plain, */*",
		"Connection": "keep-alive",
		"Host" : "api.bilibili.com",
		"Origin" : "https://www.bilibili.com",
		"Referer" : f"https://www.bilibili.com/video/{vp.bvid}/",
		"User-Agent": USER_AGENT,
	}

	for segment in range(segments):
		filename = f"[{vp.bvid}]_[{vp.cid}]_[Danmaku]_[{segment}].bin"
		if segment == 0:
		#"?type=1&oid=XXX&pid=XXX&segment_index=1&pull_mode=1&ps=0&pe=120000&web_location=1315873&w_rid=XXX&wts=XXX"
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
		#"?type=1&oid=XXX&pid=XXX&segment_index=1&pull_mode=1&ps=120000&pe=360000&web_location=1315873&w_rid=XXX&wts=XXX"
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
		#"?type=1&oid=XXX&pid=XXX&segment_index=3&web_location=1315873&w_rid=XXX&wts=XXX"
		#"?type=1&oid=XXX&pid=XXX&segment_index=3&web_location=1315873&w_rid=XXX&wts=XXX"
			params = {
				"type": "1",
				"oid": str(vp.cid),
				"pid": str(vp.avid_n),
				"segment_index": str(segment),
				"web_location": "1315873",
			}
		url = "https://api.bilibili.com/x/v2/dm/wbi/web/seg.so?"+gen_w_rid(params)
		file_content = downloader(url, headers, session)
		danmakus.append(bytes(file_content))
		writeToFiles(filename, file_content)
	return danmakus


def getSpecialDanmaku(vp: VideoPart, input: dm_pb2.DmWebViewReply, session: requests.Session) -> list[bytes]:
	"""
	获取特殊弹幕
	"""
	headers = {
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Origin": "https://www.bilibili.com",
		"Referer": f"https://www.bilibili.com/{vp.bvid}",
		"User-Agent": USER_AGENT,
		"Connection": "keep-alive",
	}

	bas_danmakus = []
	for url in input.special_dms:
		bas_data = downloader(url, headers, session)
		filename = f"[{vp.bvid}]_[{vp.cid}]_[BAS]_[{url[27:67]}].bin"
		bas_danmakus.append(bas_data)
		writeToFiles(filename, bas_data)
	return bas_danmakus


def writeToFiles(filename: str, data: str | bytes | dict, _gzip: bool = False) -> None:
	"""
	输出文件
	"""
	_type = type(data)
	if _type == str:
		_data = bytes(data, encoding="utf-8")
	elif _type == dict:
		_data = bytes(json.dumps(data, ensure_ascii=False, separators=(",",":")), encoding="utf-8")
	else:
		_data = data
	if _gzip:
		gzip.open(filename, "wb", 9).write(_data)
	else:
		open(filename, "wb", 1048576).write(_data)


def main(video:Video):
	"""
	视频处理
	"""
	if video == None:
		return
	url_info_1n = f"https://api.bilibili.com/x/web-interface/view?bvid={video.bvid}"
	url_info_1e = "https://api.bilibili.com/x/web-interface/wbi/view?"+gen_w_rid({"aid":video.avid_n})
	url_info_2n = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={video.bvid}"
	session = requests.Session()
	headers = {
		"Accept-Encoding": "gzip, deflate, br, zstd",
		"Origin": "https://www.bilibili.com",
		"Referer": f"https://www.bilibili.com/{video.bvid}",
		"User-Agent": USER_AGENT,
		"Connection": "keep-alive",
	}
	# ================================ 视频信息1
	video_info_1 = downloader(url_info_1n, headers, session)
	video_info_1_load = json.loads(video_info_1)
	try:
		video_info_1_load["data"]["ugc_season"]["sections"] = []
	except:
		pass
	writeToFiles(f"[{video.bvid}]_[0]_[Video]_[INFO].json", video_info_1_load)
	# ================================ 视频信息2
	video_info_2 = downloader(url_info_2n, headers, session)
	video_info_2_load = json.loads(video_info_2)
	video_info_2_load["data"]["Related"] = []
	video_info_2_load["data"]["Reply"]["replies"] = []
	try:
		video_info_2_load["data"]["View"]["ugc_season"]["sections"] = []
	except:
		pass
	writeToFiles(f"[{video.bvid}]_[0]_[Video]_[INFO_2].json", video_info_2_load)
	# ================================ 视频信息3
	video_info_3 = downloader(url_info_1e, headers, session)
	video_info_3_load = json.loads(video_info_3)
	writeToFiles(f"[{video.bvid}]_[0]_[Video]_[INFO_3].json", video_info_3_load)
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
			writeToFiles(f"[{video.bvid}]_[Subtitle]_[{subs['id']}]_[{subs['lan']}].bcc", downloader(subs["subtitle_url"], headers, session))
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
		vp = VideoPart(V=video,cid=oid)

		segment_count = (int(this["duration"])/360).__ceil__()+1
		extra_info_proto_binary = downloader(f"https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={vp.cid}", headers, session)
		writeToFiles(f"[{video.bvid}]_[{vp.cid}]_[BAS]_[INFO].bin", extra_info_proto_binary)

		extra_info_proto = dm_pb2.DmWebViewReply()
		extra_info_proto.ParseFromString(extra_info_proto_binary)
		extra_info_json = json.loads(MessageToJson(extra_info_proto, indent=0))

		danmaku_binary_list = getDanmaku(vp, segment_count, session)
		danmaku_list = []
		danmakuColorful_list = []
		for dm_bin in danmaku_binary_list:
			dms = dm_pb2.DmSegMobileReply()
			dms.ParseFromString(dm_bin)
			dms_j = json.loads(MessageToJson(dms, indent=0))
			for dm in dms_j['elems']:
				danmaku_list.append(dm)
			for dmc in dms_j['colorfulSrc']:
				danmakuColorful_list.append(dmc)
		final_json = {
			"elems":danmaku_list,
			"colorfulSrc":danmakuColorful_list
		}
		with open(f"[{video.bvid}]_[{video.avid}].json","w",encoding="utf-8") as fp:
			final_string = json.dumps(final_json, ensure_ascii=False, separators=(",",":"))
			fp.write(final_string.replace("{\"id\":","\n\t{\"id\":"))


def process_args(vid: str):
	if vid.find("https://www.bilibili.com/video/") == 0:
		vid = vid.lstrip("https://www.bilibili.com/video/")
	elif vid.find("http://www.bilibili.com/video/") == 0:
		vid = vid.lstrip("http://www.bilibili.com/video/")
	elif vid.find("https://b23.tv/BV1") == 0 or vid.find("https://b23.tv/av") == 0:
		vid = vid.lstrip("https://b23.tv/")
	vid = vid.split("?")[0].split("/")[0]
	if vid.find("BV") == 0:
		bvid = vid[vid.find("BV"):vid.find("BV")+12]
		avid_n = BV2AV(bvid)
		avid = f"av{avid_n}"
	elif vid.find("av") == 0:
		avid_n = int(vid.lstrip("av"))
		avid = f"av{avid_n}"
		bvid = AV2BV(avid_n)
	else:
		raise Exception(msg=vid)
	return Video(avid, bvid, avid_n)


if __name__ == "__main__":
	for i in sys.argv[1:]:
		main(process_args(i))
