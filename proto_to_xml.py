#!/usr/bin/python3
import sys
import time
try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2
	
from my_lib.proto2xml import proto2xml

Start_Time = time.time()

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000
XML_Data_1st_Cache = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\x0a<i>\x0a\t<chatserver>chat.bilibili.com</chatserver>\x0a\t<chatid>0</chatid>\x0a\t<mission>0</mission>\x0a\t<maxlimit>6000</maxlimit>\x0a\t<state>0</state>\x0a\t<real_name>0</real_name>\x0a\t<source>k-v</source>\x0a"
XML_Data_2nd_Cache = XML_Data_3rd_Cache = ""
i = 1

itm = dm_pb2.DmSegMobileReply()
itm.ParseFromString(open(sys.argv[1], "rb").read())

XML_Data_2nd = ""
Danmaku_Count = len(itm.elems)
for this in itm.elems:
	XML_Data_3rd_Cache += proto2xml(this, exdata=True, enable_weight=0)
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}", end="")
print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}", end="")

open(f"{sys.argv[1]}.XML", "w", encoding="utf-8").write(XML_Data_1st_Cache+XML_Data_2nd_Cache+XML_Data_3rd_Cache+f"</i>\x0a<!-- Create Time: {int(Start_Time)} -->")
End_Time = time.time()
print(f"\r{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
