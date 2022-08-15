#!/usr/bin/python3
import sys
import time

try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

from my_lib.proto2xml_Lib import proto2xml
from my_lib.file_writer import writeE

Start_Time = time.time()

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000
XML_Data_1st_Cache = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>0</chatid>\n\t<mission>0</mission>\n\t<maxlimit>6000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
XML_Data_2nd_Cache = XML_Data_3rd_Cache = ""
i = 1

itm = dm_pb2.DmSegMobileReply()
itm.ParseFromString(open(sys.argv[1], "rb").read())

XML_Data_2nd = ""
Danmaku_Count = len(itm.elems)
if Danmaku_Count == 0:
	print("No Data")
	sys.exit()
for this in itm.elems:
	XML_Data_3rd_Cache += proto2xml(this, exdata=True, enable_weight=True)
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}", end="")
print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}")

writeE(f"{sys.argv[1]}.XML", XML_Data_1st_Cache+XML_Data_2nd_Cache+XML_Data_3rd_Cache+f"</i>\n<!-- Create Time: {int(Start_Time)} -->")
End_Time = time.time()
print(f"\r{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
