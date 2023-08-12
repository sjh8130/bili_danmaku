#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson
import ssl
import requests
from binascii import crc32
import time
import json
import sys
import logging

try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

# from my_lib.proto2xml_Lib import Proto2XML
from my_lib.bvav import BV2AV, AV2BV
from my_lib.file_writer import FileWriter
from my_lib.debug import SettingsDebug
from my_lib.gen_wib import gen_w_rid

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
# logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52"
headers = {
	'User-Agent': USER_AGENT,
	'origin': "https://www.bilibili.com",
	'referer': "https://www.bilibili.com",
	"Connection": "keep-alive"
}
SLEEP_TIME = 2
network_request_count = [0, 0]
err_sign = ""
settings = []
for _ in range(64): settings.append(False)
RETRIES = 2
RETRY_SIZE = 2048
session = requests.Session()


def Program_FLAG(flag: str) -> None:
	"""
	控制运行参数
	"""
	if flag == "-1": return
	if flag.find("0b") == 0: flag = "0"+flag
	else: flag = bin(int(flag))
	flag = "00000000000000000000000000000000" + flag.lstrip("0b")
	global settings
	for xx in range(-1, -len(flag), -1):
		if flag[xx] == "1": settings[-xx - 1] = True
		else: settings[-xx - 1] = False
	if settings[3]:
		# logging.Logger.setLevel(level=logging.DEBUG)
		logging.warning(f"Program_FLAG {flag}")


def Downloader(url_DL: str, filename: str, headers: dict = headers) -> bytes:
	"""
	下载
	"""
	logging.debug(f"[Downloader] {bvid}")
	global network_request_count
	network_request_count[0] += 1
	network_request_count[1] += 1
	url_DL = url_DL.replace("http://", "https://")
	status_code = [0, 0]
	if settings[8]:
		try:
			DL_Data = open(filename, "rb").read()
			status_code[0] = 200
		except FileNotFoundError:
			DL_Data = b""
			status_code[0] = 404
		try: status_code[1] = json.loads(DL_Data)["code"]
		except UnicodeDecodeError: status_code[1] = 0
		except KeyError: status_code[1] = 0
		except json.decoder.JSONDecodeError:
			if status_code[0] == 404: status_code[1] = 404
		if settings[3]:
			logging.debug(f"[NET]? File{status_code[0]}, Json{status_code[1]}")
		if status_code[1] != 0 or status_code[0] != 200:
			logging.error(f"[NET]? File{status_code[0]}, Json{status_code[1]}")
		logging.debug("[Downloader] " + filename)
		return DL_Data
	else:
		time.sleep(SLEEP_TIME)
		while True:
			try:
				DL_Data = session.request(method='GET', url=url_DL, headers=headers, verify=False, timeout=10)
			except TimeoutError:
				logging.warning("[Downloader] Timeout " + url_DL)
				continue
			except requests.exceptions.ReadTimeout:
				logging.warning("[Downloader] requests.exceptions.ReadTimeout " + url_DL)
				continue
			except requests.exceptions.ConnectionError:
				logging.warning("[Downloader] requests.exceptions.ConnectionError " + url_DL)
				continue
			else:
				break
		status_code[0] = DL_Data.status_code
		try:
			status_code[1] = json.loads(DL_Data.content)["code"]
			if status_code[1] != 0:
				settings[12] = True
		except UnicodeDecodeError: status_code[1] = 0
		except KeyError: status_code[1] = 0
		return DL_Data.content


def GetDanmaku(cid: str, segment_index: str, retries: str = "") -> bytes:
	"""
	获取弹幕
	"""
	logging.debug(f"{bvid}: [Danmaku] [{cid}] {segment_index} {retries}")
	temp_string = ""
	# if segment_index == "1":temp_string = "&pull_mode=1&ps=120000&pe=360000"
	# else:temp_string = ""

	headers = {
		'Host': "api.bilibili.com",
		"Connection": "keep-alive",
		'Accept': "application/json, text/plain, */*",
		'User-Agent': USER_AGENT,
		'origin': "https://www.bilibili.com",
		'referer': f"https://www.bilibili.com/video/{bvid}/",
		'Accept-Encoding': "gzip, deflate, br",
	}
	file_content = Downloader(f"https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&pid={avid_in}&segment_index={segment_index}{temp_string}", f"[{bvid}]_[{cid}]_[Danmaku]_[{segment_index+retries}].bin", headers=headers)
	if settings[12] and settings[1]: return b""
	DumpData(f"[{bvid}]_[{cid}]_[Danmaku]_[{segment_index+retries}].bin", file_content)
	return file_content


