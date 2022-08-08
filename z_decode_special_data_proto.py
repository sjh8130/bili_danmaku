#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson
try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2

import json
import sys

if __name__ == '__main__':
	Danmaku_Binary = open(sys.argv[1], "rb").read()
	Temp_Binary = dm_pb2.DmWebViewReply()
	Temp_Binary.ParseFromString(Danmaku_Binary)
	Write_Data = str(MessageToJson(Temp_Binary, indent=0, ensure_ascii=False))
	open(f"{sys.argv[1]}.json", 'w', encoding='utf-8').write(Write_Data)
