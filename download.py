#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson

import requests
import binascii
import math
import time
import json
import sys
import threading

try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

from my_lib.proto2xml_Lib import proto2xml
from my_lib.bvav import BV_to_AV, AV_to_BV
from my_lib.file_writer import writeER

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
	# global flag_13
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
	# if b[-13] == "1": flag_13 = True

	if b[-10] == "0": flag_spec_danmaku_1 = False
	if b[-11] == "0": flag_gzip = False
	if b[-12] == "0": flag_spec_danmaku_2 = False
	# if b[-13] == "0": flag_13 = False
	if flag_Many_Logs: print(f"[FLAG]: {b}")


def Downloader(url_DL: str, str_s: dict) -> bytes:
	"""
	Text
	"""
	global NET_count_all
	global NET_count
	NET_count_all += 1
	NET_count += 1
	if flag_Many_Logs:
		if flag_Test_Run:
			print(f"[NET]? {url_DL}\t{NET_count_all}   ", end="\t")
		else:
			print(f"[NET]: {url_DL}\t{NET_count_all}   ", end="\t")
	if flag_Test_Run:
		try:
			DL_Data = open(f"[{bvid}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}", "rb").read()
			Fake_status_code___ = 200
		except FileNotFoundError:
			DL_Data = b""
			Fake_status_code___ = 404
		try: DL_Json_code = json.loads(DL_Data)["code"]
		except UnicodeDecodeError: DL_Json_code = 0
		except KeyError: DL_Json_code = 0
		except json.decoder.JSONDecodeError:
			if Fake_status_code___ == 404: DL_Json_code = 404
		if flag_Many_Logs or DL_Json_code != 0 or Fake_status_code___ != 200: print(f"[NET]? File {Fake_status_code___}, Json Code {DL_Json_code}", end="\t")
		if (not flag_Many_Logs) and (DL_Json_code != 0 or Fake_status_code___ != 200): print(f"[{bvid}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}")
		fi = DL_Data
	else:
		time.sleep(SLEEP_TIME)
		DL_Data = requests.get(url_DL, headers=headers)
		try:
			DL_Json_code = json.loads(DL_Data.content)["code"]
			if DL_Json_code != 0:
				global is_ERROR
				is_ERROR = True
		except UnicodeDecodeError: DL_Json_code = 0
		except KeyError: DL_Json_code = 0
		if flag_Many_Logs or DL_Json_code != 0 or DL_Data.status_code != 200: print(f"[NET]: HTTP {DL_Data.status_code}, Json Code {DL_Json_code}", end="\t")
		if (not flag_Many_Logs) and (DL_Json_code != 0 or DL_Data.status_code != 200): print(url_DL)
		fi = DL_Data.content
	return fi


def get_Danmaku(cid: str, Segment_Index: str, retry: str = "") -> bytes:
	"""
	Text
	"""
	URL_Danmaku = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={Segment_Index}'
	ARR_Danmaku_name = [cid, "Danmaku", Segment_Index+retry, "bin"]
	Content = Downloader(URL_Danmaku, ARR_Danmaku_name)
	if is_ERROR and flag_Error_Stop: return b""
	dump_Data(str_s=ARR_Danmaku_name, data=Content)
	return Content


def get_Special_Danmaku(input: dm_pb2.DmWebViewReply) -> bytes:
	"""
	Text
	"""
	BAS_Binary = b""
	i_for_BAS = 1
	for URL_special_dms in input.special_dms:
		ARR_BAS_name = [cid, "BAS", URL_special_dms[27:67], "bin"]
		BAS_Data = Downloader(url_DL=URL_special_dms, str_s=ARR_BAS_name)
		if flag_Many_Logs: print(f"[BAS_DL]: DL {i_for_BAS}")
		if is_ERROR and flag_Error_Stop: break
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
	for this in data: out0 += proto2xml(this=this, exdata=flag_Ext_XML_Data, enable_weight=True)
	return out0