def GetSpecialDanmaku(input: dm_pb2.DmWebViewReply) -> bytes:
	"""
	获取特殊弹幕
	"""
	logging.debug(f"{bvid}: get_Special_Danmaku")
	bas_danmaku = b""
	ib = 1
	for URL_special_dms in input.special_dms:
		bas_data = Downloader(URL_special_dms, f"[{bvid}]_[{cid}]_[BAS]_[{URL_special_dms[27:67]}].bin")
		logging.debug(f"[BAS_DL]: Download {ib}")
		if settings[12] and settings[1]: break
		bas_danmaku += bas_data
		DumpData(f"[{bvid}]_[{cid}]_[BAS]_[{URL_special_dms[27:67]}].bin", bas_data)
		ib += 1
	return bas_danmaku


# def xmlDanmakuProcess(Proto_data) -> str:
# 	"""
# 	弹幕 --> XML
# 	"""
# 	logging.debug(f"{bvid}: XML_Process")
# 	this: dm_pb2.DanmakuElem
# 	out0 = ""
# 	for this in Proto_data: out0 += Proto2XML(this=this, extra_data=settings[4], enable_weight=settings[17])
# 	return out0


# def xmlSpecialDanmakuProcess(Proto_data) -> str:
# 	"""
# 	特殊弹幕 --> XML
# 	"""
# 	this: dm_pb2.CommandDm
# 	logging.debug(f"{bvid}: XML_Special_Process")
# 	out1 = ""
# 	for this in Proto_data:
# 		Ex_Extra_Data = ""
# 		if settings[4]: Ex_Extra_Data = f"<!-- SPECIAL: {this.command}{this.extra} -->"
# 		out1 += f"\t<d p=\"{format(this.stime/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(this.ctime, '%Y-%m-%d %H:%M:%S')))},999,{hex(crc32(str(this.mid).encode()) ^ 0xFFFFFFFF)[2:].lstrip('0')},{this.id},11\">{this.content}</d>{Ex_Extra_Data}\n"
# 	return out1


def DumpData(filename: str, data: bytes, Always_Write: bool = False) -> None:
	"""
	输出文件
	"""
	if settings[7] and ((not settings[8]) or Always_Write): pass
	else: return
	if len(data) == 0: return
	logging.debug("[dump_Data] " + filename)
	FileWriter(filename=filename, data=data, gz=False, binary_=True)


