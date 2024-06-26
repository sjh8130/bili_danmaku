#!/usr/bin/python3
import json
import sys
import time
import gzip
import os
import binascii

from my_lib.json2xml_Lib import json2XML

Start_Time = time.time()
input_File = sys.argv[1]

with open(input_File, "rb")as file_in:
	preload = file_in.read(3)
	if preload[0] == b"\x7b":
		Loaded_JSON = json.load(file_in)
	if preload == b"\xeb\xbb\xbf":
		Loaded_JSON = json.load(file_in)
	if preload == b"\x1f\x8b\x08":
		infile = str(gzip.open(input_File, "rb").read(), encoding="utf-8")

outputFile = input_File.rstrip(".gz").rstrip(".json").rstrip(".bin")+".xml"

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000

Loaded_JSON = json.loads(infile)
del infile
i = 1

try: cid = Loaded_JSON["info"]["cid"]
except KeyError: cid = 0
try: dmk_Ver = Loaded_JSON["info"]["dmk_Ver"]
except KeyError: dmk_Ver = 0

try: Max_Limit = Loaded_JSON["info"]["segment_count"]*6000
except KeyError: Max_Limit = 6000

XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>{Max_Limit}</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
XML_Data_2nd_Cache = XML_Data_3rd_Cache = ""

try: Last_Modified_Time = int(Loaded_JSON["info"]["File_Create_Time"])
except KeyError: Last_Modified_Time = int(os.stat(input_File).st_ctime)

try: commandDms_Len = len(Loaded_JSON["commandDms"])
except KeyError: commandDms_Len = 0

try: Danmaku_Count = len(Loaded_JSON["elems"])
except KeyError: Danmaku_Count = 0

if Danmaku_Count == 0 and commandDms_Len == 0:
	# XML_Data_2nd_Cache = '<d p="0.00000,1,25,16776960,1660114514,9,ffffffff,99999999,9">_MARK_FOR_SEARCH_</d>\n'
	print("No Data")
	sys.exit()

# try: is_live_record: bool = Loaded_JSON["info"]["is_live_record"]
# except KeyError: is_live_record: bool = False

if commandDms_Len != 0:
	for this in Loaded_JSON["commandDms"]:
		if dmk_Ver in [0, 1, 2, 3]:
			try: stime = this["progress"]
			except KeyError: stime = 0
		elif dmk_Ver in [4]:
			try: stime = this["stime"]
			except KeyError: stime = 0

		XML_Data_1st_Cache += f"\t<d p=\"{format(stime/1000, '.5f')},1,25,16777215,{int(time.mktime(time.strptime(this['ctime'], '%Y-%m-%d %H:%M:%S')))},999,{hex(binascii.crc32(str(this['mid']).encode())^0xFFFFFFFF).lstrip('0x').lstrip('0')},{this['id']},11\">{this['content']}</d><!-- SPECIAL: {this['command']}{this['extra']} -->\n"
	del this
for this in Loaded_JSON["elems"]:
	XML_Data_3rd_Cache += json2XML(this=this, exdata=True, enable_weight=True, dmk_Ver=dmk_Ver)
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}", end="")

with open(outputFile, "r", encoding="utf-8")as file_out:
	file_out.write(XML_Data_1st_Cache + XML_Data_2nd_Cache + XML_Data_3rd_Cache + f"</i>\n<!-- Create Time: {Last_Modified_Time} -->")

End_Time = time.time()
print(f"\r{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
