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

from my_lib.proto2xml_Lib import proto2xml
from my_lib.bvav import BV_to_AV, AV_to_BV
from my_lib.file_writer import writeER
from my_lib.debug import flag_debug

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.52"
headers = {
	'User-Agent': USER_AGENT,
	'origin': "https://www.bilibili.com",
	'referer': "https://www.bilibili.com",
	"Connection": "keep-alive"
}
SLEEP_TIME = 0.2
NET_count = [0, 0]
err_sign = ""
P_flag = []
for _ in range(64): P_flag.append(False)
RETRY_TIMES = 2
RETRY_SIZE = 2048


def Program_FLAG(flag: str) -> None:
	"""
	控制运行参数
	"""
	if flag == "-1": return
	if flag.find("0b") == 0: flag = "0"+flag
	else: flag = bin(int(flag))
	flag = "00000000000000000000000000000000" + flag.lstrip("0b")
	global P_flag
	for xx in range(-1, -len(flag), -1):
		if flag[xx] == "1": P_flag[-xx - 1] = True
		else: P_flag[-xx - 1] = False
	if P_flag[3]:
		# logging.Logger.setLevel(level=logging.DEBUG)
		logging.warning(f"Program_FLAG {flag}")


def Downloader(url_DL: str, filename: str, headers: dict = headers) -> bytes:
	"""
	下载
	"""
	logging.debug(f"[Downloader] {bvid}")
	global NET_count
	NET_count[0] += 1
	NET_count[1] += 1
	url_DL = url_DL.replace("http://", "https://")
	status_code = [0, 0]
	if P_flag[8]:
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
		if P_flag[3]:
			logging.debug(f"[NET]? File{status_code[0]}, Json{status_code[1]}")
		if status_code[1] != 0 or status_code[0] != 200:
			logging.error(f"[NET]? File{status_code[0]}, Json{status_code[1]}")
		logging.debug("[Downloader] " + filename)
		return DL_Data
	else:
		time.sleep(SLEEP_TIME)
		while True:
			try:
				DL_Data = requests.get(url_DL, headers=headers, verify=False, timeout=10)
			except TimeoutError:
				logging.warning("[Downloader] TimeoutError " + url_DL)
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
				P_flag[12] = True
		except UnicodeDecodeError: status_code[1] = 0
		except KeyError: status_code[1] = 0
		return DL_Data.content


def get_Danmaku(cid: str, Segment_Index: str, retry: str = "") -> bytes:
	"""
	获取弹幕
	"""
	logging.debug(f"{bvid}: [Danmaku] [{cid}] {Segment_Index} {retry}")
	tempString = ""
	# if Segment_Index == "1":tempString = "&pull_mode=1&ps=120000&pe=360000"
	# else:tempString = ""

	headers = {
		'Host': "api.bilibili.com",
		"Connection": "keep-alive",
		'Accept': "application/json, text/plain, */*",
		'User-Agent': USER_AGENT,
		'origin': "https://www.bilibili.com",
		'referer': f"https://www.bilibili.com/video/{bvid}/",
		'Accept-Encoding': "gzip, deflate, br",
	}
	File_Content = Downloader(f"https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&pid={avid_in}&segment_index={Segment_Index}{tempString}", f"[{bvid}]_[{cid}]_[Danmaku]_[{Segment_Index+retry}].bin", headers=headers)
	if P_flag[12] and P_flag[1]: return b""
	dump_Data(f"[{bvid}]_[{cid}]_[Danmaku]_[{Segment_Index+retry}].bin", File_Content)
	return File_Content


def get_Special_Danmaku(input: dm_pb2.DmWebViewReply) -> bytes:
	"""
	获取特殊弹幕
	"""
	logging.debug(f"{bvid}: get_Special_Danmaku")
	BAS_danmaku = b""
	i_for_BAS = 1
	for URL_special_dms in input.special_dms:
		BAS_Data = Downloader(URL_special_dms, f"[{bvid}]_[{cid}]_[BAS]_[{ URL_special_dms[27:67]}].bin")
		logging.debug(f"[BAS_DL]: Download {i_for_BAS}")
		if P_flag[12] and P_flag[1]: break
		BAS_danmaku += BAS_Data
		dump_Data(f"[{bvid}]_[{cid}]_[BAS]_[{ URL_special_dms[27:67]}].bin", BAS_Data)
		i_for_BAS += 1
	return BAS_danmaku


def XML_Process(Proto_data) -> str:
	"""
	弹幕 --> XML
	"""
	logging.debug(f"{bvid}: XML_Process")
	this: dm_pb2.DanmakuElem
	out0 = ""
	for this in Proto_data: out0 += proto2xml(this=this, extra_data=P_flag[4], enable_weight=P_flag[17])
	return out0


