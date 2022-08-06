#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson
try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2

import json
import sys
import time
import gzip
import io

if __name__ == '__main__':
	time1 = time.time()
	print("read")
	Danmaku_Binary = open(sys.argv[1], "rb").read()

	time2 = time.time()
	print("proto")
	Temp_Binary = dm_pb2.DmSegMobileReply()
	Temp_Binary.ParseFromString(Danmaku_Binary)

	time3 = time.time()
	print("json")
	Write_Data = json.dumps(json.loads(MessageToJson(Temp_Binary, indent=0, ensure_ascii=False)), ensure_ascii=False)
	Temp_Binary = None
	time4 = time.time()
	print("write")
	open(f"{sys.argv[1]}.json", 'w', encoding='utf-8').write(Write_Data.replace("}, {\"id\"", "},\x0a{\"id\"").replace(", \"test20\": \"0\", \"test21\": \"0\"", ""))
	# io.TextIOWrapper(gzip.open(f"{sys.argv[1]}.json.gz",'wb'), encoding='utf-8').writelines(Write_Data)
	time5 = time.time()

	print(f"ALL:{time5-time1}, Write: {time5-time4}, Json: {time4-time3}, Proto: {time3-time2}, Read: {time2-time1}")
