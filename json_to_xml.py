#!/usr/bin/python3
import json
import sys
import time
import os

from my_lib.json2xml import json2XML, json2XML_CMD
from my_lib.file_writer import write_file

start_time = time.time()
in_path = sys.argv[1]

with open(in_path, "rb") as fl:
	preload = fl.read(4)

with open(in_path, "rb") as file_in:
	if preload == b'{"el':
		data = json.load(file_in)
	elif preload == b"\xeb\xbb\xbf":
		data = json.load(file_in)
	elif preload[0:2] == b"\x1f\x8b":
		import gzip

		tmp1 = str(gzip.open(in_path, "rb").read(), encoding="utf-8")
		data = json.loads(tmp1)
		del tmp1

out_path = in_path.rstrip(".gz").rstrip(".json").rstrip(".bin") + ".xml"

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000

i = 1

try:
	cid = 0
except KeyError:
	cid = 0

try:
	max_limit = 0 * 6000
except KeyError:
	max_limit = 6000

xml_cache_layer_1 = f"""<?xml version="1.0" encoding="UTF-8"?>
<i>
	<chatserver>chat.bilibili.com</chatserver>
	<chatid>{cid}</chatid>
	<mission>0</mission>
	<maxlimit>{max_limit}</maxlimit>
	<state>0</state>
	<real_name>0</real_name>
	<source>k-v</source>
"""
xml_cache_layer_2 = ""
xml_cache_layer_3 = ""

last_modified_time = int(os.stat(in_path).st_ctime)

try:
	commandDms_count = len(data["commandDms"])
except KeyError:
	commandDms_count = 0

try:
	danmaku_count = len(data["elems"])
except KeyError:
	danmaku_count = 0

if danmaku_count == 0 and commandDms_count == 0:
	# xml_cache_layer_2 = '<d p="0.00000,1,25,16776960,1660114514,9,ffffffff,99999999,9">_MARK_FOR_SEARCH_</d>\n'
	print("No Data")
	sys.exit()

if commandDms_count > 0:
	for this in data["commandDms"]:
		xml_cache_layer_1 += json2XML_CMD(this)
	del this
for this in data["elems"]:
	xml_cache_layer_3 += json2XML(this)
	i += 1
	if i % SPLIT_2ND_SIZE == 0:
		xml_cache_layer_2 += xml_cache_layer_3
	if i % SPLIT_3RD_SIZE == 0:
		xml_cache_layer_1 += xml_cache_layer_2
		xml_cache_layer_2 = ""
		print(
			f"\rProgress: {i}/{danmaku_count}, Time: {round(time.time()-start_time,3)}",
			end="",
		)

write_file(
	out_path,
	xml_cache_layer_1
	+ xml_cache_layer_2
	+ xml_cache_layer_3
	+ f"</i>\n<!-- Create Time: {last_modified_time} -->",
)

end_time = time.time()
print(
	f"\r{danmaku_count}, 总计用时：{round(end_time-start_time, 4)}                     "
)
