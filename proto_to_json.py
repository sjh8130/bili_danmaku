#!/usr/bin/python3
import json
import sys
import time

from google.protobuf.json_format import MessageToDict

import dm_pb2
from my_lib.file_writer import write_file

if __name__ == "__main__":
    t1 = time.time()
    print("read")
    danmaku_binary = open(sys.argv[1], "rb").read()
    t2 = time.time()
    print("proto")
    temp_binary = dm_pb2.DmSegMobileReply()
    temp_binary.ParseFromString(danmaku_binary)
    if len(temp_binary.elems) == 0:
        print("No Data")
        sys.exit()
    t3 = time.time()
    print("json")
    j1 = MessageToDict(temp_binary)
    fw = json.dumps(j1, ensure_ascii=False, separators=(",", ":"))
    fw = fw.replace('},{"id"', '},\x0a{"id"').replace(',"test20":"0"', "").replace(',"test21":"0"', "").replace(',"test25":"1"', "")
    temp_binary = None
    t4 = time.time()
    print("write")
    write_file(f"{sys.argv[1]}.json", fw)
    t5 = time.time()
    print(f"ALL:{t5-t1}, Write: {t5-t4}, Json: {t4-t3}, Proto: {t3-t2}, Read: {t2-t1}")
