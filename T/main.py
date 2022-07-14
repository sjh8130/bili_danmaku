#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson
import json
import dm_pb2
import sys
import time

if __name__ == '__main__':
	time1 = time.time()

	with open(sys.argv[1], "rb") as inp:
		Danmaku_Binary = inp.read()

	time2 = time.time()

	Temp_Binary = dm_pb2.DmSegMobileReply()
	Temp_Binary.ParseFromString(Danmaku_Binary)

	time3 = time.time()

	Write_Data = json.dumps(json.loads(MessageToJson(Temp_Binary)), ensure_ascii=False)

	time4 = time.time()

	with open("out.json", "w", encoding="utf-8") as f:
		f.write(Write_Data)

	time5 = time.time()

	print(f"ALL:{time5-time1}, Write: {time5-time4}, Json: {time4-time3}, Proto: {time3-time2}, Read: {time2-time1}")