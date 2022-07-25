#!/usr/bin/python3
# 系统十分稳定，所有代码不要随便动.JPG
from google.protobuf.json_format import MessageToJson
from tqdm import tqdm
import requests

import zzzz

import math
import time
import json
import sys
import io
import gzip

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}
SLEEP_TIME = 0.75
BV_AV_table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
BV_AV_base58_dic = {}
for BV_AV_base58_i in range(58): BV_AV_base58_dic[BV_AV_table[BV_AV_base58_i]] = BV_AV_base58_i
s = [11, 10, 3, 8, 4, 6]
BV_AV_xor = 177451812
BV_AV_add = 8728348608
NET_count = -1
NET_count_all = 0


def Program_FLAG(flag: str):
	if flag == "-1": return
	if flag.find("0b") == 0: b = flag
	else: b = bin(int(flag))
	b = "0000000000" + b.lstrip("0b")
	global flag_Timer
	global flag_Error_Stop
	global flag_Zero_Stop
	global flag_Many_Logs
	global flag_Ext_XML_Data
	global flag_NO_Json
	global flag_NO_XML
	global flag_Dump_Binary_
	global flag_Test_Run
	if b[-1] == "1": flag_Timer = True
	if b[-2] == "1": flag_Error_Stop = True
	if b[-3] == "1": flag_Zero_Stop = True
	if b[-4] == "1": flag_Many_Logs = True
	if b[-5] == "1": flag_Ext_XML_Data = True
	if b[-6] == "1": flag_NO_Json = True
	if b[-7] == "1": flag_NO_XML = True
	if b[-8] == "1": flag_Dump_Binary_ = True
	if b[-9] == "1": flag_Test_Run = True
	if b[-1] == "0": flag_Timer = False
	if b[-2] == "0": flag_Error_Stop = False
	if b[-3] == "0": flag_Zero_Stop = False
	if b[-4] == "0": flag_Many_Logs = False
	if b[-5] == "0": flag_Ext_XML_Data = False
	if b[-6] == "0": flag_NO_Json = False
	if b[-7] == "0": flag_NO_XML = False
	if b[-8] == "0": flag_Dump_Binary_ = False
	if b[-9] == "0": flag_Test_Run = False
	if flag_Many_Logs: print(f"[FLAG]: {b}", end="\t")


def danmaku_ATTR_TYPE(attr: int):
	global flag_Ext_XML_Data
	if (not flag_Ext_XML_Data): return ""
	o = ""
	b = "0000000000" + bin(attr).lstrip("0b")
	if b[-1] == "1": o += "保护 "
	if b[-2] == "1": o += "直播 "
	if b[-3] == "1": o += "高赞 "
	if b[-4] == "1": o += "壹 "
	if b[-5] == "1": o += "贰 "
	if b[-6] == "1": o += "叁 "
	if b[-7] == "1": o += "肆 "
	if b[-8] == "1": o += "伍 "
	if b[-9] == "1": o += "陆 "
	if b[-10] == "1": o += "柒 "
	if o == "": return ""
	o = f"<!-- {o}-->"
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


def downloader(url_DL: str):
	if flag_Many_Logs: print(f"[NET]: {url_DL}", end="\t")
	time.sleep(SLEEP_TIME)
	resp = requests.get(url_DL, headers=headers)
	global NET_count
	NET_count += 1
	global NET_count_all
	NET_count_all += 1
	try:
		status_code = json.loads(resp.content)["code"]
		if status_code != 0:
			global is_ERROR
			is_ERROR = True
	except UnicodeDecodeError: status_code = 0
	if flag_Many_Logs or status_code != 0 or resp.status_code != 200: print(f"[NET]: HTTP {resp.status_code}, Json Code {status_code}", end="\t")
	return resp.content


def FAKE_downloader(str0:str, str1:str, str2:str, url_Fake_DL:str):
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
	if flag_Many_Logs or status_code != 0 or Fake_status_code != 200: print(f"[NET]? HTTP {Fake_status_code}, Json Code {status_code}", end="\t")
	return resp


def get_danmaku(cid: str, segment_index: str):
	url_Danmaku = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={segment_index}'
	if flag_Test_Run: content = FAKE_downloader(str0=cid, str1="Danmaku", str2=segment_index, url_Fake_DL=url_Danmaku)
	else: content = downloader(url_Danmaku)
	dump_Data(str0=cid, str1="Danmaku", str2=segment_index, data=content)
	if is_ERROR and flag_Error_Stop: return b""
	return content


