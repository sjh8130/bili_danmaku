#!/usr/bin/python3
# 系统十分稳定，所有代码不要随便动.JPG
import binascii
from google.protobuf.json_format import MessageToJson
from tqdm import tqdm
import requests

try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2

import math
import time
import json
import sys
import io
import gzip

headers = {
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44",
	'origin': "https://www.bilibili.com",
	'referer': "https://www.bilibili.com"
	}
SLEEP_TIME = 0.75
BV_AV_table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
BV_AV_base58_dic = {}
for BV_AV_base58_i in range(58): BV_AV_base58_dic[BV_AV_table[BV_AV_base58_i]] = BV_AV_base58_i
s = [11, 10, 3, 8, 4, 6]
BV_AV_xor = 177451812
BV_AV_add = 8728348608
NET_count = -1
NET_count_all = 0
err_sign = ""

def Program_FLAG(flag: str):
	if flag == "-1": return
	if flag.find("0b") == 0: b = flag
	else: b = bin(int(flag))
	b = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" + b.lstrip("0b")
	global flag_Timer
	global flag_Error_Stop
	global flag_Zero_Stop
	global flag_Many_Logs
	global flag_Ext_XML_Data
	global flag_NO_Json
	global flag_NO_XML
	global flag_Dump_Binary
	global flag_Test_Run
	global flag_BAS
	global flag_gzip
	if b[-1 ] == "1": flag_Timer = True
	if b[-2 ] == "1": flag_Error_Stop = True
	if b[-3 ] == "1": flag_Zero_Stop = True
	if b[-4 ] == "1": flag_Many_Logs = True
	if b[-5 ] == "1": flag_Ext_XML_Data = True
	if b[-6 ] == "1": flag_NO_Json = True
	if b[-7 ] == "1": flag_NO_XML = True
	if b[-8 ] == "1": flag_Dump_Binary = True
	if b[-9 ] == "1": flag_Test_Run = True
	if b[-1 ] == "0": flag_Timer = False
	if b[-2 ] == "0": flag_Error_Stop = False
	if b[-3 ] == "0": flag_Zero_Stop = False
	if b[-4 ] == "0": flag_Many_Logs = False
	if b[-5 ] == "0": flag_Ext_XML_Data = False
	if b[-6 ] == "0": flag_NO_Json = False
	if b[-7 ] == "0": flag_NO_XML = False
	if b[-8 ] == "0": flag_Dump_Binary = False
	if b[-9 ] == "0": flag_Test_Run = False

	# if b[-10] == "1": flag_BAS = True
	if b[-11] == "1": flag_gzip = True
	# if b[-10] == "0": flag_BAS = False
	if b[-11] == "0": flag_gzip = False
	if flag_Many_Logs: print(f"[FLAG]: {b}")


def Danmaku_ATTR_TYPE(attr: int):
	global flag_Ext_XML_Data
	if (not flag_Ext_XML_Data): return ""
	if attr == 0: return "DM "
	o = ""
	b = "00000000000000000000000000000000" + bin(attr).lstrip("0b")
	if b[-1 ] == "1": o += "保护 "	# 1
	if b[-2 ] == "1": o += "直播 "	# 2
	if b[-3 ] == "1": o += "高赞 "	# 4
	if b[-4 ] == "1": o += "壹 "	# 8
	if b[-5 ] == "1": o += "贰 "	# 16 硬核会员 不显示？
	if b[-6 ] == "1": o += "叁 "	# 32
	if b[-7 ] == "1": o += "肆 "	# 64 硬核会员 不显示？
	if b[-8 ] == "1": o += "伍 "	# 128
	if b[-9 ] == "1": o += "陆 "	# 256
	if b[-10] == "1": o += "柒 "	# 512
	if b[-11] == "1": o += "捌 "	# 1024
	if b[-12] == "1": o += "玖 "	# 2048
	if b[-13] == "1": o += "拾 "	# 4096
	if b[-14] == "1": o += "拾壹 "	# 8192
	return o


def BV_to_AV(input_BV: str):
	result = 0
	for i in range(6): result += BV_AV_base58_dic[input_BV[s[i]]]*58**i
	out = (result-BV_AV_add) ^ BV_AV_xor
	if out <= 0:
		print("[BV_to_AV]: invaild avid")
	return out


