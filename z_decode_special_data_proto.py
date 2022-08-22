#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson

import json
import sys

try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

from my_lib.file_writer import writeER

if __name__ == '__main__':
	Danmaku_Binary = open(sys.argv[1], "rb").read()
	Temp_Binary = dm_pb2.DmWebViewReply()
	Temp_Binary.ParseFromString(Danmaku_Binary)
	data_ = json.dumps(json.loads(MessageToJson(Temp_Binary, indent=0)), ensure_ascii=False, separators=(',',':'))
	writeER(f"{sys.argv[1]}.json", data_)
