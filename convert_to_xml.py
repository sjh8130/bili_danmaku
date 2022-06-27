import json
import sys
import re
import time

Start_Time = time.time()
jsonData = ""
input_file = sys.argv[1]
outputFile = input_file.rstrip(".json")+".xml"
Split_SIZE = 2500

with open(input_file, "r", encoding="utf-8")as f:
	jsonData = f.read()

try: jsonData = json.loads(jsonData)
except json.decoder.JSONDecodeError:
	print("\033[41m==============================ERROR=============================\033[0m")
	if len(jsonData) <= 2:	print("\033[41m Empty File\033[0m")
	print("总计用时:", time.time()-Start_Time)
	sys.exit(1)

cid = re.split("_", input_file)[3]
XML_item = ""

danmu_count = len(jsonData["elems"])
XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
XML_Data_2nd_Cache = ""

for i in range(danmu_count):
	Sub_Item = jsonData["elems"][i]

	try: content = Sub_Item["content"]		# string content = 7;
	except KeyError: continue
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

	string_not_used_1 = ""
	string_not_used_2 = ""
	string_not_used_3 = ""

	try: progress = Sub_Item["progress"]	# int32 progress = 2;
	except KeyError: progress = 0.0

	progress = format(progress/1000, ".5f")	# int32 progress = 2;
	mode = Sub_Item["mode"]					# int32 mode = 3;
	fontsize = Sub_Item["fontsize"]			# int32 fontsize = 4;

	try: color = Sub_Item["color"]			# uint32 color = 5;
	except KeyError: color = 0

	midHash = Sub_Item["midHash"]			# string midHash = 6;
	ctime = Sub_Item["ctime"]				# int64 ctime = 8;

	try: weight = Sub_Item["weight"]		# int32 weight = 9;
	except KeyError: weight = 11

	try: attr = Sub_Item["attr"]			# int32 attr = 13;
	except KeyError: attr = 0
	if attr == 0: string_not_used_1 = "<!-- DANMU -->"
	if attr == 1: string_not_used_1 = "<!-- 保护弹幕 -->"
	if attr == 2: string_not_used_1 = "<!-- 直播弹幕 -->"
	if attr == 3: string_not_used_1 = "<!-- 保护弹幕+直播弹幕 -->"
	if attr == 4: string_not_used_1 = "<!-- 高赞弹幕 -->"
	if attr == 5: string_not_used_1 = "<!-- 保护弹幕+高赞弹幕 -->"
	if attr == 6: string_not_used_1 = "<!-- 直播弹幕+高赞弹幕 -->"
	if attr == 7: string_not_used_1 = "<!-- 保护弹幕+直播弹幕+高赞弹幕 -->"

	try: action = Sub_Item["action"]		# string action = 10;
	except KeyError: pass

	try: animation = Sub_Item["animation"]	# string animation = 22;
	except KeyError: pass

	try: idstr = Sub_Item["idstr"]			# string idStr = 12;
	except KeyError: idstr = "0" # ,print("\n idstr    ERROR", 1)

	try: id_ = Sub_Item["id"]				# int64 id = 1;
	except KeyError: pass

	# if id_ != idstr:print("\n id idstr mismatch:", id_, idstr)

	try: pool = Sub_Item["pool"]			# int32 pool = 11;
	except KeyError: pool = 0
	if pool == 2: content = content.replace("\n", "\\n").replace("\r\n", "\\n")

	XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}\n".format(progress, mode, fontsize, color, ctime, pool, midHash, id_, weight, content, string_not_used_1)
	XML_Data_2nd_Cache += XML_item
	if i % Split_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
		print(f"\r进度：{i}/{danmu_count}，用时：{round(time.time()-Start_Time,4 )}",end="")

XML_Data_1st_Cache += XML_Data_2nd_Cache
XML_Data_1st_Cache += "</i>\n"
with open(outputFile, "w", encoding="utf-8")as Final_Write:
	Final_Write.write(XML_Data_1st_Cache)
	Final_Write.close()
End_Time = time.time()
print(f"\r总计用时: {round(End_Time-Start_Time, 6)}              ")
