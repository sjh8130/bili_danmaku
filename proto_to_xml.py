#!/usr/bin/python3
import os
import sys
import time

import dm_pb2

from my_lib.proto2xml_Lib import proto_to_xml
from my_lib.file_writer import write_file

st = time.time()
lmt = os.stat(sys.argv[1]).st_mtime

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000
fs = """<?xml version="1.0" encoding="UTF-8"?>
<i>
	<chatserver>chat.bilibili.com</chatserver>
	<chatid>_MARK_FOR_SEARCH_</chatid>
	<mission>0</mission>
	<maxlimit>6000</maxlimit>
	<state>0</state>
	<real_name>0</real_name>
	<source>k-v</source>
"""
fe = f"</i>\n<!-- Create Time: {int(lmt)} -->"
cache_1 = ""
cache_2 = ""
cache_3 = ""

i = 0

itm = dm_pb2.DmSegMobileReply()
itm.ParseFromString(open(sys.argv[1], "rb").read())

count = len(itm.elems)
if count == 0:
    # cache_1 += '<d p="0.00000,1,25,16776960,1660114514,9,ffffffff,99999999,9">_MARK_FOR_SEARCH_</d>\n'
    print("No Data")
    sys.exit()
for this in itm.elems:
    cache_3 += proto_to_xml(this, extra_data=True, enable_weight=True)
    i += 1
    if i % SPLIT_3RD_SIZE == 0:
        cache_1 += cache_2
        cache_2 = ""
    if i % SPLIT_2ND_SIZE == 0:
        cache_2 += cache_3
        cache_3 = ""
        print(f"\rProgress: {i}/{count}, Time: {round(time.time()-st,3)}", end="")
print(f"\rProgress: {i}/{count}, Time: {round(time.time()-st,3)}")

write_file(f"{sys.argv[1]}.xml", fs + cache_1 + cache_2 + cache_3 + fe)

et = time.time()
print(f"\r{count}, 总计用时：{round(et-st, 4)}                     ")
