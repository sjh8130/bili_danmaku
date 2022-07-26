#!/usr/bin/python3
import json
import sys
import time
import gzip

def ATTR_TYPE(attr:int):
	o = ""
	b = "0000000000" + bin(attr).lstrip("0b")
	if b[-1 ] == "1": o += "保护|"
	if b[-2 ] == "1": o += "直播|"
	if b[-3 ] == "1": o += "高赞|"
	if b[-4 ] == "1": o += "壹|"
	if b[-5 ] == "1": o += "贰|"	# Y
	if b[-6 ] == "1": o += "叁|"
	if b[-7 ] == "1": o += "肆|"
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

jsonData = json.loads(infile)
infile = None
i = 1
try: cid = jsonData["info"]["cid"]
except KeyError: cid = 0
try: maxlimit = jsonData["info"]["segment_count"]*6000
except KeyError: maxlimit = 6000
danmu_count = len(jsonData["elems"])
XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\x0a<i>\x0a\t<chatserver>chat.bilibili.com</chatserver>\x0a\t<chatid>{cid}</chatid>\x0a\t<mission>0</mission>\x0a\t<maxlimit>{maxlimit}</maxlimit>\x0a\t<state>0</state>\x0a\t<real_name>0</real_name>\x0a\t<source>k-v</source>\x0a"
XML_Data_2nd_Cache = ""
XML_Data_3rd_Cache = ""
for Sub_Item in jsonData["elems"]:
	try: id_ = Sub_Item["id"]						# int64 id = 1;
	except KeyError: id_ = "0"

	# # Deduplication 20x time
	# if id_ in dedup_Table:
	# 	continue
	# dedup_Table.append(id_)

	spec_tag = ""
	try: content = Sub_Item["content"]				# string content = 7;
	except KeyError: content = ""

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

	try: sendtime = Sub_Item["ctime"]				# int64 ctime = 8;
	except KeyError: sendtime = "1262275200"

	try: ban_weight = Sub_Item["weight"]			# int32 weight = 9;
	except KeyError: ban_weight = 11

	try: attr = ATTR_TYPE(Sub_Item["attr"])			# int32 attr = 13;
	except KeyError: attr = "DM "

	try: action = Sub_Item["action"]				# string action = 10;
	except KeyError: pass

	try: animation = Sub_Item["animation"]			# string animation = 22;
	except KeyError: pass

	try: usermid = f"mid:{Sub_Item['usermid']} "	# string usermid = 14;
	except KeyError: usermid = ""

	try: likes = f"likes:{Sub_Item['likes']} "		# string likes = 15;
	except KeyError: likes = ""

	try: dm_reply = f"replies:{Sub_Item['test18']} "													# test18
	except KeyError: dm_reply = ""
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

	spec_tag = f"<!-- {attr}{usermid}{likes}{dm_reply}{dm_reply_to}-->".replace("  "," ")

	try: idStr = Sub_Item["idStr"]					# string idStr = 12;
	except KeyError: idStr = "0"
	if id_ != idStr:print("\n id idStr mismatch:", id_, idStr)

	try: pool = Sub_Item["pool"]					# int32 pool = 11;
	except KeyError: pool = 0

	progress = format(progress/1000, ".5f")
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")

	XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}\x0a".format(progress, mode, fontsize, color, sendtime, pool, midHash, id_, ban_weight, content, spec_tag)
	XML_Data_3rd_Cache += XML_item
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {1+len(dedup_Table)}|{i}/{danmu_count}, Time: {round(time.time()-Start_Time,3)}",end="")
	Sub_Item = {}

XML_Data_2nd_Cache += XML_Data_3rd_Cache
XML_Data_1st_Cache += XML_Data_2nd_Cache
XML_Data_1st_Cache += "</i>\x0a"
open(outputFile, "w", encoding="utf-8").write(XML_Data_1st_Cache)
End_Time = time.time()
print(f"\r{1+len(dedup_Table)}|{danmu_count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
