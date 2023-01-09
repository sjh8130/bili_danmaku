#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson
import ssl
import requests
import binascii
import math
import time
import json
import sys
import tarfile
import threading
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

headers = {
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53",
	'origin': "https://www.bilibili.com",
	'referer': "https://www.bilibili.com",
	"Connection": "keep-alive"
}
SLEEP_TIME = 0.05
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
		logging.debug(f"Program_FLAG {flag}")


def Downloader(url_DL: str, str_s: dict) -> bytes:
	"""
	下载
	"""
	logging.debug(f"{bvid} {cid}: Downloader")
	global NET_count
	NET_count[0] += 1
	NET_count[1] += 1
	url_DL = url_DL.replace("http://", "https://")
	status_code = [0, 0]
	if P_flag[8]:
		try:
			DL_Data = open(f"[{str_s[4]}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}", "rb").read()
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
		logging.debug(f"[{str_s[4]}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}")
		return DL_Data
	else:
		time.sleep(SLEEP_TIME)
		DL_Data = requests.get(url_DL, headers=headers, verify=False)
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
	logging.debug(f"{bvid} {cid}: get_Danmaku")
	ARR_Danmaku_name = [cid, "Danmaku", Segment_Index+retry, "bin", bvid]
	Content = Downloader(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={Segment_Index}', ARR_Danmaku_name)
	if P_flag[12] and P_flag[1]: return b""
	dump_Data(str_s=ARR_Danmaku_name, data=Content)
	return Content


def get_Special_Danmaku(input: dm_pb2.DmWebViewReply) -> bytes:
	"""
	获取特殊弹幕
	"""
	logging.debug(f"{bvid} {cid}: get_Special_Danmaku")
	BAS_Binary = b""
	i_for_BAS = 1
	for URL_special_dms in input.special_dms:
		ARR_BAS_name = [cid, "BAS", URL_special_dms[27:67], "bin", bvid]
		BAS_Data = Downloader(url_DL=URL_special_dms, str_s=ARR_BAS_name)
		logging.debug(f"[BAS_DL]: Download {i_for_BAS}")
		if P_flag[12] and P_flag[1]: break
		BAS_Binary += BAS_Data
		dump_Data(str_s=ARR_BAS_name, data=BAS_Data)
		i_for_BAS += 1
	return BAS_Binary


def XML_Process(Proto_data) -> str:
	"""
	弹幕 --> XML
	"""
	logging.debug(f"{bvid} {cid}: XML_Process")
	this: dm_pb2.DanmakuElem
	out0 = ""
	for this in Proto_data: out0 += proto2xml(this=this, exdata=P_flag[4], enable_weight=P_flag[17])
	return out0


def XML_Special_Process(Proto_data) -> str:
	"""
	特殊弹幕 --> XML
	"""
	this: dm_pb2.CommandDm
	logging.debug(f"{bvid} {cid}: XML_Special_Process")
	out1 = ""
	for this in Proto_data:
		Ex_Extra_Data = ""
		if P_flag[4]: Ex_Extra_Data = f"<!-- SPECIAL: {this.command}{this.extra} -->"
		out1 += f"\t<d p=\"{format(this.progress/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(this.ctime, '%Y-%m-%d %H:%M:%S')))},999,{hex(binascii.crc32(str(this.mid).encode()) ^ 0xFFFFFFFF).lstrip('0x').lstrip('0')},{this.id},11\">{this.content}</d>{Ex_Extra_Data}\n"
	return out1


def dump_Data(str_s: dict, data: bytes, force: bool = False) -> None:
	"""
	输出文件
	"""
	if P_flag[7] and ((not P_flag[8]) or force): pass
	else: return
	if len(data) == 0: return
	logging.debug(f"[file]: {str_s[4]}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}")
	writeER(filename=f"[{str_s[4]}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}", data=data, gz=False, binary_=True)


def main_Func():
	"""
	视频处理
	"""
	# ================================ 视频信息（全部）
	ARR_json_Resp_name = ["0", "Video", "INFO", "json", bvid]
	logging.debug(f"{bvid} Video info 1")
	video_info = json.loads(Downloader(url_DL=url_info_1, str_s=ARR_json_Resp_name))
	try: video_info["data"]["ugc_season"]["sections"] = []
	except: pass
	threading.Thread(dump_Data(str_s=ARR_json_Resp_name, data=bytes(json.dumps(video_info, ensure_ascii=False, separators=(",", ":"), indent="\t"), encoding="utf-8"))).start()
	# ================================ 视频信息?
	ARR_Info_Detail_name = ["0", "Video", "INFO_Detail", "json", bvid]
	logging.debug(f"{bvid} Video info 2")
	if P_flag[8]: video_info_detail = '{"data":{"Related":[],"Reply":{"replies":[]}}}'
	else: video_info_detail = Downloader(url_DL=url_info_2, str_s=ARR_Info_Detail_name)
	Vid_detail_json = json.loads(video_info_detail)
	Vid_detail_json["data"]["Related"] = []
	Vid_detail_json["data"]["Reply"]["replies"] = []
	try: Vid_detail_json["data"]["View"]["ugc_season"]["sections"] = []
	except: pass
	threading.Thread(dump_Data(str_s=ARR_Info_Detail_name, data=bytes(json.dumps(Vid_detail_json, ensure_ascii=False, separators=(',', ':'), indent="\t"), encoding="utf-8"))).start()
	# ================================ 加载
	Json_Info = video_info["data"]
	Main_Title = Json_Info["title"]
	P_Date = str(Json_Info["pubdate"])
	if Main_Title == "": Main_Title = "Fake_MainTitle"
	Num_of_Videos = int(len(Json_Info["pages"]))
	# ================================ bvid aid 检查
	if Json_Info["bvid"] != bvid: logging.error(f"[bvid]: bvid mismatch {Json_Info['bvid']}|{bvid}")
	if Json_Info["aid"] != avid_in: logging.error(f"[avid]: avid mismatch av{Json_Info['aid']}|{avid}")
	if P_flag[14]: return
	# ================================ 字幕
	for subs in Json_Info["subtitle"]["list"]:
		subs_name = ["0", "Subs", f"{subs['id']}_{subs['lan']}", "bcc", bvid]
		threading.Thread(dump_Data(str_s=subs_name, data=Downloader(url_DL=subs["subtitle_url"], str_s=subs_name), force=True)).start()
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
		timeB = time.time()
		global err_sign
		global cid
		P_flag[2] = False
		i_for_videos += 1
		NET_count[0] = 0
		cid = str(This["cid"])
		if P_flag[12] and P_flag[1]: break
		Danmaku_Final_Binary = b""
		duration = int(This["duration"])
		Segment_Count = math.ceil(duration/360)
		logging.info(f"[{bvid}][Special_Danmaku]: P{i_for_videos}")
		ARR_Ext_Info = [cid, "BAS", "INFO", "bin", bvid]
		DL_Data_Extra_Info = Downloader(url_DL=f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}', str_s=ARR_Ext_Info)
		if P_flag[16]: continue
		ExInfo_Proto = dm_pb2.DmWebViewReply()
		ExInfo_Proto.ParseFromString(DL_Data_Extra_Info)
		ExInfo_Json = json.loads(MessageToJson(ExInfo_Proto, indent=0, ensure_ascii=False))
		threading.Thread(dump_Data(str_s=ARR_Ext_Info, data=DL_Data_Extra_Info)).start()
		if (not P_flag[6]): XML_Write_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>{6000*Segment_Count}</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
		P_Title = str(This["part"])
		if P_Title == "": P_Title = f"P{i_for_videos}"
		logging.info(f"{P_Date}|{bvid}|{avid}|P{i_for_videos}/{Num_of_Videos}|{cid}|{duration}|{math.ceil(duration/360)}|{Main_Title}|{P_Title}")
		if P_Title == Main_Title: P_Title = ""
		File_Name = f"[{P_Date}][{bvid}][{avid}][P{i_for_videos}][{cid}]{Main_Title.replace('_', '＿')}_{P_Title.replace('_', '＿')}".replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"", "＂").replace("\r", "").replace("\n", "").rstrip("_")	# \/:*?"<>|
		# [1656432000][BV*********][av*********][P**][cid]MainTitle_P-Title
		if (not P_flag[6]) and P_flag[11]: XML_Write_Data += XML_Special_Process(ExInfo_Proto.commandDms, cid=cid)
		if P_flag[9]:
			BAS_danmaku = get_Special_Danmaku(ExInfo_Proto)
			xml_t1 = dm_pb2.DmSegMobileReply()
			xml_t1.ParseFromString(BAS_danmaku)
			if (not P_flag[6]): XML_Write_Data += XML_Process(xml_t1.elems)
			Danmaku_Final_Binary += BAS_danmaku
		# 弹幕分段下载
		for segments in range(Segment_Count):
			if P_flag[12] and P_flag[1]: break
			try: Danmaku_Binarys = get_Danmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: Danmaku_Binarys = b""
			logging.info(f"[{bvid}][danmaku]: P{i_for_videos}/{Num_of_Videos}\t{segments+1}/{Segment_Count}")
			# 重试
			if len(Danmaku_Binarys) < RETRY_SIZE and (not P_flag[8]):
				temp_filelen = len(Danmaku_Binarys)
				retry_file = []
				for retry_i in range(RETRY_TIMES):
					if len(Danmaku_Binarys) == 0: break
					try: retry_file.append(get_Danmaku(cid, str(segments+1), retry=f"_R{retry_i+1}"))
					except json.decoder.JSONDecodeError: retry_file.append(b"")
					if len(retry_file[retry_i]) > temp_filelen:
						Danmaku_Binarys = retry_file[retry_i]
						del retry_file, temp_filelen
						break
					logging.info(f"[{bvid}][danmaku]: P{i_for_videos}/{Num_of_Videos}\t{segments+1}/{Segment_Count} [R{retry_i+1}]")
			Danmaku_Final_Binary += Danmaku_Binarys
			if (not P_flag[6]):
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_Binarys)
				XML_Write_Data += XML_Process(xml_t1.elems)
		# if Segment_Count != 1: dump_Data(str_s=[cid, "Danmaku", "ALL", "bin", bvid], data=Danmaku_Final_Binary, force=True)
		timeC = time.time()
		if (not P_flag[5]):
			logging.debug(f"[{bvid}][File_JSON P{i_for_videos}]: 开始处理")
			Temp_Binary = dm_pb2.DmSegMobileReply()
			Temp_Binary.ParseFromString(Danmaku_Final_Binary)
			json_proccess = json.loads(MessageToJson(Temp_Binary, indent=0, ensure_ascii=False))
			del Temp_Binary
			# ==================
			P_flag[13] = False
			try:
				json_proccess["elems"]
				P_flag[13] = True
			except KeyError:
				json_proccess["elems"] = []
			if P_flag[13]:
				for that in json_proccess["elems"]:
					try: del that["idStr"]
					except KeyError: pass
					try:
						if that["test20"] == "0": del that["test20"]
					except KeyError: pass
					try:
						if that["test21"] == "0": del that["test21"]
					except KeyError: pass
					try:
						if that["mode"] == 1: del that["mode"]
					except KeyError: that["mode"] = 0
					try:
						if that["fontsize"] == 25: del that["fontsize"]
					except KeyError: that["fontsize"] = 0
					try:
						if that["color"] == 16777215: del that["color"]
					except KeyError: that["color"] = 0
					try: del that["likes"]
					except KeyError: pass
					try: del that["weight"]
					except KeyError: pass
					try:
						if that["attr"] == 2: P_flag[2] = True
					except KeyError: pass
			P_flag[13] = False
			# ==================
			if P_flag[8]:
				try: time_FC = json.loads(open(f"{File_Name}.json", "r", encoding="utf-8"))["info"]["File_Create_Time"]
				except: time_FC = timeC
			else: time_FC = timeC
			try: json_proccess["commandDms"] = ExInfo_Json["commandDms"]
			except KeyError: json_proccess["commandDms"] = []
			try: Danmaku_Count = len(json_proccess["elems"])
			except KeyError: Danmaku_Count = 0
			json_proccess["info"] = {}
			json_proccess["info"]["Ver"] = "V5_20220916"
			json_proccess["info"]["dmk_Ver"] = 2
			json_proccess["info"]["owner"] = Json_Info['owner']								# dict get all
			json_proccess["info"]["bvid"] = Json_Info['bvid']								# str  get all
			json_proccess["info"]["avid"] = Json_Info['aid']								# num  get all
			json_proccess["info"]["V_Name"] = Json_Info["title"]							# str  get all
			json_proccess["info"]["pubdate"] = Json_Info['pubdate']							# num  get all unix_timestamp
			json_proccess["info"]["i_ctime"] = Json_Info['ctime']							# num  get all unix_timestamp
			json_proccess["info"]["P_Name"] = This["part"]									# str  get part
			json_proccess["info"]["cid"] = This["cid"]										# num  get part
			json_proccess["info"]["duration"] = This["duration"]							# num  get part
			json_proccess["info"]["segment_count"] = Segment_Count							# num  set
			json_proccess["info"]["danmaku_count"] = Danmaku_Count							# num  set
			json_proccess["info"]["danmaku_web_reported"] = Json_Info['stat']['danmaku']	# num get
			json_proccess["info"]["danmaku_proto_reported"] = ExInfo_Proto.count			# num get
			json_proccess["info"]["File_Create_Time"] = int(time_FC)						# num  set unix_timestamp
			json_proccess["info"]["File_Create_Time_Start"] = int(timeA)					# num  set unix_timestamp
			json_proccess["info"]["is_live_record"] = P_flag[2]								# bool GET
			Json_Write_Data = json.dumps(json_proccess, ensure_ascii=False, separators=(',', ':')).replace("},{\"id\"", "},\n{\"id\"")
			del json_proccess
			logging.debug(f"[{bvid}][File_JSON P{i_for_videos}]: 结束处理")
		if P_flag[12]: err_sign = "ERR_"
		if (not P_flag[5]):
			logging.debug(f"[{bvid}][File_JSON P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.json", Json_Write_Data, gz=P_flag[10])
			del Json_Write_Data
		if (not P_flag[6]):
			logging.debug(f"[{bvid}][File_XML  P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.xml", XML_Write_Data + f"</i>\n<!-- Create Time: {str(int(timeC))} -->")
			del XML_Write_Data
		del ExInfo_Proto, ExInfo_Json, DL_Data_Extra_Info, Danmaku_Final_Binary
		timeD = time.time()
		logging.debug(f"P{i_for_videos}: {round(timeD-timeB, 3)}，Wait: {round(NET_count[0]*SLEEP_TIME, 2)}，Net: {NET_count[0]}")
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
	vids = vids.split(",")
	
	for vid in vids:
		vid = str(vid)
		P_flag[2] = False  # X
		P_flag[12] = False  # X
		P_flag[13] = False  # X
		P_flag[14] = False  # X
		P_flag[15] = False  # X
		P_flag[16] = False  # X
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