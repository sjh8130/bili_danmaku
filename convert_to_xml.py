#!/usr/bin/python3
import json
import sys
import time
import gzip
import os
import binascii

def ATTR_TYPE(attr:int):
	o = ""
	b = "0000000000" + bin(attr).lstrip("0b")
	if b[-1 ] == "1": o += "保护|"
	if b[-2 ] == "1": o += "直播|"
	if b[-3 ] == "1": o += "高赞|"
	if b[-4 ] == "1": o += "壹|"
	if b[-5 ] == "1": o += "贰|"	# Y 硬核会员 不显示？
	if b[-6 ] == "1": o += "叁|"
	if b[-7 ] == "1": o += "肆|"	# Y 硬核会员 不显示？
	if b[-8 ] == "1": o += "伍|"
	if b[-9 ] == "1": o += "陆|"	# Y
	if b[-10] == "1": o += "柒|"
	return o

Start_Time = time.time()
try:
	input_File = sys.argv[1]
except IndexError:
	print("No Input")
	sys.exit(1)

try:
	infile = gzip.open(input_File, "rb").read()
except gzip.BadGzipFile:
	infile = open(input_File, "r", encoding="utf-8").read()
outputFile = input_File.rstrip(".gz").rstrip(".json")+".xml"

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000

dedup_Table = []

Loaded_JSON = json.loads(infile)
infile = None
i = 1
try: cid = Loaded_JSON["info"]["cid"]
except KeyError: cid = 0
try: Max_Limit = Loaded_JSON["info"]["segment_count"]*6000
except KeyError: Max_Limit = 6000
Danmaku_Count = len(Loaded_JSON["elems"])
XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\x0a<i>\x0a\t<chatserver>chat.bilibili.com</chatserver>\x0a\t<chatid>{cid}</chatid>\x0a\t<mission>0</mission>\x0a\t<maxlimit>{Max_Limit}</maxlimit>\x0a\t<state>0</state>\x0a\t<real_name>0</real_name>\x0a\t<source>k-v</source>\x0a"
XML_Data_2nd_Cache = ""
XML_Data_3rd_Cache = ""

try: Last_Modified_Time = Loaded_JSON['info']['File_Create_Time']
except KeyError: Last_Modified_Time = int(os.stat(input_File).st_ctime)

compatible_1 = False
try:
	Loaded_JSON["commandDms"]
	compatible_1 = True
except KeyError: pass
if compatible_1:
	for Item_sp in Loaded_JSON["commandDms"]:
		id_ = Item_sp["id"]					# int64 id = 1
		oid = Item_sp["oid"]				# int64 oid = 2;
		mid = Item_sp['mid']				# int64 mid = 3;
		command = Item_sp["command"]		# string command = 4;
		content = Item_sp["content"]		# string content = 5;
		try: progress = Item_sp["progress"]		# int32 progress = 6;
		except KeyError: progress = 0
		ctime = Item_sp["ctime"]			# string ctime = 7;
		mtime = Item_sp["mtime"]			# string mtime = 8;
		extra = Item_sp["extra"]			# string extra = 9;
		idStr = Item_sp["idStr"]			# string idStr = 10
		progress = format(progress/1000, ".5f")
		sendtime = int(time.mktime(time.strptime(ctime, '%Y-%m-%d %H:%M:%S')))
		midHash = hex(binascii.crc32(mid.encode())^0xFFFFFFFF).lstrip("0x").lstrip("0")
		XML_Data_1st_Cache += f"\t<d p=\"{progress},1,25,16777215,{sendtime},999,{midHash},{id_},11\">{content}</d><!-- SPECIAL: {command}{extra} -->\x0a"

for Sub_Item in Loaded_JSON["elems"]:
	try: id_ = Sub_Item["id"]						# int64 id = 1;
	except KeyError: id_ = "0"

	# # Deduplication 20x time
	# if id_ in dedup_Table:
	# 	continue
	# dedup_Table.append(id_)

	Extended_Data = ""
	try: progress = Sub_Item["progress"]			# int32 progress = 2;
	except KeyError: progress = 0

	try: mode = Sub_Item["mode"]					# int32 mode = 3;
	except KeyError: mode = 1

	try: fontsize = Sub_Item["fontsize"]			# int32 fontsize = 4;
	except KeyError: fontsize = 25

	try: color = Sub_Item["color"]					# uint32 color = 5;
	except KeyError: color = 0

	try: midHash = Sub_Item["midHash"]				# string midHash = 6;
	except KeyError: midHash = "ffffffff"

	try: content = Sub_Item["content"]				# string content = 7;
	except KeyError: content = ""

	try: sendtime = Sub_Item["ctime"]				# int64 ctime = 8;
	except KeyError: sendtime = "1262275200"

	try: weight = Sub_Item["weight"]			# int32 weight = 9;
	except KeyError: weight = 11

	try: action = Sub_Item["action"]				# string action = 10;
	except KeyError: pass

	try: pool = Sub_Item["pool"]					# int32 pool = 11;
	except KeyError: pool = 0

	try: idStr = Sub_Item["idStr"]					# string idStr = 12;
	except KeyError: idStr = "0"
	if id_ != idStr:print("\n id idStr mismatch:", id_, idStr)

	try: attr = ATTR_TYPE(Sub_Item["attr"])			# int32 attr = 13;
	except KeyError: attr = "DM "

	try: usermid = f"mid:{Sub_Item['usermid']} "	# string usermid = 14;
	except KeyError: usermid = ""

	try: likes = f"Likes:{Sub_Item['likes']} "		# string likes = 15;
	except KeyError: likes = ""

	try: animation = Sub_Item["animation"]			# string animation = 22;
	except KeyError: pass

	try: replyCount = f"Reply:{Sub_Item['replyCount']} "												# replyCount
	except KeyError: replyCount = ""
	dm_reply_to = " "
	try: dm_reply_to = f"reply_to:{Sub_Item['test16']} "												# test16
	except KeyError:
		try: dm_reply_to = f"reply_to:{Sub_Item['test17']} "											# test17
		except KeyError:
			try:
				if Sub_Item['test20'] != "0": dm_reply_to = f"reply_to:{Sub_Item['test20']} "			# test20
			except KeyError:
				try:
					if Sub_Item['test21'] != "0": dm_reply_to = f"reply_to:{Sub_Item['test21']} "		# test21
				except KeyError: pass

	Extended_Data = f"<!-- {attr}{usermid}{likes}{replyCount}{dm_reply_to}-->".replace("  "," ")
	progress = format(progress/1000, ".5f")
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")

	# XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}\x0a".format(progress, mode, fontsize, color, sendtime, pool, midHash, id_, weight, content, spec_tag)
	XML_Data_3rd_Cache += f"\t<d p=\"{progress},{mode},{fontsize},{color},{sendtime},{pool},{midHash},{id_},{weight}\">{content}</d>{Extended_Data}\x0a"
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {len(dedup_Table)}|{i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}",end="")
	Sub_Item = {}

open(outputFile, "w", encoding="utf-8").write(XML_Data_1st_Cache+XML_Data_2nd_Cache+XML_Data_3rd_Cache+f"</i>\x0a<!-- Create Time: {Last_Modified_Time} -->")
End_Time = time.time()
print(f"\r{len(dedup_Table)}|{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