def MainFunc():
	"""
	视频处理
	"""
	# ================================ 视频信息1
	logging.debug(f"{bvid} Video info 1")
	video_info_1 = json.loads(Downloader(url_info_1, f"[{bvid}]_[0]_[Video]_[INFO].json"))
	try: video_info_1["data"]["ugc_season"]["sections"] = []
	except: pass
	DumpData(f"[{bvid}]_[0]_[Video]_[INFO].json", bytes(json.dumps(video_info_1, ensure_ascii=False, separators=(",", ":"), indent="\t"), encoding="utf-8"))
	# ================================ 视频信息2
	logging.debug(f"{bvid} Video info 2")
	if settings[8]: video_info_2 = '{"data":{"Related":[],"Reply":{"replies":[]}}}'
	else: video_info_2 = Downloader(url_info_2, f"[{bvid}]_[0]_[Video]_[INFO_2].json")
	video_info_2_load = json.loads(video_info_2)
	video_info_2_load["data"]["Related"] = []
	video_info_2_load["data"]["Reply"]["replies"] = []
	try: video_info_2_load["data"]["View"]["ugc_season"]["sections"] = []
	except: pass
	DumpData(f"[{bvid}]_[0]_[Video]_[INFO_2].json", bytes(json.dumps(video_info_2_load, ensure_ascii=False, separators=(',', ':'), indent="\t"), encoding="utf-8"))
	# ================================ 视频信息3
	logging.debug(f"{bvid} Video info V2 + wib")
	if settings[8]: video_info_3 = '{"data":{"Related":[],"Reply":{"replies":[]}}}'
	else: video_info_3 = Downloader(f"{url_info_3}?{gen_w_rid({'aid':avid_in})}", f"[{bvid}]_[0]_[Video]_[INFO_3].json")
	video_info_3_load = json.loads(video_info_3)
	DumpData(f"[{bvid}]_[0]_[Video]_[INFO_3].json", bytes(json.dumps(video_info_3_load, ensure_ascii=False, separators=(',', ':'), indent="\t"), encoding="utf-8"))
	# ================================ 加载
	json_info = video_info_1["data"]
	main_title:str = json_info["title"]
	pub_date = int(json_info["pubdate"])
	part_count = int(len(json_info["pages"]))
	# ================================ bvid aid 检查
	if json_info["bvid"] != bvid: logging.error(f"[bvid]: bvid mismatch {json_info['bvid']}|{bvid}")
	if json_info["aid"] != avid_in: logging.error(f"[avid]: avid mismatch av{json_info['aid']}|{avid}")
	if settings[14]: return
	# sys.exit()
	# ================================ 字幕
	if json_info["subtitle"] != None:
		for subs in json_info["subtitle"]["list"]:
			DumpData(f"[{bvid}]_[Subtitle]_[{subs['id']}]_[{subs['lan']}].bcc", Downloader(subs["subtitle_url"], f"[{bvid}]_[Subtitle]_[{subs['id']}]_[{subs['lan']}].bcc"), Always_Write=True)
			logging.debug(f"[{bvid}]: 字幕")
		if settings[15]: return
	# ================================ 分集处理
	iv = 0
	try:
		if json_info["premiere"] is not None: logging.warning(f"[{bvid}]: 首映 premiere")
	except:
		pass
	for This in json_info["pages"]:
		time_start_process = time.time()
		global err_sign
		global cid
		settings[2] = False
		iv += 1
		network_request_count[0] = 0
		cid = int(This["cid"])
		if settings[12] and settings[1]: break
		danmaku_final_binary = b""
		duration = int(This["duration"])
		segment_count = (duration/360).__ceil__()
		logging.debug(f"[{bvid}][Special_Danmaku]: P{iv}")
		extra_info_proto_binary = Downloader(f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}', f"[{bvid}]_[{cid}]_[BAS]_[INFO].bin")
		if settings[16]: continue
		extra_info_proto = dm_pb2.DmWebViewReply()
		extra_info_proto.ParseFromString(extra_info_proto_binary)
		extra_info_json = json.loads(MessageToJson(extra_info_proto, indent=0, ensure_ascii=False))
		DumpData(f"[{bvid}]_[{cid}]_[BAS]_[INFO].bin", extra_info_proto_binary)
