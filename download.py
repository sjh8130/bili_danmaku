#!/usr/bin/python3
# 系统十分稳定，所有代码不要随便动.JPG
from google.protobuf.json_format import MessageToJson
import requests

import binascii
import math
import time
import json
import sys

try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

from my_lib.proto2xml_Lib import proto2xml
from my_lib.bvav import BV_to_AV, AV_to_BV
from my_lib.file_writer import writeE

headers = {
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
	'origin': "https://www.bilibili.com",
	'referer': "https://www.bilibili.com"
}
SLEEP_TIME = 0.03
NET_count = 0
NET_count_all = 0
err_sign = ""


def Program_FLAG(flag: str) -> None:
	"""
	Text
	"""
	if flag == "-1": return
	if flag.find("0b") == 0: b = flag
	else: b = bin(int(flag))
	b = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" + b.lstrip("0b")
	global flag_Timer
	global flag_Error_Stop
	global flag_Many_Logs
	global flag_Ext_XML_Data
	global flag_NO_Json
	global flag_NO_XML
	global flag_Dump_Binary
	global flag_Test_Run
	global flag_spec_danmaku_1
	global flag_gzip
	global flag_spec_danmaku_2
	global flag_13
	if b[-1 ] == "1": flag_Timer = True
	if b[-2 ] == "1": flag_Error_Stop = True
	if b[-4 ] == "1": flag_Many_Logs = True
	if b[-5 ] == "1": flag_Ext_XML_Data = True
	if b[-6 ] == "1": flag_NO_Json = True
	if b[-7 ] == "1": flag_NO_XML = True
	if b[-8 ] == "1": flag_Dump_Binary = True
	if b[-9 ] == "1": flag_Test_Run = True
	if b[-1 ] == "0": flag_Timer = False
	if b[-2 ] == "0": flag_Error_Stop = False
	if b[-4 ] == "0": flag_Many_Logs = False
	if b[-5 ] == "0": flag_Ext_XML_Data = False
	if b[-6 ] == "0": flag_NO_Json = False
	if b[-7 ] == "0": flag_NO_XML = False
	if b[-8 ] == "0": flag_Dump_Binary = False
	if b[-9 ] == "0": flag_Test_Run = False

	if b[-10] == "1": flag_spec_danmaku_1 = True
	if b[-11] == "1": flag_gzip = True
	if b[-12] == "1": flag_spec_danmaku_2 = True
	if b[-13] == "1": flag_13 = True

	if b[-10] == "0": flag_spec_danmaku_1 = False
	if b[-11] == "0": flag_gzip = False
	if b[-12] == "0": flag_spec_danmaku_2 = False
	if b[-13] == "0": flag_13 = False
	if flag_Many_Logs: print(f"[FLAG]: {b}")


def Downloader(url_Real_DL: str) -> bytes:
	"""
	Text
	"""
	global NET_count_all
	global NET_count
	NET_count_all += 1
	NET_count += 1
	if flag_Many_Logs: print(f"[NET]: {url_Real_DL}\t{NET_count_all}   ", end="\t")
	time.sleep(SLEEP_TIME)
	DL_Data = requests.get(url_Real_DL, headers=headers)
	try:
		DL_Json_code = json.loads(DL_Data.content)["code"]
		if DL_Json_code != 0:
			global is_ERROR
			is_ERROR = True
	except UnicodeDecodeError: DL_Json_code = 0
	if flag_Many_Logs or DL_Json_code != 0 or DL_Data.status_code != 200: print(f"[NET]: HTTP {DL_Data.status_code}, Json Code {DL_Json_code}", end="\t")
	return DL_Data.content


def FAKE_Downloader(str_s: dict, url_Fake_DL: str) -> bytes:
	"""
	Text
	"""
	global NET_count_all
	global NET_count
	NET_count_all += 1
	NET_count += 1
	if flag_Many_Logs: print(f"[NET]? {url_Fake_DL}|{NET_count_all}   ", end="\t")
	try:
		DL_Data = open(f"[{bvid}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].bin", "rb").read()
		Fake_status_code = 200
	except FileNotFoundError:
		DL_Data = b""
		Fake_status_code = 404
	try: DL_Json_code = json.loads(DL_Data)["code"]
	except UnicodeDecodeError: DL_Json_code = 0
	except json.decoder.JSONDecodeError:
		if Fake_status_code == 404: DL_Json_code = 404
	if flag_Many_Logs or DL_Json_code != 0 or Fake_status_code != 200: print(f"[NET]? File {Fake_status_code}, Json Code {DL_Json_code}", end="\t")
	return DL_Data


