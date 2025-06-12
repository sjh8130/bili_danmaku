#!/usr/bin/python3
import os
import sys
import time

import dm_pb2
from my_lib.file_writer import write_file
from my_lib.proto2xml_Lib import proto_to_xml


def main(file_name) -> None:
    st = time.time()
    lmt = os.stat(file_name).st_mtime
    xml_head = """<?xml version="1.0" encoding="UTF-8"?>
<i>
\t<chatserver>chat.bilibili.com</chatserver>
\t<chatid>_MARK_FOR_SEARCH_</chatid>
\t<mission>0</mission>
\t<maxlimit>6000</maxlimit>
\t<state>0</state>
\t<real_name>0</real_name>
\t<source>k-v</source>
"""
    xml_tail = f"</i>\n<!-- Create Time: {int(lmt)} -->"
    itm = dm_pb2.DmSegMobileReply()
    with open(file_name, "rb") as fp:
        itm.ParseFromString(fp.read())
    count = len(itm.elems)
    if count == 0:
        # cache_1 += '<d p="0.00000,1,25,16776960,1660114514,9,ffffffff,99999999,9">_MARK_FOR_SEARCH_</d>\n'
        print("No Data")
        sys.exit()
    list_dm = [proto_to_xml(x) for x in itm.elems]
    write_file(f"{file_name}.xml", xml_head + "\n".join(list_dm) + xml_tail)
    et = time.time()
    print(f"\r{count}, 总计用时：{round(et - st, 4)}                     ")


if __name__ == "__main__":
    for _i in sys.argv[1:]:
        main(_i)
