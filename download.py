#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson

import requests
import binascii
import math
import time
import json
import sys
import tarfile
import threading

try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

from my_lib.proto2xml_Lib import proto2xml
from my_lib.bvav import BV_to_AV, AV_to_BV
from my_lib.file_writer import writeER
from my_lib.debug import flag_debug

headers = {
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27",
	'origin': "https://www.bilibili.com",
	'referer': "https://www.bilibili.com"
	}
SLEEP_TIME = 0.03
NET_count = [0, 0]
err_sign = ""
P_flag = []
for i in range(32):P_flag.append(False)
def Program_FLAG(flag: str) -> None:
	"""
	Text
	"""
	if flag == "-1": return
	if flag.find("0b") == 0: b = "0"+flag
	else: b = bin(int(flag))
	b = "00000000000000000000000000000000" + b.lstrip("0b")
	global P_flag
	for xx in range(-1,-len(b),-1):
		if b[xx] == "1": P_flag[-xx - 1] = True
		else: P_flag[-xx - 1] = False
	if P_flag[3]: print(f"[FLAG]: {b}")


def Downloader(url_DL: str, str_s: dict) -> bytes:
	"""
	Text
	"""
	global NET_count
	NET_count[0] += 1
	NET_count[1] += 1
	status_code = [0,0]
	if P_flag[3]: print(f"[NET]: {url_DL}\t{NET_count[1]}   ", end="\t")
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
		if P_flag[3] or status_code[1] != 0 or status_code[0] != 200: print(f"[NET]? File {status_code[0]}, Json Code {status_code[1]}", end="\t")
		if (not P_flag[3]) and (status_code[1] != 0 or status_code[0] != 200): print(f"[{str_s[4]}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}")
		return DL_Data
	else:
		time.sleep(SLEEP_TIME)
		DL_Data = requests.get(url_DL, headers=headers)
		status_code[0] = DL_Data.status_code
		try:
			status_code[1] = json.loads(DL_Data.content)["code"]
			if status_code[1] != 0:
				P_flag[12] = True
		except UnicodeDecodeError: status_code[1] = 0
		except KeyError: status_code[1] = 0
		if P_flag[3] or status_code[1] != 0 or status_code[0] != 200: print(f"[NET]: HTTP {status_code[0]}, Json Code {status_code[1]}", end="\t")
		if (not P_flag[3]) and (status_code[1] != 0 or status_code[0] != 200): print(url_DL)
		return DL_Data.content


