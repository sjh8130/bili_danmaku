#!/usr/bin/python3
import json
import sys
import time
import gzip
import os
import binascii
from my_lib.json2xml import json2xml

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

try: Last_Modified_Time = int(Loaded_JSON['info']['File_Create_Time'])
except KeyError: Last_Modified_Time = int(os.stat(input_File).st_ctime)

compatible_1:bool = False
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
		try: progress = Item_sp["progress"]	# int32 progress = 6;
		except KeyError: progress = 0
		ctime = Item_sp["ctime"]			# string ctime = 7;
		mtime = Item_sp["mtime"]			# string mtime = 8;
		extra = Item_sp["extra"]			# string extra = 9;
		idStr = Item_sp["idStr"]			# string idStr = 10
		sendtime = int(time.mktime(time.strptime(ctime, '%Y-%m-%d %H:%M:%S')))
		midHash = hex(binascii.crc32(mid.encode())^0xFFFFFFFF).lstrip("0x").lstrip("0")
		XML_Data_1st_Cache += f"\t<d p=\"{format(progress/1000, '.5f')},1,25,16777215,{sendtime},999,{midHash},{id_},11\">{content}</d><!-- SPECIAL: {command}{extra} -->\x0a"

for this in Loaded_JSON["elems"]:
	XML_Data_3rd_Cache += json2xml(this, True, False)
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}",end="")
	this = {}

open(outputFile, "w", encoding="utf-8").write(XML_Data_1st_Cache+XML_Data_2nd_Cache+XML_Data_3rd_Cache+f"</i>\x0a<!-- Create Time: {Last_Modified_Time} -->")
End_Time = time.time()
print(f"\r{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
