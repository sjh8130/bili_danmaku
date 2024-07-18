#!/usr/bin/python3
from google.protobuf.json_format import MessageToDict

import json
import sys

import dm_pb2

from my_lib.file_writer import FileWriter

if __name__ == "__main__":
	a = open(sys.argv[1], "rb").read()
	b = dm_pb2.DmWebViewReply()
	b.ParseFromString(a)
	data_ = json.dumps(MessageToDict(b), ensure_ascii=False, separators=(",",":"))
	FileWriter(f"{sys.argv[1]}.json", data_)
