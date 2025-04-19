#!/usr/bin/python3
import json
import os
import sys
import time
import gzip

try:
    import simdjson
except ImportError:
    simdjson = json
from my_lib.file_writer import write_file
from my_lib.json2xml import json2XML, json2XML_CMD


def main():
    start_time = time.time()
    in_path = sys.argv[1]
    with open(in_path, "rb") as fp:
        preload = fp.read(4)
    with open(in_path, "rb") as fp:
        if preload.startswith(b'{"el'):
            data = simdjson.load(fp)
        elif preload.startswith(b"\xeb\xbb\xbf"):
            data = simdjson.load(fp)
        elif preload.startswith(b"\x1f\x8b"):
            with gzip.open(fp, "r", encoding="utf-8") as gfp:
                data = simdjson.load(gfp)
        else:
            raise
    try:
        cid = 0
    except KeyError:
        cid = 0
    try:
        max_limit = 0 * 6000
    except KeyError:
        max_limit = 6000
    xml_head = f"""<?xml version="1.0" encoding="UTF-8"?>
<i>
\t<chatserver>chat.bilibili.com</chatserver>
\t<chatid>{cid}</chatid>
\t<mission>0</mission>
\t<maxlimit>{max_limit}</maxlimit>
\t<state>0</state>
\t<real_name>0</real_name>
\t<source>k-v</source>
"""
    xml_data = []
    last_modified_time = int(os.stat(in_path).st_ctime)
    xml_tail = f"</i>\n<!-- Create Time: {last_modified_time} -->"
    try:
        commandDms_count = len(data["commandDms"])
    except KeyError:
        commandDms_count = 0
    try:
        danmaku_count = len(data["elems"])
    except KeyError:
        danmaku_count = 0
    if danmaku_count == 0 and commandDms_count == 0:
        print("No Data")
        sys.exit()
    if commandDms_count > 0:
        for this in data["commandDms"]:
            xml_data.append(json2XML_CMD(this))
    for this in data["elems"]:
        xml_data.append(json2XML(this))
    write_file(in_path + ".xml", xml_head + "\n".join(xml_data) + xml_tail)
    end_time = time.time()
    print(f"\r{danmaku_count=:10}, 总计用时：{round(end_time-start_time, 4):10}")


if __name__ == "__main__":
    main()