def get_Danmaku(cid: str, Segment_Index: str, retry: str = "") -> bytes:
	"""
	Text
	"""
	ARR_Danmaku_name = [cid, "Danmaku", Segment_Index+retry, "bin", bvid]
	Content = Downloader(f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={Segment_Index}', ARR_Danmaku_name)
	if P_flag[12] and P_flag[1]: return b""
	dump_Data(str_s=ARR_Danmaku_name, data=Content)
	return Content


def get_Special_Danmaku(input: dm_pb2.DmWebViewReply) -> bytes:
	"""
	Text
	"""
	BAS_Binary = b""
	i_for_BAS = 1
	for URL_special_dms in input.special_dms:
		ARR_BAS_name = [cid, "BAS", URL_special_dms[27:67], "bin", bvid]
		BAS_Data = Downloader(url_DL=URL_special_dms, str_s=ARR_BAS_name)
		if P_flag[3]: print(f"[BAS_DL]: Download {i_for_BAS}")
		if P_flag[12] and P_flag[1]: break
		BAS_Binary += BAS_Data
		dump_Data(str_s=ARR_BAS_name, data=BAS_Data)
		i_for_BAS += 1
	return BAS_Binary


def XML_Process(data) -> str:
	"""
	Text
	"""
	this: dm_pb2.DanmakuElem
	out0 = ""
	for this in data: out0 += proto2xml(this=this, exdata=P_flag[4], enable_weight=True)
	return out0


def XML_Special_Process(data, cid) -> str:
	"""
	Text
	"""
	this: dm_pb2.CommandDm
	out1 = ""
	for this in data:
		Ex_Extra_Data = ""
		if P_flag[4]: Ex_Extra_Data = f"<!-- SPECIAL: {this.command}{this.extra} -->"
		out1 += f"\t<d p=\"{format(this.progress/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(this.ctime, '%Y-%m-%d %H:%M:%S')))},999,{hex(binascii.crc32(str(this.mid).encode()) ^ 0xFFFFFFFF).lstrip('0x').lstrip('0')},{this.id},11\">{this.content}</d>{Ex_Extra_Data}\n"
	return out1


def dump_Data(str_s: dict, data: bytes, force: bool = False) -> None:
	"""
	Text
	"""
	if P_flag[7] and ((not P_flag[8]) or force): pass
	else: return
	if len(data) == 0: return
	writeER(filename=f"[{str_s[4]}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}", data=data, gz=False, binary_=True)


if __name__ == '__main__':
	timeA = time.time()
	# print(sys.argv)
	# ================================ 程序设置
	P_flag[0]  = True	#    1 计时器
	P_flag[1]  = True	#    2 错误停机
	P_flag[2]  = False	#    X 直播回放:set
	P_flag[3]  = False	#    8 日志
	P_flag[4]  = False	#   16 输出 其他信息到 XML 文件
	P_flag[5]  = False	#   32 不输出 Json
	P_flag[6]  = False	#   64 不输出 XML
	P_flag[7]  = False	#  128 输出 Protobuf 二进制文件
	P_flag[8]  = False	#  256 模拟运行
	P_flag[9]  = True	#  512 特殊弹幕:BAS
	P_flag[10] = False	# 1024 压缩为gzip
	P_flag[11] = True	# 2048 特殊弹幕:UP主自定义内容
	P_flag[12] = False	# 4096 is_ERROR:set
	P_flag[13] = False	# 8192 in use
	try: Program_FLAG(sys.argv[2])
	except IndexError: pass
	# if flag_Test_Run: print("[Test Run]: ================================ ")
	# ================================ 终端输入
	try: vid = sys.argv[1]
	except IndexError:
		print("download.py av|bv [flag]")
		# vid = "av2"
		# Program_FLAG("2688")
		sys.exit()
	if vid.find("https://www.bilibili.com/video/") == 0: vid = vid.lstrip("https://www.bilibili.com/video/")
	if vid.find("http://www.bilibili.com/video/") == 0: vid = vid.lstrip("http://www.bilibili.com/video/")
	if vid.find("https://b23.tv/BV1") == 0 or vid.find("https://b23.tv/av") == 0: vid = vid.lstrip("https://b23.tv/")
	vid = vid.split("?")[0].split("/")[0]
	if vid.find("av") == 0:
		avid = vid
		avid_in = int(avid.lstrip("av"))
		bvid = AV_to_BV(avid_in)
		url_Main = f"https://api.bilibili.com/x/web-interface/view?aid={avid_in}"
		url_xx1 = f"https://api.bilibili.com/x/web-interface/view/detail?aid={avid_in}"
	else:
		bvid = vid[vid.find("BV"):vid.find("BV")+12]
		avid_in = BV_to_AV(bvid)
		avid = f"av{avid_in}"
		url_Main = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
		url_xx1 = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={bvid}"
	if P_flag[3]: print(f"[Info]: {bvid}|{avid}")
	flag_debug(pflag=P_flag)
	# ================================ 视频信息（全部）
	ARR_json_Resp_name = ["0", "Video", "INFO", "json", bvid]
	json_Resp = Downloader(url_DL=url_Main, str_s=ARR_json_Resp_name)
	if P_flag[3]: print(f"[Info]: 1")
	threading.Thread(dump_Data(str_s=ARR_json_Resp_name, data=bytes(json.dumps(json.loads(json_Resp), ensure_ascii=False, separators=(",", ":"), indent="\t"), encoding="utf-8"))).start()
	# ================================ 视频信息?
	ARR_Info_Detail_name = ["0", "Video", "INFO_Detail", "json", bvid]
	if P_flag[8]: video_info_detail = '{"data":{"Related":[],"Reply":{"replies":[]}}}'
	else: video_info_detail = Downloader(url_DL=url_xx1, str_s=ARR_Info_Detail_name)
	if P_flag[3]: print(f"[Info]: 2")
	Vid_detail_json = json.loads(video_info_detail)
	Vid_detail_json["data"]["Related"] = []
	Vid_detail_json["data"]["Reply"]["replies"] = []
	# Vid_detail_json["data"]["View"]["ugc_season"]["sections"]=[]
	threading.Thread(dump_Data(str_s=ARR_Info_Detail_name, data=bytes(json.dumps(Vid_detail_json, ensure_ascii=False, separators=(',', ':'), indent="\t"), encoding="utf-8"))).start()
	# ================================ 加载
	Json_Info = json.loads(json_Resp)["data"]
	Main_Title = Json_Info["title"]
	P_Date = str(Json_Info["pubdate"])
	if Main_Title == "": Main_Title = "Fake_MainTitle"
	Num_of_Videos = int(len(Json_Info["pages"]))
	# ================================ bvid aid 检查
	if Json_Info["bvid"] != bvid: print(f"[bvid]: bvid mismatch {Json_Info['bvid']}|{bvid}")
	if Json_Info["aid"] != avid_in: print(f"[avid]: avid mismatch av{Json_Info['aid']}|{avid}")
	# ================================ 字幕
	for subs in Json_Info["subtitle"]["list"]:
		if P_flag[8]: break
		subs_name = ["0", "Subs", f"{subs['id']}_{subs['lan']}", "bcc", bvid]
		threading.Thread(dump_Data(str_s=subs_name, data=Downloader(url_DL=subs["subtitle_url"], str_s=subs_name))).start()
		if P_flag[3]: print(f"[Subtitle]: {bvid}")
	# ================================ 分集处理
	i_for_videos = 0
	for This in Json_Info["pages"]:
		timeB = time.time()
		P_flag[2] = False
		i_for_videos += 1
		NET_count[0] = 0
		cid = str(This["cid"])
		if P_flag[12] and P_flag[1]: break
		Danmaku_Final_Binary = b""
		duration = int(This["duration"])
		Segment_Count = math.ceil(duration/360)
		ARR_Ext_Info = [cid, "BAS", "INFO", "bin", bvid]
		DL_Data_Extra_Info = Downloader(url_DL=f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}', str_s=ARR_Ext_Info)
		if P_flag[3]: print(f"[Special_Danmaku]: P{i_for_videos}")
		ExInfo_Proto = dm_pb2.DmWebViewReply()
		ExInfo_Proto.ParseFromString(DL_Data_Extra_Info)
		ExInfo_Json = json.loads(MessageToJson(ExInfo_Proto, indent=0, ensure_ascii=False))
		threading.Thread(dump_Data(str_s=ARR_Ext_Info, data=DL_Data_Extra_Info)).start()
		if (not P_flag[6]): XML_Write_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>{6000*Segment_Count}</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
		P_Title = str(This["part"])
		if P_Title == "": P_Title = f"P{i_for_videos}"
		print(f"{P_Date}|{bvid}|{avid}|P{i_for_videos}/{Num_of_Videos}|{cid}|{duration}|{math.ceil(duration/360)}|{Main_Title}|{P_Title}")
		if P_Title == Main_Title: P_Title = ""
		File_Name = f"[{P_Date}][{bvid}][{avid}][P{i_for_videos}][{cid}]{Main_Title.replace('_', '＿')}_{P_Title.replace('_', '＿')}".replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"", "＂").rstrip("_")	# \/:*?"<>|
		# [1656432000][BV1**4*1*7*][av*********][P*][cid]MainTitle_P-Title
		if (not P_flag[6]) and P_flag[11]: XML_Write_Data += XML_Special_Process(ExInfo_Proto.commandDms, cid=cid)
		if P_flag[9]:
			BAS_danmaku = get_Special_Danmaku(ExInfo_Proto)
			xml_t1 = dm_pb2.DmSegMobileReply()
			xml_t1.ParseFromString(BAS_danmaku)
			if (not P_flag[6]): XML_Write_Data += XML_Process(xml_t1.elems)
			Danmaku_Final_Binary += BAS_danmaku
		# 弹幕分段下载
		sec_c: int = 1
		for segments in range(Segment_Count):
			if P_flag[12] and P_flag[1]: break
			try: Danmaku_Binarys = get_Danmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: Danmaku_Binarys = b""
			# 重试
			if len(Danmaku_Binarys) < 4096 and (not P_flag[8]):
				temp_filelen = len(Danmaku_Binarys)
				retry_file = []
				for retry_i in range(3):
					if len(Danmaku_Binarys) == 0: break
					if P_flag[3]: print(f"[retry]: {segments+1} [{retry_i+1}]")
					try: retry_file.append(get_Danmaku(cid, str(segments+1), retry=f"_R{retry_i+1}"))
					except json.decoder.JSONDecodeError: retry_file.append(b"")
					if len(retry_file[retry_i]) > temp_filelen:
						Danmaku_Binarys = retry_file[retry_i]
						del retry_file, temp_filelen
						break
			Danmaku_Final_Binary += Danmaku_Binarys
			if (not P_flag[6]):
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_Binarys)
				XML_Write_Data += XML_Process(xml_t1.elems)
			if (not P_flag[3]): print(f"[{cid}]: {sec_c}/{Segment_Count}\r", end="")
			sec_c += 1
			if P_flag[3]: print(f"[danmaku]: P{i_for_videos}/{Num_of_Videos}::{segments+1}/{Segment_Count}")
		if (not P_flag[3]): print("                      \r", end="")
		if Segment_Count != 1: dump_Data(str_s=[cid, "Danmaku", "ALL", "bin", bvid], data=Danmaku_Final_Binary, force=True)
		timeC = time.time()
		if (not P_flag[5]):
			if P_flag[3]: print(f"[File_JSON P{i_for_videos}]: PROC start")
			Temp_Binary = dm_pb2.DmSegMobileReply()
			Temp_Binary.ParseFromString(Danmaku_Final_Binary)
			j1 = json.loads(MessageToJson(Temp_Binary, indent=0, ensure_ascii=False))
			# ==================
			P_flag[13] = False
			try:
				j1["elems"]
				P_flag[13] = True
			except KeyError: pass
			if P_flag[13]:
				for temp_Del in j1["elems"]:
					try: del temp_Del["idStr"]
					except KeyError: pass
					try:
						if temp_Del["test20"] == "0": del temp_Del["test20"]
					except KeyError: pass
					try:
						if temp_Del["test21"] == "0": del temp_Del["test21"]
					except KeyError: pass
					try:
						if temp_Del["attr"] == 2:
							P_flag[2] = True
							try: del temp_Del["likes"]
							except KeyError: pass
							try:
								if temp_Del["mode"] == 1: del temp_Del["mode"]
							except KeyError: pass
							try:
								if temp_Del["fontsize"] == 25: del temp_Del["fontsize"]
							except KeyError: pass
							try:
								if temp_Del["color"] == 16777215: del temp_Del["color"]
							except KeyError: pass
							try: del temp_Del["weight"]
							except KeyError: pass
					except KeyError: pass
			del P_flag[13]
			# ==================
			del Temp_Binary
			if 1:
				if P_flag[8]:
					try: xx = json.loads(open(f"{File_Name}.json", "r", encoding="utf-8"))["info"]["File_Create_Time"]
					except: xx = timeC
				try: j1["commandDms"] = ExInfo_Json["commandDms"]
				except KeyError: j1["commandDms"] = []
				try: Danmaku_Count = len(j1["elems"])
				except KeyError: Danmaku_Count = 0
				j1["info"] = {}
				j1["info"]["owner"] = Json_Info['owner']				# dict get all
				j1["info"]["bvid"] = Json_Info['bvid']					# str  get all
				j1["info"]["avid"] = Json_Info['aid']					# num  get all
				j1["info"]["V_Name"] = Json_Info["title"]				# str  get all
				j1["info"]["pubdate"] = Json_Info['pubdate']			# num  get all unix_timestamp
				j1["info"]["i_ctime"] = Json_Info['ctime']				# num  get all unix_timestamp
				j1["info"]["P_Name"] = This["part"]						# str  get part
				j1["info"]["duration"] = This["duration"]				# num  get part
				j1["info"]["cid"] = This["cid"]							# num  get part
				j1["info"]["segment_count"] = Segment_Count				# num  set
				j1["info"]["danmaku_count"] = Danmaku_Count				# num  set
				j1["info"]["danmaku_web_reported"] = Json_Info['stat']['danmaku']	# num get
				j1["info"]["danmaku_proto_reported"] = ExInfo_Proto.count	# num get
				j1["info"]["File_Create_Time"] = int(timeC)				# num  set unix_timestamp
				j1["info"]["is_live_record"] = P_flag[2]		# bool GET
				j1["File_Ver"] = "V3_20220819"
			Json_Write_Data = json.dumps(j1, ensure_ascii=False, separators=(',', ':')).replace("},{\"id\"", "},\n{\"id\"")
			del j1
			if P_flag[3]: print(f"[File_JSON P{i_for_videos}]: PROC end--")
		if P_flag[12]: err_sign = "ERR_"
		if (not P_flag[5]):
			if P_flag[12] or P_flag[3]: print(f"[File_JSON P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.json", Json_Write_Data, gz=P_flag[10])
			del Json_Write_Data
		if (not P_flag[6]):
			if P_flag[12] or P_flag[3]: print(f"[File_XML_ P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.xml", XML_Write_Data + f"</i>\n<!-- Create Time: {str(int(timeC))} -->")
			del XML_Write_Data
		del ExInfo_Proto, ExInfo_Json, DL_Data_Extra_Info, Danmaku_Final_Binary
		timeD = time.time()
		if P_flag[0] or P_flag[3]: print(f"P{i_for_videos}: {round(timeD-timeB, 3)}，Wait: {round(NET_count[0]*SLEEP_TIME, 2)}，Net: {NET_count[0]}")
	# ================================ 结束
	if P_flag[12] or P_flag[0] or P_flag[3]:
		timeE = time.time()
		print(f"{bvid}|{avid} Time: {round(timeE-timeA, 3)} Net: {NET_count[1]} Wait: {round(NET_count[1]*SLEEP_TIME, 2)} SLEEP: {SLEEP_TIME}")
