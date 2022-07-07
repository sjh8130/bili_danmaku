#!/usr/bin/python3
import json
import sys
import re
import time

def ATTR_TYPE(attr:int):
	# return ""
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
	# if o == "" : return "<!-- DM -->"
	if o == "" : return ""
	o = "<!-- " + o + "-->"
	return o

Start_Time = time.time()
try:
	input_PATH = sys.argv[1]
except IndexError:
	print("No Input")
	sys.exit(1)

PathSuffix = re.split("//", input_PATH)[-1]					# Unix,Linux,Windows
if len(re.split("//", input_PATH)) >1:
	PathSuffix = re.split("\\\\", input_PATH)[-1]			# Windows
outputFile = input_PATH.rstrip(".json")+".xml"

Split_SIZE = 4100
try:
	with open(input_PATH, "r", encoding="utf-8")as f:
		jsonData = f.read()
except FileNotFoundError:
	print("File Not Found")
	sys.exit(1)

try: jsonData = json.loads(jsonData)
except json.decoder.JSONDecodeError:
	print("====ERROR====")
	if len(jsonData) <= 2: print("Empty File")
	print("总计用时:", time.time()-Start_Time)
	sys.exit(1)

cid = re.split("\]",re.split("\]\[", PathSuffix)[4])[0]		# [publishtTime][BV**][av**][P*][cid]Title_P-Title.json

danmu_count = len(jsonData["elems"])
XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
XML_Data_2nd_Cache = ""

for i in range(danmu_count):
	Sub_Item = jsonData["elems"][i]
	spec_tag = ""
	try: content = Sub_Item["content"]		# string content = 7;
	except KeyError: content = ""
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\u0008","").replace("\u0017","")

	try: progress = Sub_Item["progress"]	# int32 progress = 2;
	except KeyError: progress = 0
	progress = format(progress/1000, ".5f")

	mode = Sub_Item["mode"]					# int32 mode = 3;
	fontsize = Sub_Item["fontsize"]			# int32 fontsize = 4;

	try: color = Sub_Item["color"]			# uint32 color = 5;
	except KeyError: color = 0

	midHash = Sub_Item["midHash"]			# string midHash = 6;
	sendtime = Sub_Item["ctime"]				# int64 ctime = 8;

	try: ban_weight = Sub_Item["weight"]		# int32 weight = 9;
	except KeyError: ban_weight = 11

	try: attr = Sub_Item["attr"]			# int32 attr = 13;
	except KeyError: attr = 0

	try: action = Sub_Item["action"]		# string action = 10;
	except KeyError: pass

	try: animation = Sub_Item["animation"]	# string animation = 22;
	except KeyError: pass

	try: id_ = Sub_Item["id"]				# int64 id = 1;
	except KeyError: id_ = "0"

	try: idStr = Sub_Item["idStr"]			# string idStr = 12;
	except KeyError:
		idStr = "0"
		print(f"\n idStr ERROR: {id_}")

	if id_ != idStr:print("\n id idStr mismatch:", id_, idStr)

	try: pool = Sub_Item["pool"]			# int32 pool = 11;
	except KeyError: pool = 0
	if pool == 2: content = content.replace("\n", "\\n").replace("\r\n", "\\n")

	# Mode	1/2/3:regular	4:buttom	5:top	6:reverse(disable)	7:advance	8:code	9:BAS
	# Pool	0:regular	1:subtitle	2:special(BAS/code)
	if True:
		if mode == 0: spec_tag += "mode:ERROR"
		# if mode == 1: spec_tag += "mode:Normal-1"
		if mode == 2: spec_tag += "mode:Normal-2"
		if mode == 3: spec_tag += "mode:Normal-3"
		# if mode == 4: spec_tag += "mode:Bottom"
		# if mode == 5: spec_tag += "mode:Top"
		if mode == 6: spec_tag += "mode:Reverse!!!!"
		if mode == 7: spec_tag += "mode:!!Advanced!!"
		if mode == 8: spec_tag += "mode:!!Code!!"
		if mode == 9: spec_tag += "mode:!!BAS!!"
		# if pool == 0: spec_tag += "pool:Regular"
		if pool == 1: spec_tag += "pool:SubTitle"
		if pool == 2: spec_tag += "pool:BAS|Code"
		if spec_tag != "": spec_tag = "<!-- "+spec_tag+" -->"

	XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}{11}\n".format(progress, mode, fontsize, color, sendtime, pool, midHash, id_, ban_weight, content, ATTR_TYPE(attr), spec_tag)
	XML_Data_2nd_Cache += XML_item
	if i % Split_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
		print(f"\rProgress: {i}/{danmu_count}, Time: {round(time.time()-Start_Time,3)}",end="")

XML_Data_1st_Cache += XML_Data_2nd_Cache
XML_Data_1st_Cache += "</i>\n"
with open(outputFile, "w", encoding="utf-8")as g:
	g.write(XML_Data_1st_Cache)
	g.close()
End_Time = time.time()
print(f"\r总计用时：{round(End_Time-Start_Time, 4)}                     ")
