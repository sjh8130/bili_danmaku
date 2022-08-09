#!/usr/bin/python3
import json
import sys
import time
import gzip
import os
import binascii

from my_lib.json2xml import json2xml
from my_lib.file_writer import writeE

Start_Time = time.time()
input_File = sys.argv[1]
if open(input_File, "rb").read(1) == b"\x7b":
	infile = open(input_File, "r", encoding="utf-8").read()
if open(input_File, "rb").read(2) == b"\x1f\x8b":
	infile = gzip.open(input_File, "rb").read()

outputFile = input_File.rstrip(".gz").rstrip(".json").rstrip(".bin")+".xml"

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000

Loaded_JSON = json.loads(infile)
del infile
i = 1
try: cid = Loaded_JSON["info"]["cid"]
except KeyError: cid = 0
try: Max_Limit = Loaded_JSON["info"]["segment_count"]*6000
except KeyError: Max_Limit = 6000
XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\x0a<i>\x0a\t<chatserver>chat.bilibili.com</chatserver>\x0a\t<chatid>{cid}</chatid>\x0a\t<mission>0</mission>\x0a\t<maxlimit>{Max_Limit}</maxlimit>\x0a\t<state>0</state>\x0a\t<real_name>0</real_name>\x0a\t<source>k-v</source>\x0a"
XML_Data_2nd_Cache = XML_Data_3rd_Cache = ""

try: Last_Modified_Time = int(Loaded_JSON['info']['File_Create_Time'])
except KeyError: Last_Modified_Time = int(os.stat(input_File).st_ctime)

try: commandDms_Len = len(Loaded_JSON["commandDms"])
except KeyError: commandDms_Len = 0

try: Danmaku_Count = len(Loaded_JSON["elems"])
except KeyError: Danmaku_Count = 0
if Danmaku_Count == 0 and commandDms_Len ==0: print("No Data"),sys.exit()

if commandDms_Len != 0:
	for this in Loaded_JSON["commandDms"]:
		id_ = this["id"]					# int64 id = 1
		oid = this["oid"]				# int64 oid = 2;
		mid = this['mid']				# int64 mid = 3;
		command = this["command"]		# string command = 4;
		content = this["content"]		# string content = 5;
		try: progress = this["progress"]	# int32 progress = 6;
		except KeyError: progress = 0
		ctime = this["ctime"]			# string ctime = 7;
		mtime = this["mtime"]			# string mtime = 8;
		extra = this["extra"]			# string extra = 9;
		idStr = this["idStr"]			# string idStr = 10
		sendtime = int(time.mktime(time.strptime(ctime, '%Y-%m-%d %H:%M:%S')))
		midHash = hex(binascii.crc32(mid.encode())^0xFFFFFFFF).lstrip("0x").lstrip("0")
		XML_Data_1st_Cache += f"\t<d p=\"{format(progress/1000, '.5f')},1,25,16777215,{sendtime},999,{midHash},{id_},11\">{content}</d><!-- SPECIAL: {command}{extra} -->\x0a"
	del this
for this in Loaded_JSON["elems"]:
	XML_Data_3rd_Cache += json2xml(this, True, 0)
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}",end="")
	del this

writeE(outputFile, XML_Data_1st_Cache+XML_Data_2nd_Cache+XML_Data_3rd_Cache+f"</i>\x0a<!-- Create Time: {Last_Modified_Time} -->")
End_Time = time.time()
print(f"\r{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
