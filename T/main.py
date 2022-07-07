#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson
import json
import dm_pb2
import sys

if __name__ == '__main__':
	with open(sys.argv[1], "rb") as inp:
		Danmaku_Binary = inp.read()
	Temp_Binary = dm_pb2.DmSegMobileReply()
	Temp_Binary.ParseFromString(Danmaku_Binary)
	Write_Data = json.dumps(json.loads(MessageToJson(Temp_Binary)), ensure_ascii=False)
	with open("File_Name", "w", encoding="utf-8") as f:
		f.write(Write_Data)
