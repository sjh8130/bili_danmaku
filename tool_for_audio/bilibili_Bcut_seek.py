#!/usr/bin/python3
import json
import sys

input_File = sys.argv[1]
SEEK_TIME = int(sys.argv[2])
output_file = input_File.rsplit(".", 1)[-2] + "_seek.json"
with open(input_File, "r", encoding="utf-8") as file_in:
    file = json.load(file_in)
for item in file["utterances"]:
    if SEEK_TIME == 0:
        break
    item["start_time"] += SEEK_TIME
    item["end_time"] += SEEK_TIME
    for words in item["words"]:
        words["start_time"] += SEEK_TIME
        words["end_time"] += SEEK_TIME
with open(output_file, "w", encoding="utf-8") as file_out:
    json.dump(file, file_out, ensure_ascii=False, separators=(",", ":"), indent="\t")
