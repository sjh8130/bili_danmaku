#!/usr/bin/python3
import math
import time
from google.protobuf.json_format import MessageToJson
import requests
import json
import dm_pb2
import sys
from tqdm import tqdm

is_ERROR = False
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"}

BV_AV_table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
BV_AV_base58_dic = {}
for BV_AV_base58_i in range(58): BV_AV_base58_dic[BV_AV_table[BV_AV_base58_i]] = BV_AV_base58_i
s = [11, 10, 3, 8, 4, 6]
BV_AV_xor = 177451812
BV_AV_add = 8728348608


def BV_to_AV(input_BV: str):
	result = 0
	for i in range(6): result += BV_AV_base58_dic[input_BV[s[i]]]*58**i
	out = (result-BV_AV_add) ^ BV_AV_xor
	if out <= 0:
		print("[BV_to_AV]: invaild avid")
		global is_ERROR																						# 错误停机
		is_ERROR = True																						# 错误停机
	return out


def AV_to_BV(input_AV: int):
	if input_AV > 2147483647:
		global is_ERROR																						# 错误停机
		is_ERROR = True																						# 错误停机
		print("[AV_to_BV]: avid is too big")
	input_AV = (input_AV ^ BV_AV_xor)+BV_AV_add
	result = list('BV1  4 1 7  ')
	for i in range(6): result[s[i]] = BV_AV_table[input_AV//58**i % 58]
	return ''.join(result)


def downloader(url):
	contents = requests.get(url, headers=headers).content
	try:
		status_code = json.loads(contents)["code"]
		if status_code != 0:
			print(f"[NET]: Error Code {status_code}")
			global is_ERROR																					# 错误停机
			is_ERROR = True																					# 错误停机
	except UnicodeDecodeError: pass
	return contents


def getDanmu(cid: str, segment_index: str):
	url = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={segment_index}'
	if is_ERROR: return b""																					# 错误停机
	time.sleep(0.7)
	return downloader(url)


def get_BAS_danmu(avid: str, cid: str):
	url_1 = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}&pid={avid}'
	data_1 = downloader(url_1)
	data_2 = dm_pb2.DmWebViewReply()
	data_2.ParseFromString(data_1)
	try: data_3 = json.loads(MessageToJson(data_2))["specialDms"]
	except KeyError: return b""
	if len(data_3) == 0: return b""
	BAS_Binary = b""
	for i in data_3:
		data = downloader(i)
		if is_ERROR: break																					# 错误停机
		time.sleep(1)
		BAS_Binary += data
	return BAS_Binary


if __name__ == '__main__':
	开始时间 = time.time()													# 性能测试
	if sys.argv[1].find("https://www.bilibili.com/video/") == 0:vid = sys.argv[1].lstrip("https://www.bilibili.com/video/")
	elif sys.argv[1].find("http://www.bilibili.com/video/") == 0:vid = sys.argv[1].lstrip("http://www.bilibili.com/video/")
	elif sys.argv[1].find("https://b23.tv/BV1") == 0:vid = sys.argv[1].lstrip("https://b23.tv/")
	else:vid = sys.argv[1]
	vid = vid.split("?")[0].split("/")[0]
	if vid.find("av") == 0:
		avid = vid
		avid_in = int(avid.lstrip("av"))
		bvid = AV_to_BV(avid_in)
	else:
		bvid = vid
		avid_in = BV_to_AV(bvid)
		avid = "av" + str(avid_in)

	url = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
	json_Resp = downloader(url)
	json_List = json.loads(json_Resp)

	if is_ERROR:																							# 错误停机
		print(f"[{bvid}|{avid}]Error: {json_List['data']}")
		print("总计用时:", time.time()-开始时间)								# 性能测试
		sys.exit(1)

	json_Data = json_List["data"]
	sub_Items = json_Data["pages"]
	mainTitle = json_Data["title"]
	publish_D = str(json_Data["pubdate"])
	if mainTitle == "": mainTitle = "Fake_MainTitle"
	mainTitle_escape = mainTitle.replace("_","＿").replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*","＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜")	# \/:*?"<>|
	sub_Items_Len = len(sub_Items)

	if json_List["data"]["stat"]["danmaku"] == 0:
		for i in range(sub_Items_Len):
			duration = int(sub_Items[i]["duration"])
			cid = str(sub_Items[i]["cid"])
			P_Title = str(sub_Items[i]["part"])
			show_string = publish_D+"|{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, i+1, sub_Items_Len, cid, duration, math.ceil(duration/360), mainTitle, P_Title)
			print(show_string)
		print("No danmu")
		print("总计用时:", time.time()-开始时间)								# 性能测试
		sys.exit(1)

	for i in range(sub_Items_Len):
		if is_ERROR: break																					# 错误停机
		分P开始时间 = time.time()												# 性能测试
		Danmaku_Binary = b""
		Temp_Binary = b""
		Temp_Binary = dm_pb2.DmSegMobileReply()
		duration = int(sub_Items[i]["duration"])
		cid = str(sub_Items[i]["cid"])
		P_Title = str(sub_Items[i]["part"])
		if mainTitle == P_Title: P_Title = ""
		P_Title_escape = P_Title.replace("_","＿").replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*","＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜")
		show_string = "{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, i+1, sub_Items_Len, cid, duration, math.ceil(duration/360), mainTitle, P_Title)
		print(show_string)
		File_Name = f"[{publish_D}][{bvid}][{avid}][P{i+1}][{cid}]{mainTitle_escape}_{P_Title_escape}".rstrip("_")+".json"	#[1656432000][BV1**4*1*7*][av*********][P*][]

		BAS开始时间 = time.time()												# 性能测试
		BAS_danmu = get_BAS_danmu(avid=avid_in, cid=cid)
		if is_ERROR: print(f"[BAS_danmu]: {bvid}|{avid}|{cid}")												# 错误停机
		Danmaku_Binary += BAS_danmu
		BAS结束时间 = time.time()												# 性能测试

		Progress_Bar = tqdm(total=math.ceil(duration/360), leave=False)

		for segments in range(math.ceil(duration/360)):
			if is_ERROR: break																				# 错误停机
			try:
				Danmaku_sub_Items = getDanmu(cid, str(segments+1))
			except json.decoder.JSONDecodeError:
				Danmaku_sub_Items = b""
			if is_ERROR: print(f"[danmu]: P{i+1}/{sub_Items_Len}::{segments}/{math.ceil(duration/360)}")	# 错误停机
			Danmaku_Binary += Danmaku_sub_Items
			Progress_Bar.update(1)
		Temp_Binary.ParseFromString(Danmaku_Binary)
		Progress_Bar.close()

		写入开始时间 = time.time()												# 性能测试
		Write_Data = json.dumps(json.loads(MessageToJson(Temp_Binary)), ensure_ascii=False)
		if not(Write_Data == "{}" or Write_Data == ""):
			with open(File_Name, "w", encoding="utf-8") as f:
				if is_ERROR: print("[File]: 开始写入")								# 性能测试
				f.write(Write_Data)
		分P结束时间 = time.time()												# 性能测试
		if is_ERROR: print(f"分P{i+1} : {分P结束时间-分P开始时间}, BAS用时: {BAS结束时间-BAS开始时间}，写入用时: {分P结束时间-写入开始时间}")	# 性能测试
	if is_ERROR: print(f"{bvid}|{avid} 总计用时: {time.time()-开始时间}")		# 性能测试
	sys.exit(0)