def XML_Special_Process(Proto_data) -> str:
	"""
	特殊弹幕 --> XML
	"""
	this: dm_pb2.CommandDm
	logging.debug(f"{bvid}: XML_Special_Process")
	out1 = ""
	for this in Proto_data:
		Ex_Extra_Data = ""
		if P_flag[4]: Ex_Extra_Data = f"<!-- SPECIAL: {this.command}{this.extra} -->"
		out1 += f"\t<d p=\"{format(this.progress/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(this.ctime, '%Y-%m-%d %H:%M:%S')))},999,{hex(crc32(str(this.mid).encode()) ^ 0xFFFFFFFF)[2:].lstrip('0')},{this.id},11\">{this.content}</d>{Ex_Extra_Data}\n"
	return out1


def dump_Data(filename: str, data: bytes, Always_Write: bool = False) -> None:
	"""
	输出文件
	"""
	if P_flag[7] and ((not P_flag[8]) or Always_Write): pass
	else: return
	if len(data) == 0: return
	logging.debug("[dump_Data] " + filename)
	writeER(filename=filename, data=data, gz=False, binary_=True)


def main_Func():
	"""
	视频处理
	"""
	# ================================ 视频信息（全部）
	logging.debug(f"{bvid} Video info 1")
	video_info = json.loads(Downloader(url_info_1, f"[{bvid}]_[0]_[Video]_[INFO].json"))
	try: video_info["data"]["ugc_season"]["sections"] = []
	except: pass
	dump_Data(f"[{bvid}]_[0]_[Video]_[INFO].json", bytes(json.dumps(video_info, ensure_ascii=False, separators=(",", ":"), indent="\t"), encoding="utf-8"))
	# ================================ 视频信息?
	logging.debug(f"{bvid} Video info 2")
	if P_flag[8]: video_info_detail = '{"data":{"Related":[],"Reply":{"replies":[]}}}'
	else: video_info_detail = Downloader(url_info_2, f"[{bvid}]_[0]_[Video]_[INFO_Detail].json")
	Vid_detail_json = json.loads(video_info_detail)
	Vid_detail_json["data"]["Related"] = []
	Vid_detail_json["data"]["Reply"]["replies"] = []
	try: Vid_detail_json["data"]["View"]["ugc_season"]["sections"] = []
	except: pass
	dump_Data(f"[{bvid}]_[0]_[Video]_[INFO_Detail].json", bytes(json.dumps(Vid_detail_json, ensure_ascii=False, separators=(',', ':'), indent="\t"), encoding="utf-8"))
	# ================================ 加载
	Json_Info = video_info["data"]
	Main_Title = Json_Info["title"]
	P_Date = int(Json_Info["pubdate"])
	Num_of_Videos = int(len(Json_Info["pages"]))
	# ================================ bvid aid 检查
	if Json_Info["bvid"] != bvid: logging.error(f"[bvid]: bvid mismatch {Json_Info['bvid']}|{bvid}")
	if Json_Info["aid"] != avid_in: logging.error(f"[avid]: avid mismatch av{Json_Info['aid']}|{avid}")
	if P_flag[14]: return
	# ================================ 字幕
	for subs in Json_Info["subtitle"]["list"]:
		dump_Data(f"[{bvid}]_[Subtitle]_[{subs['id']}]_[{subs['lan']}].bcc", Downloader(subs["subtitle_url"], f"[{bvid}]_[Subtitle]_[{subs['id']}]_[{subs['lan']}].bcc"), Always_Write=True)
		logging.debug(f"[{bvid}]: 字幕")
	if P_flag[15]: return
	# ================================ 分集处理
	i_for_videos = 0
	try:
		if Json_Info["premiere"] is not None:
			logging.warning(f"[{bvid}]: 首映 premiere")
	except:
		pass
	for This in Json_Info["pages"]:
		Time_Start_Process = time.time()
		global err_sign
		global cid
		P_flag[2] = False
		i_for_videos += 1
		NET_count[0] = 0
		cid = int(This["cid"])
		if P_flag[12] and P_flag[1]: break
		Danmaku_Final_Binary = b""
		duration = int(This["duration"])
		Segment_Count = (duration/360).__ceil__()
		# if time.time() < P_Date+Segment_Count*3000/12.5+duration*2:
		logging.debug(f"[{bvid}][Special_Danmaku]: P{i_for_videos}")
		DL_Data_Extra_Info = Downloader(f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}', f"[{bvid}]_[{cid}]_[BAS]_[INFO].bin")
		if P_flag[16]: continue
		ExInfo_Proto = dm_pb2.DmWebViewReply()
		ExInfo_Proto.ParseFromString(DL_Data_Extra_Info)
		ExInfo_Json = json.loads(MessageToJson(ExInfo_Proto, indent=0, ensure_ascii=False))
		dump_Data(f"[{bvid}]_[{cid}]_[BAS]_[INFO].bin", DL_Data_Extra_Info)
		if (not P_flag[6]): XML_Write_Data = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>
