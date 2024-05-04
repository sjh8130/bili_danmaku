#!/usr/bin/python3
import sys
import json

input_File = sys.argv[1]
SEEK_TIME = int(sys.argv[2])

output_SEEK = input_File.rsplit(".", 1)[-2]+"_seek.json"
with open(input_File, "r", encoding="utf-8") as file_in:
	Loaded_JSON = json.load(file_in)

for item in Loaded_JSON["utterances"]:
	if SEEK_TIME == 0:
		break
	item["start_time"], item["end_time"] += SEEK_TIME
	for sub_item in item["words"]:
		sub_item["start_time"], sub_item["end_time"] += SEEK_TIME

with open(output_SEEK, "w", encoding="utf-8") as file_out:
	json.dump(Loaded_JSON, file_out, ensure_ascii=False, separators=(",", ":"), indent="\t")