def XML_Special_Process(data, cid) -> str:
	"""
	Text
	"""
	this: dm_pb2.CommandDm
	out1 = ""
	for this in data:
		Ex_Extra_Data = ""
		if flag_Ext_XML_Data: Ex_Extra_Data = f"<!-- SPECIAL: {this.command}{this.extra} -->"
		out1 += f"\t<d p=\"{format(this.progress/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(this.ctime, '%Y-%m-%d %H:%M:%S')))},999,{hex(binascii.crc32(str(this.mid).encode()) ^ 0xFFFFFFFF).lstrip('0x').lstrip('0')},{this.id},11\">{this.content}</d>{Ex_Extra_Data}\n"
	return out1


def dump_Data(str_s: dict, data: bytes, force: bool = False) -> None:
	"""
	Text
	"""
	if flag_Dump_Binary and ((not flag_Test_Run) or force): pass
	else: return
	if len(data) == 0: return
	writeER(filename=f"[{bvid}]_[{str_s[0]}]_[{str_s[1]}]_[{str_s[2]}].{str_s[3]}", data=data, gz=False, binary_=True)


if __name__ == '__main__':
	time1 = time.time()
	# print(sys.argv)
	# ================================ 程序设置
	is_ERROR = False
	tag_LiveRecording = False
	flag_Timer = True			#    1 计时器
	flag_Error_Stop = True		#    2 错误停机
	flag_Many_Logs = False		#    8 日志
	flag_Ext_XML_Data = False	#   16 输出 其他信息到 XML 文件
	flag_NO_Json = False		#   32 不输出 Json
	flag_NO_XML = False			#   64 不输出 XML
	flag_Dump_Binary = False	#  128 输出 Protobuf 二进制文件
	flag_Test_Run = False		#  256 模拟运行
	flag_spec_danmaku_1 = True	#  512 特殊弹幕:BAS
	flag_gzip = False			# 1024 压缩为gzip
	flag_spec_danmaku_2 = True	# 2048 特殊弹幕:UP主自定义内容
	# flag_13 = False				# flag_13
	try: Program_FLAG(sys.argv[2])
	except IndexError: pass
	# if flag_Test_Run: print("[Test Run]: ================================ ")
	# ================================ 终端输入
	try: vid = sys.argv[1]
	except IndexError:
		print("download.py av|bv [flag]")
		# vid = "av0"
		# Program_FLAG("2712")
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
	ARR_json_Resp_name = ["0", "Video", "INFO", "json"]
	json_Resp = Downloader(url_DL=url_Main, str_s=ARR_json_Resp_name)
	if flag_Many_Logs: print(f"[Info]: 1")
	threading.Thread(dump_Data(str_s=ARR_json_Resp_name, data=bytes(json.dumps(json.loads(json_Resp), ensure_ascii=False, separators=(",", ":"), indent="\t"), encoding="utf-8"))).start()
	if is_ERROR and flag_Error_Stop:
		print(f"\n[{bvid}|{avid}]Error: {json.loads(json_Resp)['message']}")
		print("总计用时:", round(time.time()-time1, 3))
		sys.exit(1)
	# ================================ 视频信息?
	if 1:
		ARR_Info_Detail_name = ["0", "Video", "INFO_Detail", "json"]
		if flag_Test_Run: video_info_detail = '{"data":{"Related":[],"Reply":{"replies":[]}}}'
		else: video_info_detail = Downloader(url_DL=url_xx1, str_s=ARR_Info_Detail_name)
		if flag_Many_Logs: print(f"[Info]: 2")
		Vid_detail_json = json.loads(video_info_detail)
		Vid_detail_json["data"]["Related"] = []
		Vid_detail_json["data"]["Reply"]["replies"] = []
		# Vid_detail_json["data"]["View"]["ugc_season"]["sections"]=[]
		threading.Thread(dump_Data(str_s=ARR_Info_Detail_name, data=bytes(json.dumps(Vid_detail_json, ensure_ascii=False, separators=(',', ':'), indent="\t"), encoding="utf-8"))).start()
		del ARR_Info_Detail_name, video_info_detail, Vid_detail_json
	del url_xx1
	# ================================ 加载
	Json_Info = json.loads(json_Resp)["data"]
	Main_Title = Json_Info["title"]
	P_Date = str(Json_Info["pubdate"])
	if Main_Title == "": Main_Title = "Fake_MainTitle"
	Num_of_Videos = int(len(Json_Info["pages"]))
	# ================================ bvid aid 检查
	if Json_Info["bvid"] != bvid: print(f"[bvid]: bvid mismatch {Json_Info['bvid']}|{bvid}")
	if Json_Info["aid"] != avid_in: print(f"[avid]: avid mismatch av{Json_Info['aid']}|{avid}")
	for subs in Json_Info["subtitle"]["list"]:
		if flag_Test_Run: break
		subs_name = ["0", "Subs", f"{subs['id']}_{subs['lan']}", "bcc"]
		threading.Thread(dump_Data(str_s=subs_name, data=Downloader(url_DL=subs["subtitle_url"], str_s=subs_name))).start()
		if flag_Many_Logs: print(f"[Subtitle]: {bvid}")
	# ================================ 分集处理
	i_for_videos = 0
	for This in Json_Info["pages"]:
		i_for_videos += 1
		NET_count = 0
		cid = str(This["cid"])
		if is_ERROR and flag_Error_Stop: break
		time2 = time.time()
		Danmaku_Final_Binary = b""
		duration = int(This["duration"])
		Segment_Count = math.ceil(duration/360)
		URL_Ext = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}'
		ARR_Ext_Info = [cid, "BAS", "INFO", "bin"]
		DL_Data_Extra_Info = Downloader(url_DL=URL_Ext, str_s=ARR_Ext_Info)
		if flag_Many_Logs: print(f"[Special_Danmaku]: P{i_for_videos}")
		ExInfo_Proto = dm_pb2.DmWebViewReply()
		ExInfo_Proto.ParseFromString(DL_Data_Extra_Info)
		ExInfo_Json = json.loads(MessageToJson(ExInfo_Proto, indent=0, ensure_ascii=False))
		threading.Thread(dump_Data(str_s=ARR_Ext_Info, data=DL_Data_Extra_Info)).start()
		if (not flag_NO_XML): XML_Write_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>{6000*Segment_Count}</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
		P_Title = str(This["part"])
		if P_Title == "": P_Title = f"P{i_for_videos}"
		print(f"{P_Date}|{bvid}|{avid}|P{i_for_videos}/{Num_of_Videos}|{cid}|{duration}|{math.ceil(duration/360)}|{Main_Title}|{P_Title}")
		if P_Title == Main_Title: P_Title = ""
		File_Name = f"[{P_Date}][{bvid}][{avid}][P{i_for_videos}][{cid}]{Main_Title.replace('_', '＿')}_{P_Title.replace('_', '＿')}".replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"", "＂").rstrip("_")	# \/:*?"<>|
		# [1656432000][BV1**4*1*7*][av*********][P*][cid]MainTitle_P-Title
		time7 = 0
		time3 = time4 = time.time()
		if (not flag_NO_XML) and flag_spec_danmaku_2: XML_Write_Data += XML_Special_Process(ExInfo_Proto.commandDms, cid=cid)
		if flag_spec_danmaku_1:
			BAS_danmaku = get_Special_Danmaku(ExInfo_Proto)
			xml_t1 = dm_pb2.DmSegMobileReply()
			xml_t1.ParseFromString(BAS_danmaku)
			if (not flag_NO_XML): XML_Write_Data += XML_Process(xml_t1.elems)
			Danmaku_Final_Binary += BAS_danmaku
		time5 = time6 = time.time()
		time7 += time5 - time3
		# 弹幕分段下载
		sec_c: int = 1
		for segments in range(Segment_Count):
			if is_ERROR and flag_Error_Stop: break
			try: Danmaku_Binarys = get_Danmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: Danmaku_Binarys = b""
			# 重试
			if len(Danmaku_Binarys) < 4096 and (not flag_Test_Run):
				temp_filelen = len(Danmaku_Binarys)
				retry_file = []
				for retry_i in range(3):
					if len(Danmaku_Binarys) == 0: break
					if flag_Many_Logs: print(f"[retry]: {segments+1} [{retry_i+1}]")
					try: retry_file.append(get_Danmaku(cid, str(segments+1), retry=f"_R{retry_i+1}"))
					except json.decoder.JSONDecodeError: retry_file.append(b"")
					if len(retry_file[retry_i]) > temp_filelen:
						Danmaku_Binarys = retry_file[retry_i]
						del retry_file, retry_i, temp_filelen
						break
			Danmaku_Final_Binary += Danmaku_Binarys
			if (not flag_NO_XML):
				time3 = time.time()
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_Binarys)
				XML_Write_Data += XML_Process(xml_t1.elems)
				time5 = time.time()
				time7 += time5 - time3
			if (not flag_Many_Logs): print(f"[{cid}]: {sec_c}/{Segment_Count}\r", end="")
			sec_c += 1
			if flag_Many_Logs: print(f"[danmaku]: P{i_for_videos}/{Num_of_Videos}::{segments+1}/{Segment_Count}")
		if (not flag_Many_Logs): print("                      \r", end="")
		if Segment_Count != 1: dump_Data(str_s=[cid, "Danmaku", "ALL", "bin"], data=Danmaku_Final_Binary, force=True)
		time8 = time.time()
		if (not flag_NO_Json):
			if flag_Many_Logs: print(f"[File_JSON P{i_for_videos}]: PROC start")
			Temp_Binary = dm_pb2.DmSegMobileReply()
			Temp_Binary.ParseFromString(Danmaku_Final_Binary)
			j1 = json.loads(MessageToJson(Temp_Binary, indent=0, ensure_ascii=False))
			# ==================
			temp_tag = False
			try:
				j1["elems"]
				temp_tag = True
			except KeyError: pass
			if temp_tag:
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
							tag_LiveRecording = True
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
			del temp_tag
			# ==================
			del Temp_Binary
			if 1:
				if flag_Test_Run:
					try: xx = json.loads(open(f"{File_Name}.json", "r", encoding="utf-8"))["info"]["File_Create_Time"]
					except: xx = time8
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
				j1["info"]["File_Create_Time"] = int(time8)				# num  set unix_timestamp
				j1["info"]["is_live_record"] = tag_LiveRecording		# bool GET
				j1["File_Ver"] = "V3_20220819"
			Json_Write_Data = json.dumps(j1, ensure_ascii=False, separators=(',', ':')).replace("},{\"id\"", "},\n{\"id\"")
			del j1
			if flag_Many_Logs: print(f"[File_JSON P{i_for_videos}]: PROC end--")
		if is_ERROR: err_sign = "ERR_"
		time9 = time.time()
		if (not flag_NO_Json):
			if is_ERROR or flag_Many_Logs: print(f"[File_JSON P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.json", Json_Write_Data, gz=flag_gzip)
			del Json_Write_Data
		timea = time.time()
		if (not flag_NO_XML):
			if is_ERROR or flag_Many_Logs: print(f"[File_XML_ P{i_for_videos}]: 开始写入")
			writeER(f"{err_sign}{File_Name}.xml", XML_Write_Data + f"</i>\n<!-- Create Time: {str(int(time8))} -->")
			del XML_Write_Data
		del ExInfo_Proto, ExInfo_Json, DL_Data_Extra_Info, Danmaku_Final_Binary
		timeb = time.time()
		if flag_Timer or flag_Many_Logs: print(f"P{i_for_videos}: {round(timeb-time2, 3)}，BAS: {round(time6-time4, 3)}，Write: {round(timeb-time9, 3)}，JSON: {round(time9-time8, 3)}，XML: {round(timeb-timea, 3)}，XML_P: {round(time7, 3)}，Wait: {round(NET_count*SLEEP_TIME, 2)}，Net: {NET_count}")
	if is_ERROR or flag_Timer or flag_Many_Logs:
		timec = time.time()
		print(f"{bvid}|{avid} Time: {round(timec-time1, 3)} Net: {NET_count_all} Wait: {round(NET_count_all*SLEEP_TIME, 2)} SLEEP: {SLEEP_TIME}")
	sys.exit(0)