\t<chatserver>chat.bilibili.com</chatserver>
\t<chatid>{cid}</chatid>
\t<mission>0</mission>
\t<maxlimit>0</maxlimit>
\t<state>0</state>
\t<real_name>0</real_name>
\t<source>k-v</source>
"""
		P_Title = str(This["part"])
		if P_Title == "": P_Title = f"P{i_for_videos}"
		logging.info(f"{P_Date}|{bvid}|{avid}|P{i_for_videos}/{Num_of_Videos}|{cid}|{duration}|{Segment_Count}|{Main_Title}|{P_Title}")
		if P_Title == Main_Title: P_Title = ""
		File_Name = f"[{P_Date}][{bvid}][{avid}][P{i_for_videos}][{cid}]{Main_Title.replace('_', '＿')}_{P_Title.replace('_', '＿')}".replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"", "＂").replace("\r", "").replace("\n", "").rstrip("_")	# \/:*?"<>|
		# [1656432000][BV*********][av*********][P**][cid]MainTitle_P-Title
		if (not P_flag[6]) and P_flag[11]: XML_Write_Data += XML_Special_Process(ExInfo_Proto.commandDms)
		if P_flag[9]:
			BAS_danmaku = get_Special_Danmaku(ExInfo_Proto)
			xml_t1 = dm_pb2.DmSegMobileReply()
			xml_t1.ParseFromString(BAS_danmaku)
			if (not P_flag[6]): XML_Write_Data += XML_Process(xml_t1.elems)
			Danmaku_Final_Binary += BAS_danmaku
		# 弹幕分段下载
		for segments in range(Segment_Count):
			if P_flag[12] and P_flag[1]: break
			try: Danmaku_Binary = get_Danmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: Danmaku_Binary = b""
			# 重试
			if len(Danmaku_Binary) < RETRY_SIZE and (not P_flag[8]):
				temp_filelen = len(Danmaku_Binary)
				retry_file = []
				for retry_i in range(RETRY_TIMES):
					if len(Danmaku_Binary) == 0: break
					try: retry_file.append(get_Danmaku(cid, str(segments+1), retry=f"_R{retry_i+1}"))
					except json.decoder.JSONDecodeError: retry_file.append(b"")
					if len(retry_file[retry_i]) > temp_filelen:
						Danmaku_Binary = retry_file[retry_i]
						del retry_file, temp_filelen
						break
			Danmaku_Final_Binary += Danmaku_Binary
			if (not P_flag[6]):
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_Binary)
				XML_Write_Data += XML_Process(xml_t1.elems)
		# if Segment_Count != 1: dump_Data(f"[{bvid}]_[{cid}]_[Danmaku]_[ALL].bin", Danmaku_Final_Binary, Always_Write=True)
		Time_Process_Danmaku = time.time()
		if (not P_flag[5]):
			logging.debug(f"[{bvid}][File_JSON] 开始处理 P{i_for_videos}")
			Temp_Binary = dm_pb2.DmSegMobileReply()
			Temp_Binary.ParseFromString(Danmaku_Final_Binary)
			json_process = json.loads(MessageToJson(Temp_Binary, indent=None, ensure_ascii=False, including_default_value_fields=True))
			del json_process["state"]
			del Temp_Binary
			# ==================
			try:
				json_process["elems"]
			except KeyError:
				json_process["elems"] = []
			else:
				for this in json_process["elems"]:
					this["ctime"] = int(this["ctime"])
					this["usermid"] = int(this["usermid"])
					if not P_flag[2] and this["attr"] == 2: P_flag[2] = True
					del this["idStr"]
					del this["test19"]
					del this["test23"]
					if this["action"] == "": del this["action"]
					if this["animation"] == "": del this["animation"]
					if this["test16"] == "0": del this["test16"]
					if this["test17"] == "0": del this["test17"]
					if this["test20"] == "0" or this["test20"] == "": del this["test20"]
					if this["test21"] == "0" or this["test21"] == "": del this["test21"]
					if this["mode"] == 1: del this["mode"]
					if this["fontsize"] == 25: del this["fontsize"]
					if this["color"] == 16777215: del this["color"]
					if this["pool"] == 0: del this["pool"]
					if this["attr"] == 0: del this["attr"]
					if this["replyCount"] == 0: del this["replyCount"]
					del this["likes"]
					del this["weight"]
			# ==================
			try: json_process["commandDms"] = ExInfo_Json["commandDms"]
			except KeyError: json_process["commandDms"] = []
			try: Danmaku_Count = len(json_process["elems"])
			except KeyError: Danmaku_Count = 0
			json_process["info"] = {}
			json_process["info"]["Ver"] = "V5_20220916"
			json_process["info"]["dmk_Ver"] = 3
			json_process["info"]["owner"] = Json_Info['owner']							# dict	get all
			json_process["info"]["bvid"] = bvid											# str	get all
			json_process["info"]["avid"] = avid_in										# num	get all
			json_process["info"]["V_Name"] = Main_Title									# str	get all
			json_process["info"]["pubdate"] = P_Date									# num	get all unix_timestamp
			json_process["info"]["i_ctime"] = Json_Info['ctime']						# num	get all unix_timestamp
			json_process["info"]["P_Name"] = This["part"]								# str	get part
			json_process["info"]["cid"] = cid											# num	get part
			json_process["info"]["duration"] = duration									# num	get part
			json_process["info"]["segment_count"] = Segment_Count						# num	set
			json_process["info"]["danmaku_count"] = Danmaku_Count						# num	set
			json_process["info"]["danmaku_web_reported"] = Json_Info['stat']['danmaku']	# num	get
			json_process["info"]["danmaku_proto_reported"] = ExInfo_Proto.count			# num	get
			json_process["info"]["File_Create_Time_Start"] = int(Time_Start_Process)	# num	set unix_timestamp
			json_process["info"]["File_Create_Time"] = int(Time_Process_Danmaku)		# num	set unix_timestamp
			json_process["info"]["is_live_record"] = P_flag[2]							# bool	GET
			Json_Write_Data = json.dumps(json_process, ensure_ascii=False, separators=(',', ':')).replace("},{\"id\"", "},\n{\"id\"")
			del json_process
			logging.debug(f"[{bvid}][File_JSON P{i_for_videos}]: 结束处理")
		if P_flag[12]: err_sign = "ERR_"
		if (not P_flag[5]):
			logging.debug(f"[{bvid}][File_JSON P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.json", Json_Write_Data, gz=P_flag[10])
			del Json_Write_Data
		if (not P_flag[6]):
			logging.debug(f"[{bvid}][File_XML  P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.xml", XML_Write_Data + f"</i>\n<!-- Create Time: {Time_Process_Danmaku} -->")
			del XML_Write_Data
		del ExInfo_Proto, ExInfo_Json, DL_Data_Extra_Info, Danmaku_Final_Binary
		timeD = time.time()
		logging.debug(f"P{i_for_videos}: {round(timeD-Time_Start_Process, 3)}，Wait: {round(NET_count[0]*SLEEP_TIME, 2)}，Net: {NET_count[0]}")
	# ================================ 结束
	timeE = time.time()
	logging.debug(f"{bvid}|{avid} Time: {round(timeE-timeA, 3)} Net: {NET_count[1]} Wait: {round(NET_count[1]*SLEEP_TIME, 2)} SLEEP: {SLEEP_TIME}")


if __name__ == '__main__':
	timeA = time.time()
	# logging.debug(sys.argv)
	# ================================ 程序设置
	P_flag[0] = True
	P_flag[1] = True
	P_flag[3] = False
	P_flag[4] = False
	P_flag[5] = False
	P_flag[6] = False
	P_flag[7] = False
	P_flag[8] = False
	P_flag[9] = True
	P_flag[10] = False
	P_flag[11] = True
	P_flag[17] = True
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
		P_flag[2] = False	# X
		P_flag[12] = False	# X
		P_flag[13] = False	# X
		P_flag[14] = False	# X
		P_flag[15] = False	# X
		P_flag[16] = False	# X
		if vid.find("https://www.bilibili.com/video/") == 0: vid = vid.lstrip("https://www.bilibili.com/video/")
		if vid.find("http://www.bilibili.com/video/") == 0: vid = vid.lstrip("http://www.bilibili.com/video/")
		if vid.find("https://b23.tv/BV1") == 0 or vid.find("https://b23.tv/av") == 0: vid = vid.lstrip("https://b23.tv/")
		vid = vid.split("?")[0].split("/")[0]
		if vid.find("BV") == 0:
			bvid = vid[vid.find("BV"):vid.find("BV")+12]
			avid_in = BV_to_AV(bvid)
			avid = f"av{avid_in}"
			url_info_1 = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
			url_info_2 = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={bvid}"
		else:
			avid = vid
			avid_in = int(avid.lstrip("av"))
			avid = f"av{avid_in}"
			bvid = AV_to_BV(avid_in)
			url_info_1 = f"https://api.bilibili.com/x/web-interface/view?aid={avid_in}"
			url_info_2 = f"https://api.bilibili.com/x/web-interface/view/detail?aid={avid_in}"
		flag_debug(pflag=P_flag)
		logging.info(f"{bvid}|{avid}")

		main_Func()
	logging.info("Exit")