def get_BAS_danmaku(avid: str, cid: str):
	url_BAS_INFO = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}&pid={avid}'

	if flag_Test_Run: data_1 = FAKE_downloader(str0=cid, str1="BAS", str2="INFO", url_Fake_DL=url_BAS_INFO)
	else: data_1 = downloader(url_BAS_INFO)

	if flag_Many_Logs: print("[BAS_DL]: Info")
	if is_ERROR or flag_Error_Stop: return b""
	data_2 = zzzz.DmWebViewReply()
	data_2.ParseFromString(data_1)
	dump_Data(str0=cid, str1="BAS", str2="Info", data=data_1)
	try: data_3 = json.loads(MessageToJson(data_2))["specialDms"]
	except KeyError:
		if flag_Many_Logs: print(f"[BAS P{i+1}]: No BAS Danmaku")
		return b""
	if len(data_3) == 0:
		if flag_Many_Logs: print(f"[BAS P{i+1}]: Empty")
		return b""
	print(f"[BAS P{i+1}]{len(data_3)}")
	BAS_Binary = b""
	k = 1
	for URL_BAS_Data in data_3:
		if flag_Test_Run: data = FAKE_downloader(str0=cid, str1="BAS", str2=f"{k}", url_Fake_DL=URL_BAS_Data)
		else: data = downloader(URL_BAS_Data)

		if flag_Many_Logs: print("[BAS_DL]: DL", end="\t")
		if is_ERROR and flag_Error_Stop: break
		BAS_Binary += data
		dump_Data(str0=cid, str1="BAS", str2=f"{k}", data=data)
		k += 1
	return BAS_Binary


def XML_Process(data):
	if data == "{}": return ""
	global flag_Ext_XML_Data
	jsonData = json.loads(data)
	XML_Data_2nd = ""
	for Sub_Item in jsonData["elems"]:
		try: content = Sub_Item["content"]			# string content = 7;
		except KeyError: content = ""
		content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ")

		try: progress = Sub_Item["progress"] 		 # int32 progress = 2;
		except KeyError: progress = 0
		progress = format(progress/1000, ".5f")

		mode = Sub_Item["mode"]						# int32 mode = 3;
		# 1/2/3:regular	4:buttom	5:top	6:reverse(disable)	7:advance	8:code	9:BAS
		fontsize = Sub_Item["fontsize"]				# int32 fontsize = 4;
		# 18/25/36
		try: color = Sub_Item["color"]				# uint32 color = 5;
		except KeyError: color = 0

		midHash = Sub_Item["midHash"]				# string midHash = 6;
		sendtime = Sub_Item["ctime"]				# int64 ctime = 8;

		try: weight = Sub_Item["weight"]			# int32 weight = 9;
		except KeyError: weight = 11
		if flag_Ext_XML_Data:
			try: attr = Sub_Item["attr"]			# int32 attr = 13;
			except KeyError: attr = 0

			try: action = Sub_Item["action"]		# string action = 10;
			except KeyError: pass

			try: animation = Sub_Item["animation"]	# string animation = 22;
			except KeyError: pass
		else:
			attr = 0
			action = ""
			animation = ""

		try: id_ = Sub_Item["id"]					# int64 id = 1;
		except KeyError: id_ = "0"

		try: idStr = Sub_Item["idStr"]				# string idStr = 12;
		except KeyError: idStr = "0"

		if id_ != idStr: print("\n id&idStr mismatch:", id_, idStr)

		try: pool = Sub_Item["pool"]			# int32 pool = 11;
		except KeyError: pool = 0
		# 0:regular	1:subtitle	2:special(BAS/code)
		content = content.replace("\n", "\\n").replace("\r\n", "\\n")
		spec_tag = ""

		XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}{11}\n".format(progress, mode, fontsize, color, sendtime, pool, midHash, id_, weight, content, danmaku_ATTR_TYPE(attr), spec_tag)
		XML_Data_2nd += XML_item
	return XML_Data_2nd


