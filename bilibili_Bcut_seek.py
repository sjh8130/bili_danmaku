#!/usr/bin/python3
import json
import sys
import time
import logging

input_File = sys.argv[1]
SEEK_TIME = int(sys.argv[2])

output_SEEK = input_File.rsplit(".", 1)[-2]+"_seek.json"
input_File = open(input_File, "r", encoding="utf-8").read()

Loaded_JSON = json.loads(input_File)
del input_File
if Loaded_JSON["version"] != "v1.3.1":
	logging.warning("not supported")
	time.sleep(5)

for item in Loaded_JSON["utterances"]:
	item["start_time"]+=SEEK_TIME
	item["end_time"]+=SEEK_TIME
	for sub_item in item["words"]:
		sub_item["start_time"]+=SEEK_TIME
		sub_item["end_time"]+=SEEK_TIME
	...

output_content = json.dumps(Loaded_JSON, ensure_ascii=False, separators=(",", ":"), indent="\t")
# print(output_content)
open(output_SEEK, "w", encoding="utf-8").write(output_content)