def AV_to_BV(input_AV: int):
	if input_AV > 2147483647:
		print("[AV_to_BV]: avid is too big")
	input_AV = (input_AV ^ BV_AV_xor)+BV_AV_add
	result = list('BV1  4 1 7  ')
	for i in range(6): result[s[i]] = BV_AV_table[input_AV//58**i % 58]
	return ''.join(result)


def Downloader(url_DL: str):
	if flag_Many_Logs: print(f"[NET]: {url_DL}", end="\t")
	time.sleep(SLEEP_TIME)
	DL_Data = requests.get(url_DL, headers=headers)
	global NET_count
	NET_count += 1
	global NET_count_all
	NET_count_all += 1
	try:
		Status_Code = json.loads(DL_Data.content)["code"]
		if Status_Code != 0:
			global is_ERROR
			is_ERROR = True
	except UnicodeDecodeError: Status_Code = 0
	if flag_Many_Logs or Status_Code != 0 or DL_Data.status_code != 200: print(f"[NET]: HTTP {DL_Data.status_code}, Json Code {Status_Code}", end="\t")
	return DL_Data.content


def FAKE_Downloader(str0: str, str1: str, str2: str, url_Fake_DL: str):
	if flag_Many_Logs: print(f"[NET]? {url_Fake_DL}     ", end="\t")
	try:
		resp = open(f"[{bvid}]_[{str0}]_[{str1}]_[{str2}].bin", "rb").read()
		Fake_status_code = 200
	except FileNotFoundError:
		resp = b""
		Fake_status_code = 404
	global NET_count
	NET_count += 1
	global NET_count_all
	NET_count_all += 1
	try: status_code = json.loads(resp)["code"]
	except UnicodeDecodeError: status_code = 0
	except json.decoder.JSONDecodeError:
		if Fake_status_code == 404: status_code = 404
	if flag_Many_Logs or status_code != 0 or Fake_status_code != 200: print(f"[NET]? File {Fake_status_code}, Json Code {status_code}", end="\t")
	return resp


def get_Danmaku(cid: str, Segment_Index: str):
	URL_Danmaku = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={Segment_Index}'
	if flag_Test_Run: Content = FAKE_Downloader(str0=cid, str1="Danmaku", str2=Segment_Index, url_Fake_DL=URL_Danmaku)
	else: Content = Downloader(URL_Danmaku)
	dump_Data(str0=cid, str1="Danmaku", str2=Segment_Index, data=Content)
	if is_ERROR and flag_Error_Stop: return b""
	return Content


def get_Special_Danmaku():
	try: special_dms_List = BAS_Info_Json["specialDms"]
	except KeyError:
		if flag_Many_Logs: print(f"[BAS P{i+1}]: No BAS Danmaku")
		return b""
	BAS_Binary = b""
	k = 1
	for URL_special_dms in special_dms_List:
		if flag_Test_Run: BAS_Data = FAKE_Downloader(str0=cid, str1="BAS", str2=f"{k}", url_Fake_DL=URL_special_dms)
		else: BAS_Data = Downloader(URL_special_dms)

		if flag_Many_Logs: print("[BAS_DL]: DL")
		if is_ERROR and flag_Error_Stop: break
		BAS_Binary += BAS_Data
		dump_Data(str0=cid, str1="BAS", str2=f"{k}", data=BAS_Data)
		k += 1
	return BAS_Binary


def XML_Process(data):
	if data == "{}": return ""
	jsonData = json.loads(data)
	XML_Data_2nd = ""
	for Item_nr in jsonData["elems"]:
		testing_1 = None	# unused!Testing
		Extended_Data = ""
		try: id_ = Item_nr["id"]									# int64 id = 1;
		except KeyError: id_ = "0"

		try: progress = Item_nr["progress"]						# int32 progress = 2;
		except KeyError: progress = 0

		try: mode = Item_nr["mode"]								# int32 mode = 3;
		except KeyError: mode = "1"
		# 1/2!/3!:regular	4:buttom	5:top	6:reverse!	7:advance	8:code	9:BAS	10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31

		try: fontsize = Item_nr["fontsize"]						# int32 fontsize = 4;
		except KeyError: fontsize = "25"
		# 18/25/36

		try: color = Item_nr["color"]								# uint32 color = 5;
		except KeyError: color = "0"

		try: midHash = Item_nr["midHash"]							# string midHash = 6;
		except KeyError: midHash = "ffffffff"

		try: content = Item_nr["content"]							# string content = 7;
		except KeyError: content = ""

		try: sendtime = Item_nr["ctime"]							# int64 ctime = 8;
		except KeyError: sendtime = "1262275200"

		try: weight = Item_nr["weight"]							# int32 weight = 9;
		except KeyError: weight = "9"

		try: pool = Item_nr["pool"]								# int32 pool = 11;
		except KeyError: pool = "0"
		# 0:regular	1:subtitle	2:special(BAS/code)

		try: idStr = Item_nr["idStr"]								# string idStr = 12;
		except KeyError: idStr = "0"

		if id_ != idStr: print("\n [XML]: id&idStr mismatch:", id_, idStr)

		if flag_Ext_XML_Data:
			try: action = Item_nr["action"]						# string action = 10;
			except KeyError: pass

			try: attr = Danmaku_ATTR_TYPE(Item_nr["attr"])			# int32 attr = 13;
			except KeyError: attr = "DM "

			try: usermid = f"mid:{Item_nr['usermid']} "			# int usermid = 14;
			except KeyError: usermid = ""

			try: likes = f"Likes: {Item_nr['likes']} "				# int likes = 15;
			except KeyError: likes = ""

			try: replyCount = f"Reply: {Item_nr['replyCount']} "	# int replyCount = 18;
			except KeyError: replyCount = ""

			try: animation = Item_nr["animation"]					# string animation = 22;
			except KeyError: pass

			Extended_Data = f"<!-- {attr}{usermid}{likes}{replyCount} -->".replace("  ", " ")

		try:	# TESTING
			testing_1 = Item_nr["test19"]
			print(f"[XML]: {id_} Have 19!!!!!!!!!!!")
		except: pass

		try:	# TESTING
			testing_1 = Item_nr["test23"]
			print(f"[XML]: {id_} Have 23!!!!!!!!!!!")
		except: pass

		content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
		progress = format(progress/1000, ".5f")

		# XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}\x0a".format(progress, mode, fontsize, color, sendtime, pool, midHash, id_, weight, content, spec_tag)
		XML_item = f"\t<d p=\"{progress},{mode},{fontsize},{color},{sendtime},{pool},{midHash},{id_},{weight}\">{content}</d>{Extended_Data}\x0a"
		XML_Data_2nd += XML_item
		Item_nr = {}
	return XML_Data_2nd


def XML_Special_Process(data):
	# return ""
	XML_Spec_Data = ""
	for Item_sp in data:
		id_ = Item_sp["id"]					# int64 id = 1
		oid = Item_sp["oid"]				# int64 oid = 2;
		mid = Item_sp['mid']				# int64 mid = 3;
		command = Item_sp["command"]		# string command = 4;
		content = Item_sp["content"]		# string content = 5;
		progress = Item_sp["progress"]		# int32 progress = 6;
		ctime = Item_sp["ctime"]			# string ctime = 7;
		mtime = Item_sp["mtime"]			# string mtime = 8;
		extra = Item_sp["extra"]			# string extra = 9;
		idStr = Item_sp["idStr"]			# string idStr = 10

		progress = format(progress/1000, ".5f")
		mode = "1"
		fontsize = "25"
		color = "16777215"
		sendtime = int(time.mktime(time.strptime(ctime, '%Y-%m-%d %H:%M:%S')))
		pool = "999"	# 
		midHash = hex(binascii.crc32(mid.encode())^0xFFFFFFFF).lstrip("0x").lstrip("0")
		weight = "11"

		spec_tag = f"<!-- SPECIAL: {command}{extra} -->"
		XML_item = f"\t<d p=\"{progress},{mode},{fontsize},{color},{sendtime},{pool},{midHash},{id_},{weight}\">{content}</d>{spec_tag}\x0a"
		XML_Spec_Data += XML_item
	return XML_Spec_Data


def dump_Data(str0: str, str1: str, str2: str, data: bin, force: bool = False):
	if flag_Dump_Binary and ((not flag_Test_Run) or force): pass
	else: return
	if len(data) == 0: return
	open(f"[{bvid}]_[{str0}]_[{str1}]_[{str2}].bin", "wb").write(data)


if __name__ == '__main__':
	开始时间 = time.time()
	# print(sys.argv)
	is_ERROR = False
	flag_Timer = True			# 计时器
	flag_Error_Stop = False		# 错误停机
	flag_Zero_Stop = False		# 0弹幕停机
	flag_Many_Logs = False		# 日志
	flag_Ext_XML_Data = True	# 输出 其他信息到 XML 文件
	flag_NO_Json = False		# 不输出 Json
	flag_NO_XML = False			# 不输出 XML
	flag_Dump_Binary = False	# 输出 Protobuf 二进制文件
	flag_Test_Run = False		# 模拟运行
	flag_BAS = True
	flag_gzip = True			# 压缩为gzip
	try:
		P_flag = sys.argv[2]
		Program_FLAG(P_flag)
	except IndexError: pass
	if flag_Test_Run: print("[Test Run]: ================================ ")
	vid = sys.argv[1]
	if flag_NO_Json and flag_NO_XML and (not flag_Dump_Binary):
		print("?????????")
		sys.exit(999)
	if vid.find("https://www.bilibili.com/video/") == 0: vid = vid.lstrip("https://www.bilibili.com/video/")
	if vid.find("http://www.bilibili.com/video/") == 0: vid = vid.lstrip("http://www.bilibili.com/video/")
	if vid.find("https://b23.tv/BV1") == 0: vid = vid.lstrip("https://b23.tv/")
	vid = vid.split("?")[0].split("/")[0]
	if vid.find("av") == 0:
		avid = vid
		avid_in = int(avid.lstrip("av"))
		bvid = AV_to_BV(avid_in)
		url_Main = f"https://api.bilibili.com/x/web-interface/view?aid={avid_in}"
	else:
		bvid = vid[0:12]
		avid_in = BV_to_AV(bvid)
		avid = f"av{avid_in}"
		url_Main = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
	if flag_Many_Logs: print(f"[Info]: {bvid}|{avid}")

	if flag_Test_Run: json_Resp = FAKE_Downloader(str0="0", str1="Video", str2="INFO", url_Fake_DL=url_Main)
	else: json_Resp = Downloader(url_Main)

	dump_Data(str0="0", str1="Video", str2="INFO", data=json_Resp)
	if is_ERROR and flag_Error_Stop:
		print(f"[{bvid}|{avid}]Error: {json_Resp}")
		print("总计用时:", round(time.time()-开始时间, 3))
		sys.exit(1)

	Json_Info = json.loads(json_Resp)["data"]
	Item = Json_Info["pages"]
	Main_Title = Json_Info["title"]
	P_Date = str(Json_Info["pubdate"])

	if Json_Info["bvid"] != bvid: print(f"[bvid]: bvid mismatch {Json_Info['bvid']}|{bvid}")
	if Json_Info["aid"] != avid_in: print(f"[avid]: avid mismatch av{Json_Info['aid']}|{avid}")

	if Main_Title == "": Main_Title = "Fake_MainTitle"
	sub_Items_Len = int(len(Item))

	if Json_Info["stat"]["danmaku"] == 0 and flag_Zero_Stop:
		print("No danmaku")
		for i in range(sub_Items_Len):
			duration = int(Item[i]["duration"])
			cid = str(Item[i]["cid"])
			P_Title = str(Item[i]["part"])
			print(f"{P_Date}|{bvid}|{avid}|P{i+1}/{sub_Items_Len}|{cid}|{duration}|{math.ceil(duration/360)}|{Main_Title}|{P_Title}")
		print("总计用时:", round(time.time()-开始时间, 3))
		sys.exit(1)

	for i in range(sub_Items_Len):
		this = Item[i]
		cid = str(this["cid"])
		Danmaku_Count = 0
		if is_ERROR and flag_Error_Stop: break
		分P开始时间 = time.time()
		Danmaku_Final_Binary = b""
		duration = int(this["duration"])
		Segment_Count = math.ceil(duration/360)

		if flag_Many_Logs: print()
		URL_Ext_ = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}'
		if flag_Test_Run: DL_Data_BAS_Info = FAKE_Downloader(str0=cid, str1="BAS", str2="INFO", url_Fake_DL=URL_Ext_)
		else: DL_Data_BAS_Info = Downloader(URL_Ext_)
		BAS_Info_Proto = dm_pb2.DmWebViewReply()
		BAS_Info_Proto.ParseFromString(DL_Data_BAS_Info)
		BAS_Info_Json = json.loads(MessageToJson(BAS_Info_Proto, indent=0, ensure_ascii=False))
		dump_Data(str0=cid, str1="BAS", str2="Info", data=DL_Data_BAS_Info)

		if (not flag_NO_XML): XML_Data_Empty = XML_Write_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\x0a<i>\x0a\t<chatserver>chat.bilibili.com</chatserver>\x0a\t<chatid>{cid}</chatid>\x0a\t<mission>0</mission>\x0a\t<maxlimit>{6000*Segment_Count}</maxlimit>\x0a\t<state>0</state>\x0a\t<real_name>0</real_name>\x0a\t<source>k-v</source>\x0a"
		P_Title = str(this["part"])
		if Main_Title == P_Title: P_Title = f"P{i+1}"
		if flag_Many_Logs: print()
		print(f"{P_Date}|{bvid}|{avid}|P{i+1}/{sub_Items_Len}|{cid}|{duration}|{math.ceil(duration/360)}|{Main_Title}|{P_Title}")
		File_Name = f"[{P_Date}][{bvid}][{avid}][P{i+1}][{cid}]{Main_Title.replace('_', '＿')}_{P_Title.replace('_', '＿')}"
		File_Name = File_Name.replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"", "＂")	# \/:*?"<>|
		# [1656432000][BV1**4*1*7*][av*********][P*][cid]MainTitle_P-Title
		XML_Time = 0

		try: XML_Write_Data += XML_Special_Process(BAS_Info_Json["commandDms"])
		except KeyError: pass

		BAS开始时间 = time.time()
		if flag_BAS:
			BAS_danmaku = get_Special_Danmaku()
			if (not flag_NO_XML):
				XML_Ti = time.time()
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(BAS_danmaku)
				xml_t2 = MessageToJson(xml_t1, indent=0, ensure_ascii=False)
				XML_Write_Data += XML_Process(xml_t2)
				XML_Tim = time.time()
				XML_Time += XML_Tim - XML_Ti
			Danmaku_Final_Binary += BAS_danmaku
		BAS结束时间 = time.time()


		if not flag_Many_Logs: Progress_Bar = tqdm(total=Segment_Count, leave=False, unit='chunks', ascii=True, ncols=100)
		for segments in range(Segment_Count):
			if is_ERROR and flag_Error_Stop: break
			try: Danmaku_Binarys = get_Danmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: Danmaku_Binarys = b""
			Danmaku_Final_Binary += Danmaku_Binarys
			if (not flag_NO_XML):
				XML_Ti = time.time()
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_Binarys)
				XML_Write_Data += XML_Process(MessageToJson(xml_t1, indent=0, ensure_ascii=False))
				XML_Tim = time.time()
				XML_Time += XML_Tim - XML_Ti
			if (not flag_Many_Logs): Progress_Bar.update(1)
			if is_ERROR or flag_Many_Logs: print(f"[danmaku]: P{i+1}/{sub_Items_Len}::{segments+1}/{Segment_Count}")
		if (not flag_Many_Logs):Progress_Bar.close()
		dump_Data(str0=cid, str1="Danmaku", str2="ALL", data=Danmaku_Final_Binary, force=True)
		JSON_Time = time.time()
		if (not flag_NO_Json):
			if flag_Many_Logs: print(f"[File_JSON P{i+1}]: PROC start")
			Temp_Binary = dm_pb2.DmSegMobileReply()
			Temp_Binary.ParseFromString(Danmaku_Final_Binary)
			j1 = json.loads(MessageToJson(Temp_Binary, indent=0, ensure_ascii=False))
			Danmaku_Count = len(j1["elems"])
			Temp_Binary = dm_pb2.DmSegMobileReply()
			if 1:
				j1["info"] = {}
				j1["info"]["owner_name"] = Json_Info['owner']['name']
				j1["info"]["owner_mid"] = Json_Info['owner']['mid']
				j1["info"]["bvid"] = Json_Info['bvid']
				j1["info"]["avid"] = Json_Info['aid']
				j1["info"]["V_Name"] = Main_Title
				j1["info"]["pubdate"] = Json_Info['pubdate']
				j1["info"]["ctime"] = Json_Info['ctime']
				j1["info"]["P_Name"] = P_Title
				j1["info"]["duration"] = duration
				j1["info"]["cid"] = cid
				j1["info"]["segment_count"] = Segment_Count
				j1["info"]["danmaku_count"] = Danmaku_Count
				j1["info"]["danmaku_web_reported"] = Json_Info['stat']['danmaku']
				j1["info"]["File_Create_Time"] = int(time.time())
				try: j1["commandDms"] = BAS_Info_Json["commandDms"]
				except KeyError: j1["commandDms"] = []

			Json_Write_Data = json.dumps(j1, ensure_ascii=False).replace("}, {\"id\"", "},\x0a{\"id\"").replace(", \"test20\": \"0\", \"test21\": \"0\"", "")
			j1 = {}
			if flag_Many_Logs: print(f"[File_JSON P{i+1}]: PROC end--")
		if is_ERROR: err_sign = "ERR"
		写入开始时间 = time.time()
		if (not flag_NO_Json):
			if Json_Write_Data == "{}" or Json_Write_Data == "":
				if is_ERROR or flag_Many_Logs: print(f"[File_JSON P{i+1}]: No Data")
			else:
				if is_ERROR or flag_Many_Logs: print(f"[File_JSON P{i+1}]: 开始写入")
				if flag_gzip: io.TextIOWrapper(gzip.open(f"{err_sign}{File_Name}.json.gz", 'wb', compresslevel=9), encoding='utf-8').writelines(Json_Write_Data)
				else: open(f"{err_sign}{File_Name}.json", "w", encoding="utf-8").write(Json_Write_Data)
				Json_Write_Data = ""
		Time_Point_ = time.time()
		if (not flag_NO_XML):
			if XML_Write_Data == XML_Data_Empty:
				if is_ERROR or flag_Many_Logs: print(f"[File_XML  P{i+1}]: No Data")
			else:
				if is_ERROR or flag_Many_Logs: print(f"[File_XML  P{i+1}]: 开始写入")
				open(f"{err_sign}{File_Name}.xml", "w", encoding="utf-8").write(XML_Write_Data + f"</i>\x0a<!-- Create Time: {str(int(JSON_Time))} -->")
				XML_Write_Data = ""
		else: print()
		Danmaku_Final_Binary = b""

		分P结束时间 = time.time()
		if flag_Timer or flag_Many_Logs: print(f"P{i+1}: {round(分P结束时间-分P开始时间, 3)}，BAS: {round(BAS结束时间-BAS开始时间, 3)}，Write: {round(分P结束时间-写入开始时间, 3)}，JSON: {round(写入开始时间-JSON_Time, 3)}，XML: {round(分P结束时间-Time_Point_, 3)}，XML_P: {round(XML_Time, 3)}，Wait: {round(NET_count*SLEEP_TIME, 2)}，Net: {NET_count}，Danmaku: {Danmaku_Count}")
		NET_count = 0
	if is_ERROR or flag_Timer or flag_Many_Logs:
		结束时间 = time.time()
		print(f"{bvid}|{avid} Time: {round(结束时间-开始时间, 3)} Net: {NET_count_all} Wait: {round(NET_count_all*SLEEP_TIME, 2)} SLEEP: {SLEEP_TIME}")
	sys.exit(0)

# 1745 dump,noxml,timer,bas
# , "likes": \d{1,}\},