# 		if (not settings[6]): xml_final = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>
# \t<chatserver>chat.bilibili.com</chatserver>
# \t<chatid>{cid}</chatid>
# \t<mission>0</mission>
# \t<maxlimit>0</maxlimit>
# \t<state>0</state>
# \t<real_name>0</real_name>
# \t<source>k-v</source>
# """
		part_title = str(This["part"])
		if part_title == "": part_title = f"P{iv}"
		logging.info(f"{pub_date}|{bvid}|{avid}|P{iv}/{part_count}|{cid}|{duration}|{segment_count}|{main_title}|{part_title}")
		if part_title == main_title: part_title = ""
		file_name = f"[{pub_date}][{bvid}][{avid}][P{iv}][{cid}]{main_title.replace('_', '＿')}_{part_title.replace('_', '＿')}".replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"", "＂").replace("\r", "").replace("\n", "").rstrip("_")	# \/:*?"<>|
		# [1656432000][BV*********][av*********][P**][cid]MainTitle_P-Title
		# if (not settings[6]) and settings[11]: xml_final += xmlSpecialDanmakuProcess(extra_info_proto.commandDms)
		if settings[9]:
			bas_danmaku = GetSpecialDanmaku(extra_info_proto)
		# 	xml_t1 = dm_pb2.DmSegMobileReply()
		# 	xml_t1.ParseFromString(bas_danmaku)
		# 	if (not settings[6]): xml_final += xmlDanmakuProcess(xml_t1.elems)
			danmaku_final_binary += bas_danmaku
		# 弹幕分段下载
		for segments in range(segment_count):
			if settings[12] and settings[1]: break
			try: danmaku_binary = GetDanmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: danmaku_binary = b""
			# 重试
			if len(danmaku_binary) < RETRY_SIZE and (not settings[8]):
				temp_file_len = len(danmaku_binary)
				retry_file = []
				for retry_i in range(RETRIES):
					if len(danmaku_binary) == 0: break
					try: retry_file.append(GetDanmaku(cid, str(segments+1), retries=f"_R{retry_i+1}"))
					except json.decoder.JSONDecodeError: retry_file.append(b"")
					if len(retry_file[retry_i]) > temp_file_len:
						danmaku_binary = retry_file[retry_i]
						del retry_file, temp_file_len
						break
			danmaku_final_binary += danmaku_binary
			# if (not settings[6]):
			# 	xml_t1 = dm_pb2.DmSegMobileReply()
			# 	xml_t1.ParseFromString(Danmaku_Binary)
			# 	xml_final += xmlDanmakuProcess(xml_t1.elems)
		# if Segment_Count != 1: dump_Data(f"[{bvid}]_[{cid}]_[Danmaku]_[ALL].bin", Danmaku_Final_Binary, Always_Write=True)
		time_process_danmaku = time.time()
		if (not settings[5]):
			logging.debug(f"[{bvid}][File_JSON] 开始处理 P{iv}")
			temp_binary = dm_pb2.DmSegMobileReply()
			temp_binary.ParseFromString(danmaku_final_binary)
			json_process = json.loads(MessageToJson(temp_binary, indent=None, ensure_ascii=False, including_default_value_fields=True))
			try:
				del json_process["state"]
			except:
				pass
			del temp_binary
			# ==================
			try:
				_ = json_process["elems"]
			except KeyError:
				json_process["elems"] = []
			else:
				for this in json_process["elems"]:
					this["date"] = int(this["date"])
					if this["usermid"] == "0": del this["usermid"]
					elif this["usermid"] == 0: del this["usermid"]
					else: this["usermid"] = int(this["usermid"])
					if not settings[2] and this["attr"] == 2: settings[2] = True
					if this["id"] == this["dmid"]: del this["id"]
					del this["test19"]
					del this["test23"]
					if this["action"] == "": del this["action"]
					if this["animation"] == "": del this["animation"]
					if this["test16"] == "0": del this["test16"]
					if this["test17"] == "0": del this["test17"]
					if this["test20"] == "0" or this["test20"] == "": del this["test20"]
					if this["test21"] == "0" or this["test21"] == "": del this["test21"]
					if this["test25"] == "": del this["test25"]
					if this["test26"] == "": del this["test26"]
					if this["test27"] == "": del this["test27"]
					if this["test28"] == "": del this["test28"]
					if this["test29"] == "": del this["test29"]
					if this["test30"] == "": del this["test30"]
					if this["test31"] == "": del this["test31"]
					if this["colorful"] == "NoneType": del this["colorful"]
					if this["mode"] == 1: del this["mode"]
					if this["size"] == 25: del this["size"]
					if this["color"] == 16777215: del this["color"]
					if this["pool"] == 0: del this["pool"]
					if this["attr"] == 0: del this["attr"]
					if this["replyCount"] == 0: del this["replyCount"]
					del this["likes"]
					del this["weight"]
			# ==================
			try: json_process["commandDms"] = extra_info_json["commandDms"]
			except KeyError: json_process["commandDms"] = []
			try: danmaku_count = len(json_process["elems"])
			except KeyError: danmaku_count = 0
			json_process["info"] = {}
			json_process["info"]["Ver"] = "V7_20230708"
			json_process["info"]["dmk_Ver"] = 5
			json_process["info"]["owner"] = json_info['owner']
			json_process["info"]["bvid"] = bvid
			json_process["info"]["avid"] = avid_in
			json_process["info"]["V_Name"] = main_title
			json_process["info"]["pubdate"] = pub_date
			json_process["info"]["ctime"] = json_info['ctime']
			json_process["info"]["P_Name"] = This["part"]
			json_process["info"]["cid"] = cid
			json_process["info"]["duration"] = duration
			json_process["info"]["segment_count"] = segment_count
			json_process["info"]["danmaku_count"] = danmaku_count
			json_process["info"]["danmaku_web_reported"] = json_info['stat']['danmaku']
			json_process["info"]["danmaku_proto_reported"] = extra_info_proto.count
			json_process["info"]["File_Create_Time_Start"] = int(time_start_process)
			json_process["info"]["File_Create_Time"] = int(time_process_danmaku)
			json_process["info"]["is_live_record"] = settings[2]
			Json_Write_Data = json.dumps(json_process, ensure_ascii=False, separators=(',', ':')).replace("},{\"stime\"", "},\n{\"stime\"")
			del json_process
			logging.debug(f"[{bvid}][File_JSON P{iv}]: 结束处理")
		if settings[12]: err_sign = "ERR_"
		if (not settings[5]):
			logging.debug(f"[{bvid}][File_JSON P{iv}]: 开始写入")
			FileWriter(f"{err_sign}{file_name}.json", Json_Write_Data, gz=settings[10])
			del Json_Write_Data
		# if (not settings[6]):
		# 	logging.debug(f"[{bvid}][File_XML  P{iv}]: 开始写入")
		# 	FileWriter(f"{err_sign}{file_name}.xml", xml_final + f"</i>\n<!-- Create Time: {time_process_danmaku} -->")
		# 	del xml_final
		del extra_info_proto, extra_info_json, extra_info_proto_binary, danmaku_final_binary
		time_part_end = time.time()
		logging.debug(f"P{iv}: {round(time_part_end-time_start_process, 3)}，Wait: {round(network_request_count[0]*SLEEP_TIME, 2)}，Net: {network_request_count[0]}")
	# ================================ 结束
	time_video_end = time.time()
	logging.debug(f"{bvid}|{avid} Time: {round(time_video_end-time_process_start, 3)} Net: {network_request_count[1]} Wait: {round(network_request_count[1]*SLEEP_TIME, 2)} SLEEP: {SLEEP_TIME}")


