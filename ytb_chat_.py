#!/usr/bin/python3
import json
import sys
from time import time

input_File = sys.argv[1]
outputFile = input_File+".json"


class outFileDesc:
    type: str
    time_: int
    text: str
    SC_price: int
    SC_currency: str
    emoji_id: str


out_file_content = {
    "chats": [],
    "emoji": {},
    "info": {
        "video_id": "",
        "create_time": time().__trunc__}
}

with open(input_File, "r", encoding="utf-8") as infile:
    for lines in infile.readlines():
        items = json.loads(lines)
        for item in items:
            out_file_content["chats"].append()
