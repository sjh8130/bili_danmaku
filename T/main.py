#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson

import dm_pb2

import json
import sys
import time
import gzip
import io

if __name__ == '__main__':
	time1 = time.time()

	Danmaku_Binary = open(sys.argv[1], "rb").read()

	time2 = time.time()

	Temp_Binary = dm_pb2.DmSegMobileReply()
	Temp_Binary.ParseFromString(Danmaku_Binary)

	time3 = time.time()

	Write_Data = json.dumps(json.loads(MessageToJson(Temp_Binary)), ensure_ascii=False)

	time4 = time.time()

	open("out.json", 'w', encoding='utf-8').write(Write_Data.replace("}, {\"id\"", "},\x0a{\"id\""))
	# io.TextIOWrapper(gzip.open("out.json.gz",'wb'),encoding='utf-8').writelines(Write_Data)
	time5 = time.time()

	print(f"ALL:{time5-time1}, Write: {time5-time4}, Json: {time4-time3}, Proto: {time3-time2}, Read: {time2-time1}")
