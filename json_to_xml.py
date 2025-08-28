#!/usr/bin/python3
import gzip
import json
import os
import sys
import time
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json
from my_lib.file_writer import write_file
from my_lib.json2xml import json2XML, json2XML_CMD


def main(file_name: Path) -> None:
    start_time = time.time()
    with file_name.open("rb") as fp:
        preload = fp.read(4)
        fp.seek(0)
        if preload.startswith((b'{"el', b"\xeb\xbb\xbf")):
            data = simdjson.load(fp)
        elif preload.startswith(b"\x1f\x8b"):
            with gzip.open(fp, "r", encoding="utf-8") as gfp:
                data = simdjson.load(gfp)
        else:
            raise  # noqa: PLE0704
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
    last_modified_time = int(os.stat(file_name).st_ctime)
    xml_tail = f"</i>\n<!-- Create Time: {last_modified_time} -->"
    try:
        command_dms_count = len(data["commandDms"])
    except KeyError:
        command_dms_count = 0
    try:
        danmaku_count = len(data["elems"])
    except KeyError:
        danmaku_count = 0
    if danmaku_count == 0 and command_dms_count == 0:
        print("No Data")
        sys.exit()
    if command_dms_count > 0:
        for this in data["commandDms"]:
            xml_data.append(json2XML_CMD(this))
    for this in data["elems"]:
        xml_data.append(json2XML(this))
    write_file(file_name.with_suffix(".xml"), xml_head + "\n".join(xml_data) + xml_tail)
    end_time = time.time()
    print(f"\r{danmaku_count=:10}, 总计用时：{round(end_time - start_time, 4):10}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(Path(p))
