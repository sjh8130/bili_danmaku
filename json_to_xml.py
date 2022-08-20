#!/usr/bin/python3
import json
import sys
import time
import gzip
import os
import binascii

from my_lib.json2xml_Lib import json2xml
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

XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>{Max_Limit}</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
XML_Data_2nd_Cache = XML_Data_3rd_Cache = ""

try: Last_Modified_Time = int(Loaded_JSON['info']['File_Create_Time'])
except KeyError: Last_Modified_Time = int(os.stat(input_File).st_ctime)

try: commandDms_Len = len(Loaded_JSON["commandDms"])
except KeyError: commandDms_Len = 0

try: Danmaku_Count = len(Loaded_JSON["elems"])
except KeyError: Danmaku_Count = 0

if Danmaku_Count == 0 and commandDms_Len ==0: print("No Data"),sys.exit()

# try: is_live_record: bool = Loaded_JSON["info"]["is_live_record"]
# except KeyError: is_live_record: bool = False

if commandDms_Len != 0:
	for this in Loaded_JSON["commandDms"]:
		id_ = this["id"]
		# oid = this["oid"]
		mid = str(this['mid'])
		command = this["command"]
		content = this["content"]
		try: progress = this["progress"]
		except KeyError: progress = 0
		ctime = this["ctime"]
		# mtime = this["mtime"]
		extra = this["extra"]
		# idStr = this["idStr"]
		midHash = hex(binascii.crc32(mid.encode())^0xFFFFFFFF).lstrip("0x").lstrip("0")
		XML_Data_1st_Cache += f"\t<d p=\"{format(progress/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(ctime, '%Y-%m-%d %H:%M:%S')))},999,{midHash},{id_},11\">{content}</d><!-- SPECIAL: {command}{extra} -->\n"
	del this
for this in Loaded_JSON["elems"]:
	XML_Data_3rd_Cache += json2xml(this=this, exdata=False, enable_weight=True)
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}",end="")
	del this

writeE(outputFile, XML_Data_1st_Cache+XML_Data_2nd_Cache+XML_Data_3rd_Cache+f"</i>\n<!-- Create Time: {Last_Modified_Time} -->")
End_Time = time.time()
print(f"\r{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