def dump_Data(str0:str, str1:str, str2:str, data: bin):
	if flag_Dump_Binary_ and (not flag_Test_Run): pass
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
	flag_Dump_Binary_ = False	# 输出 Protobuf 二进制文件
	flag_Test_Run = False		# 模拟运行
	flag_BAS = True
	try: P_flag = sys.argv[2]
	except IndexError: P_flag = "0"
	Program_FLAG(P_flag)
	if flag_Test_Run: print("[Test Run]: ================================ ")
	vid = sys.argv[1]
	if flag_NO_Json and flag_NO_XML and (not flag_Dump_Binary_):
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

	if flag_Test_Run: json_Resp = FAKE_downloader(str0="0", str1="Video", str2="INFO", url_Fake_DL=url_Main)
	else: json_Resp = downloader(url_Main)

	dump_Data(str0="0", str1="Video", str2="INFO", data=json_Resp)
	if is_ERROR and flag_Error_Stop:
		print(f"[{bvid}|{avid}]Error: {json_Resp}")
		print("总计用时:", time.time()-开始时间)
		sys.exit(1)

	json_Data = json.loads(json_Resp)["data"]
	sub_Items = json_Data["pages"]
	mainTitle = json_Data["title"]
	publish_D = str(json_Data["pubdate"])

	if json_Data["bvid"] != bvid: print(f"[bvid]: bvid mismatch {json_Data['bvid']}|{bvid}")
	if json_Data["aid"] != avid_in: print(f"[avid]: avid mismatch av{json_Data['aid']}|{avid}")

	if mainTitle == "": mainTitle = "Fake_MainTitle"
	sub_Items_Len = len(sub_Items)

	if json_Data["stat"]["danmaku"] == 0 and flag_Zero_Stop:
		print("No danmaku")
		for i in range(sub_Items_Len):
			duration = int(sub_Items[i]["duration"])
			cid = str(sub_Items[i]["cid"])
			P_Title = str(sub_Items[i]["part"])
			show_string = f"{publish_D}|{bvid}|{avid}|P{i+1}/{sub_Items_Len}|{cid}|{duration}|{math.ceil(duration/360)}|{mainTitle}|{P_Title}"
			print(show_string)
		print("总计用时:", time.time()-开始时间)
		sys.exit(1)

	for i in range(sub_Items_Len):
		if is_ERROR and flag_Error_Stop: break
		分P开始时间 = time.time()
		if (not flag_NO_Json):
			Danmaku_Binary = b""
			Temp_Binary = zzzz.DmSegMobileReply()
		duration = int(sub_Items[i]["duration"])
		segment_count = math.ceil(duration/360)
		cid = str(sub_Items[i]["cid"])
		if (not flag_NO_XML): XML_Write_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>{6000*segment_count}</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
		if (not flag_NO_XML): XML_Data_Empty = XML_Write_Data
		P_Title = str(sub_Items[i]["part"])
		if mainTitle == P_Title: P_Title = ""
		show_string = f"\n{publish_D}|{bvid}|{avid}|P{i+1}/{sub_Items_Len}|{cid}|{duration}|{math.ceil(duration/360)}|{mainTitle}|{P_Title}"
		print(show_string)
		File_Name = f"[{publish_D}][{bvid}][{avid}][P{i+1}][{cid}]{mainTitle.replace('_', '＿')}_{P_Title.replace('_', '＿')}".rstrip("_")
		File_Name = File_Name.replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜").replace("\"","＂")	# \/:*?"<>|
		# [1656432000][BV1**4*1*7*][av*********][P*][cid]MainTitle_P-Title
		# [1656432000][BV1**4*1*7*][av*********][P*][cid]MainTitle
		XML_Time = 0
		BAS开始时间 = time.time()
		if flag_BAS:
			if flag_Many_Logs: print(f"[BAS]: {bvid}|{avid}|{cid}|P{i+1}")
			BAS_danmaku = get_BAS_danmaku(avid=avid_in, cid=cid)
			if len(BAS_danmaku) == 0: pass
			else:
				if (not flag_NO_XML):
					XML_Ti = time.time()
					xml_t1 = zzzz.DmSegMobileReply()
					xml_t1.ParseFromString(BAS_danmaku)
					xml_t2 = MessageToJson(xml_t1)
					XML_Write_Data += XML_Process(xml_t2)
					XML_Tim = time.time()
					XML_Time += XML_Tim - XML_Ti
				if (not flag_NO_Json): Danmaku_Binary += BAS_danmaku
		BAS结束时间 = time.time()
		if not flag_Many_Logs: Progress_Bar = tqdm(total=segment_count, leave=False, unit='chunks', ascii=True, ncols=100)
		for segments in range(segment_count):
			if is_ERROR and flag_Error_Stop: break
			try: Danmaku_sub_Items = get_danmaku(cid, str(segments+1))
			except json.decoder.JSONDecodeError: Danmaku_sub_Items = b""
			if (not flag_NO_Json): Danmaku_Binary += Danmaku_sub_Items
			if (not flag_NO_XML):
				XML_Ti = time.time()
				xml_t1 = zzzz.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_sub_Items)
				XML_Write_Data += XML_Process(MessageToJson(xml_t1))
				XML_Tim = time.time()
				XML_Time += XML_Tim - XML_Ti
			if (not flag_Many_Logs): Progress_Bar.update(1)
			if is_ERROR or flag_Many_Logs: print(f"[danmaku]: P{i+1}/{sub_Items_Len}::{segments+1}/{segment_count}")
		if (not flag_Many_Logs):Progress_Bar.close()
		dump_Data(str0=cid, str1="Danmaku", str2="ALL", data=Danmaku_Binary)
		JSON_Time = time.time()
		if (not flag_NO_Json):
			if flag_Many_Logs: print(f"[File_JSON P{i+1}]: PROC start")
			Temp_Binary.ParseFromString(Danmaku_Binary)
			j1 = json.loads(MessageToJson(Temp_Binary))
			danmaku_count = len(j1["elems"])
			Danmaku_Binary = b""
			Temp_Binary = zzzz.DmSegMobileReply()
			j1["info"] = {}
			j1["info"]["owner_name"] = json_Data['owner']['name']
			j1["info"]["owner_mid"] = json_Data['owner']['mid']
			j1["info"]["bvid"] = json_Data['bvid']
			j1["info"]["avid"] = json_Data['aid']
			j1["info"]["V_Name"] = mainTitle
			j1["info"]["pubdate"] = json_Data['pubdate']
			j1["info"]["ctime"] = json_Data['ctime']
			j1["info"]["P_Name"] = P_Title
			j1["info"]["duration"] = duration
			j1["info"]["cid"] = cid
			j1["info"]["segment_count"] = segment_count
			j1["info"]["danmaku_count"] = danmaku_count
			Json_Write_Data = json.dumps(j1, ensure_ascii=False)
			j1 = {}
			if flag_Many_Logs: print(f"[File_JSON P{i+1}]: PROC end--")
		写入开始时间 = time.time()
		if (not flag_NO_Json):
			if Json_Write_Data == "{}" or Json_Write_Data == "":
				if is_ERROR or flag_Many_Logs: print(f"[File_JSON P{i+1}]: No Data")
			else:
				if is_ERROR or flag_Many_Logs: print(f"[File_JSON P{i+1}]: 开始写入")
				io.TextIOWrapper(gzip.open(File_Name+".json.gz",'wb'),encoding='utf-8').writelines(Json_Write_Data)
				Json_Write_Data = ""
		Time_Point_ = time.time()
		if (not flag_NO_XML):
			if XML_Write_Data == XML_Data_Empty: 
				if is_ERROR or flag_Many_Logs: print(f"[File_XML  P{i+1}]: No Data")
			else:
				if is_ERROR or flag_Many_Logs: print(f"[File_XML  P{i+1}]: 开始写入")
				open(File_Name+".xml", "w", encoding="utf-8").write(XML_Write_Data + "</i>\n")
				XML_Write_Data = ""
		else: print()

		分P结束时间 = time.time()
		if flag_Timer or flag_Many_Logs: print(f"P{i+1}: {分P结束时间-分P开始时间}，BAS: {BAS结束时间-BAS开始时间}，Write: {分P结束时间-写入开始时间}，JSON: {写入开始时间-JSON_Time}，XML: {分P结束时间-Time_Point_}，XML_P: {XML_Time}，Wait:{NET_count*SLEEP_TIME}，Net:{NET_count}，Danmaku:{danmaku_count}")
		NET_count = 0
	if is_ERROR or flag_Timer or flag_Many_Logs:
		结束时间 = time.time()
		print(f"{bvid}|{avid} Time: {结束时间-开始时间} Net:{NET_count_all} Wait:{NET_count_all*SLEEP_TIME} SLEEP:{SLEEP_TIME}")
	sys.exit(0)