def get_Danmaku(cid: str, Segment_Index: str) -> bytes:
	"""
	Text
	"""
	URL_Danmaku = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={Segment_Index}'
	if flag_Test_Run: Content = FAKE_Downloader([cid, "Danmaku", Segment_Index], url_Fake_DL=URL_Danmaku)
	else: Content = Downloader(URL_Danmaku)
	if is_ERROR and flag_Error_Stop or len(Content) <= 10: return b""
	dump_Data(str0=cid, str1="Danmaku", str2=Segment_Index, data=Content)
	return Content


def get_Special_Danmaku() -> bytes:
	"""
	Text
	"""
	BAS_Binary = b""
	i_for_BAS = 1
	for URL_special_dms in ExInfo_Proto.special_dms:
		if flag_Test_Run: BAS_Data = FAKE_Downloader([cid, "BAS", f"{i_for_BAS}"], url_Fake_DL=URL_special_dms)
		else: BAS_Data = Downloader(URL_special_dms)
		if flag_Many_Logs: print(f"[BAS_DL]: DL {i_for_BAS}")
		if is_ERROR and flag_Error_Stop: break
		BAS_Binary += BAS_Data
		dump_Data(str0=cid, str1="BAS", str2=f"{i_for_BAS}", data=BAS_Data)
		i_for_BAS += 1
	return BAS_Binary


def XML_Process(data) -> str:
	"""
	Text
	"""
	this: dm_pb2.DanmakuElem
	out0 = ""
	for this in data: out0 += proto2xml(this, exdata=flag_Ext_XML_Data, enable_weight=True, All_Default=flag_13)
	return out0


def XML_Special_Process(data, cid) -> str:
	"""
	Text
	"""
	this: dm_pb2.CommandDm
	out1 = ""
	for this in data:
		Ex_Extra_Data = ""
		id_ = this.id				# int64 id = 1
		oid = this.oid				# int64 oid = 2;
		mid = this.mid				# int64 mid = 3;
		command = this.command		# string command = 4;
		content = this.content		# string content = 5;
		progress = this.progress	# int32 progress = 6;
		ctime = this.ctime			# string ctime = 7;
		mtime = this.mtime			# string mtime = 8;
		extra = this.extra			# string extra = 9;
		idStr = this.idStr			# string idStr = 10
		if str(id_) != idStr: print("[XML_SP]: id&idStr mismatch:", id_, idStr)
		if flag_Ext_XML_Data: Ex_Extra_Data = f"<!-- SPECIAL: {command}{extra} -->"
		out1 += f"\t<d p=\"{format(progress/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(ctime, '%Y-%m-%d %H:%M:%S')))},999,{hex(binascii.crc32(str(mid).encode()) ^ 0xFFFFFFFF).lstrip('0x').lstrip('0')},{id_},11\">{content}</d>{Ex_Extra_Data}\n"
	return out1


def dump_Data(str0: str, str1: str, str2: str, data: bytes, force: bool = False) -> None:
	"""
	Text
	"""
	if flag_Dump_Binary and ((not flag_Test_Run) or force): pass
	else: return
	if len(data) == 0: return
	writeE(f"[{bvid}]_[{str0}]_[{str1}]_[{str2}].bin", data, False, True)