if __name__ == '__main__':
	time_process_start = time.time()
	# logging.debug(sys.argv)
	# ================================ 程序设置
	settings[0] = True
	settings[1] = True
	settings[3] = False
	settings[4] = False
	settings[5] = False
	settings[6] = False
	settings[7] = False
	settings[8] = False
	settings[9] = True
	settings[10] = False
	settings[11] = True
	settings[17] = True
	try: Program_FLAG(sys.argv[2])
	except IndexError: pass
	# ================================ 终端输入
	try: vids = sys.argv[1]
	except IndexError:
		logging.error("download.py av|bv [flag]")
		vids = input("输入：")
		Program_FLAG(input("FLAG: "))
		# vids = "[2,BV1xx411c7mD,https://www.bilibili.com/video/av2,http://www.bilibili.com/video/av2,https://www.bilibili.com/video/BV1xx411c7mD,http://www.bilibili.com/video/BV1xx411c7mD,https://b23.tv/av2,https://b23.tv/BV1xx411c7mD,http://b23.tv/av2,http://b23.tv/BV1xx411c7mD]"
		# vids = "2"
		# Program_FLAG("2688")
		# sys.exit()
	try:
		vids = json.loads(vids)
	except:
		vids = vids.split(",")

	for vid in vids:
		vid = str(vid)
		settings[2] = False	# X
		settings[12] = False	# X
		settings[13] = False	# X
		settings[14] = False	# X
		settings[15] = False	# X
		settings[16] = False	# X
		if vid.find("https://www.bilibili.com/video/") == 0: vid = vid.lstrip("https://www.bilibili.com/video/")
		if vid.find("http://www.bilibili.com/video/") == 0: vid = vid.lstrip("http://www.bilibili.com/video/")
		if vid.find("https://b23.tv/BV1") == 0 or vid.find("https://b23.tv/av") == 0: vid = vid.lstrip("https://b23.tv/")
		vid = vid.split("?")[0].split("/")[0]
		if vid.find("BV") == 0:
			bvid = vid[vid.find("BV"):vid.find("BV")+12]
			avid_in = BV2AV(bvid)
			avid = f"av{avid_in}"
			url_info_1 = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
			url_info_2 = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={bvid}"
		else:
			avid = vid
			avid_in = int(avid.lstrip("av"))
			avid = f"av{avid_in}"
			bvid = AV2BV(avid_in)
			url_info_1 = f"https://api.bilibili.com/x/web-interface/view?aid={avid_in}"
			url_info_2 = f"https://api.bilibili.com/x/web-interface/view/detail?aid={avid_in}"
		url_info_3="https://api.bilibili.com/x/web-interface/wbi/view"
		SettingsDebug(settings=settings)
		logging.info(f"{bvid}|{avid}")

		MainFunc()
	session.close()
	logging.info("Exit")