if __name__ == '__main__':
	开始时间 = time.time()
	# print(sys.argv)
	# ================================ 程序设置
	is_ERROR = False
	flag_Timer = True			# 计时器
	flag_Error_Stop = True		# 错误停机
	flag_Many_Logs = False		# 日志
	flag_Ext_XML_Data = False	# 输出 其他信息到 XML 文件
	flag_NO_Json = False		# 不输出 Json
	flag_NO_XML = False			# 不输出 XML
	flag_Dump_Binary = False	# 输出 Protobuf 二进制文件
	flag_Test_Run = False		# 模拟运行
	flag_spec_danmaku_1 = True	# 特殊弹幕:BAS
	flag_gzip = False			# 压缩为gzip
	flag_spec_danmaku_2 = True	# 特殊弹幕:UP主自定义内容
	flag_13 = False				# flag_13
	try: Program_FLAG(sys.argv[2])
	except IndexError: pass
	if flag_Test_Run: print("[Test Run]: ================================ ")
	# ================================ 终端输入
	try: vid = sys.argv[1]
	except IndexError:
		print("""download.py av|bv [flag]

.3.........2.........1..........
10987654321098765432109876543210
_______________________________1    1 计时器
______________________________1_    2 错误停机
_____________________________1__    4 X
____________________________1___    8 日志
___________________________1____   16 输出其他信息到XML文件
__________________________1_____   32 不输出Json
_________________________1______   64 不输出XML
________________________1_______  128 输出Protobuf二进制文件
_______________________1________  256 模拟运行
______________________1_________  512 特殊弹幕_BAS
_____________________1__________ 1024 压缩json到gzip
____________________1___________ 2048 特殊弹幕_UP主自定义内容
___________________1____________ 4096 Text1234567890
""")
		sys.exit()
	if flag_NO_Json and flag_NO_XML and (not flag_Dump_Binary):
		print("?????????")
		sys.exit(999)
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
	if flag_Many_Logs: print(f"[Info]: {bvid}|{avid}")
	# ================================ 视频信息（全部）
	if flag_Test_Run: json_Resp = FAKE_Downloader(["0", "Video", "INFO"], url_Fake_DL=url_Main)
	else: json_Resp = Downloader(url_Main)
	if flag_Many_Logs: print(f"[Info]: 1")
	writeE(filename = f"[{bvid}]_[0]_[Video]_[INFO].bin", data=json_Resp, binary_=True)
	if is_ERROR and flag_Error_Stop:
		print(f"\n[{bvid}|{avid}]Error: {json.loads(json_Resp)['message']}")
		print("总计用时:", round(time.time()-开始时间, 3))
		sys.exit(1)
	# ================================ 视频信息?
	if 1:
		if flag_Test_Run: video_info_detail = FAKE_Downloader(["0", "Video", "INFO_Detail"], url_Fake_DL=url_xx1)
		else: video_info_detail = Downloader(url_xx1)
		if flag_Many_Logs: print(f"[Info]: 2")
		Vid_detail_json = json.loads(video_info_detail)
		Vid_detail_json["data"]["Related"]=[]
		Vid_detail_json["data"]["Reply"]["replies"]=[]
		# Vid_detail_json["data"]["View"]["ugc_season"]["sections"]=[]
		writeE(filename = f"[{bvid}]_[0]_[Video]_[INFO_Detail].bin", data=json.dumps(Vid_detail_json, ensure_ascii=False))
		del video_info_detail
		del Vid_detail_json
	del url_xx1
	# ================================ 加载
	Json_Info = json.loads(json_Resp)["data"]
	Item = Json_Info["pages"]
	Main_Title = Json_Info["title"]
	P_Date = str(Json_Info["pubdate"])
	if Main_Title == "": Main_Title = "Fake_MainTitle"
	Num_of_Videos = int(len(Item))
	# ================================ bvid aid int32 检查
	if Json_Info["bvid"] != bvid: print(f"[bvid]: bvid mismatch {Json_Info['bvid']}|{bvid}")
	if Json_Info["aid"] != avid_in: print(f"[avid]: avid mismatch av{Json_Info['aid']}|{avid}")
	# ================================ 分集处理
	for i in range(Num_of_Videos):
		NET_count = 0
		This = Item[i]
		cid = str(This["cid"])
		if is_ERROR and flag_Error_Stop: break
		分P开始时间 = time.time()
		Danmaku_Final_Binary = b""
		duration = int(This["duration"])
		Segment_Count = math.ceil(duration/360)
		URL_Ext = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}'
		if flag_Test_Run: DL_Data_Extra_Info = FAKE_Downloader([cid, "BAS", "INFO"], url_Fake_DL=URL_Ext)
		else: DL_Data_Extra_Info = Downloader(URL_Ext)
		if flag_Many_Logs: print(f"[Special_Danmaku]: P{i+1}")
		ExInfo_Proto = dm_pb2.DmWebViewReply()
		ExInfo_Proto.ParseFromString(DL_Data_Extra_Info)
		ExInfo_Json = json.loads(MessageToJson(ExInfo_Proto, indent=0, ensure_ascii=False))
		dump_Data(str0=cid, str1="BAS", str2="Info", data=DL_Data_Extra_Info)
		# if Extra_Info_Proto.dm_sge.page_size != 360000: print(f"[Segments_Split_Size P{i+1}]:err 360|{Extra_Info_Proto.dm_sge.page_size}")
		# if Segment_Count != Extra_Info_Proto.dm_sge.total: print(f"[Segments_calc P{i+1}]:err {Segment_Count}|{Extra_Info_Proto.dm_sge.total}")
		if (not flag_NO_XML): XML_Write_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>{6000*Segment_Count}</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
		P_Title = str(This["part"])
		if P_Title == "": P_Title = f"P{i+1}"
		print(f"{P_Date}|{bvid}|{avid}|P{i+1}/{Num_of_Videos}|{cid}|{duration}|{math.ceil(duration/360)}|{Main_Title}|{P_Title}")
		File_Name = f"[{P_Date}][{bvid}][{avid}][P{i+1}][{cid}]{Main_Title.replace('_', '＿')}_{P_Title.replace('_', '＿')}".replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"", "＂").rstrip("_")	# \/:*?"<>|
		# [1656432000][BV1**4*1*7*][av*********][P*][cid]MainTitle_P-Title
		XML_Time = 0
		BAS开始时间 = XML_Ti = time.time()
		if (not flag_NO_XML) and flag_spec_danmaku_2: XML_Write_Data += XML_Special_Process(ExInfo_Proto.commandDms, cid=cid)
		if flag_spec_danmaku_1:
			BAS_danmaku = get_Special_Danmaku()
			xml_t1 = dm_pb2.DmSegMobileReply()
			xml_t1.ParseFromString(BAS_danmaku)
			if (not flag_NO_XML): XML_Write_Data += XML_Process(xml_t1.elems)
			Danmaku_Final_Binary += BAS_danmaku
		XML_Tim = BAS结束时间 = time.time()
		XML_Time += XML_Tim - XML_Ti
		sec_c: int = 1
		for segments in range(Segment_Count):
			if is_ERROR and flag_Error_Stop: break
			try: Danmaku_Binarys = get_Danmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: Danmaku_Binarys = b""
			Danmaku_Final_Binary += Danmaku_Binarys
			if (not flag_NO_XML):
				XML_Ti = time.time()
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_Binarys)
				XML_Write_Data += XML_Process(xml_t1.elems)
				XML_Tim = time.time()
				XML_Time += XML_Tim - XML_Ti
			if (not flag_Many_Logs): print(f"[{cid}]: {sec_c}/{Segment_Count}\r", end="")
			sec_c += 1
			if flag_Many_Logs: print(f"[danmaku]: P{i+1}/{Num_of_Videos}::{segments+1}/{Segment_Count}")
			else: print("                      \r", end="")
		dump_Data(str0=cid, str1="Danmaku", str2="ALL", data=Danmaku_Final_Binary, force=True)
		JSON_Time = time.time()
		if (not flag_NO_Json):
			if flag_Many_Logs: print(f"[File_JSON P{i+1}]: PROC start")
			Temp_Binary = dm_pb2.DmSegMobileReply()
			Temp_Binary.ParseFromString(Danmaku_Final_Binary)
			j1 = json.loads(MessageToJson(Temp_Binary, indent=0, ensure_ascii=False))
			del Temp_Binary
			if 1:
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
				j1["info"]["segment_count_proto_reported"] = ExInfo_Proto.dm_sge.total	# num  get
				j1["info"]["danmaku_count"] = Danmaku_Count + len(ExInfo_Proto.commandDms)	# num  set
				j1["info"]["danmaku_web_reported"] = Json_Info['stat']['danmaku']	# num get
				j1["info"]["danmaku_proto_reported"] = ExInfo_Proto.count	# num get 100?
				j1["info"]["File_Create_Time"] = int(JSON_Time)			# num  set unix_timestamp
				j1["info"]["All_Default"] = flag_13
				j1["File_Ver"] = "V1_20220816"
			Json_Write_Data = json.dumps(j1, ensure_ascii=False).replace("}, {\"id\"", "},\n{\"id\"").replace(", \"test20\": \"0\", \"test21\": \"0\"", "")
			del j1
			if flag_Many_Logs: print(f"[File_JSON P{i+1}]: PROC end--")
		if is_ERROR: err_sign = "ERR_"
		写入开始时间 = time.time()
		if (not flag_NO_Json):
			if is_ERROR or flag_Many_Logs: print(f"[File_JSON P{i+1}]: 开始写入")
			writeE(f"{err_sign}{File_Name}.json", Json_Write_Data, gz=flag_gzip)
			del Json_Write_Data
		Time_Point_ = time.time()
		if (not flag_NO_XML):
			if is_ERROR or flag_Many_Logs: print(f"[File_XML  P{i+1}]: 开始写入")
			writeE(f"{err_sign}{File_Name}.xml", XML_Write_Data + f"</i>\n<!-- Create Time: {str(int(JSON_Time))} -->")
			del XML_Write_Data
		del ExInfo_Proto
		del ExInfo_Json
		del DL_Data_Extra_Info
		del Danmaku_Final_Binary
		分P结束时间 = time.time()
		if flag_Timer or flag_Many_Logs: print(f"P{i+1}: {round(分P结束时间-分P开始时间, 3)}，BAS: {round(BAS结束时间-BAS开始时间, 3)}，Write: {round(分P结束时间-写入开始时间, 3)}，JSON: {round(写入开始时间-JSON_Time, 3)}，XML: {round(分P结束时间-Time_Point_, 3)}，XML_P: {round(XML_Time, 3)}，Wait: {round(NET_count*SLEEP_TIME, 2)}，Net: {NET_count}")
	if is_ERROR or flag_Timer or flag_Many_Logs:
		结束时间 = time.time()
		print(f"{bvid}|{avid} Time: {round(结束时间-开始时间, 3)} Net: {NET_count_all} Wait: {round(NET_count_all*SLEEP_TIME, 2)} SLEEP: {SLEEP_TIME}")
	sys.exit(0)

# 1745 dump,noxml,timer,bas
# , "likes": \d{1,}\},
# "weight": \d{1,2}, 
