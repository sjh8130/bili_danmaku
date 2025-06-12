#!/usr/bin/python3
import json
import sys

from google.protobuf.json_format import MessageToDict

import dm_pb2
from my_lib.file_writer import write_file


def main():
    d: dict
    dms = dm_pb2.DmSegMobileReply()
    with open(sys.argv[1], "rb") as fp:
        dms.ParseFromString(fp.read())
    if len(dms.elems) == 0:
        print("No Data")
        sys.exit(1)
    j1 = MessageToDict(dms)
    del dms
    for d in j1["elems"]:
        d.pop("test20", None)
        d.pop("test21", None)
        d.pop("type", None)
    fw = json.dumps(j1, ensure_ascii=False, separators=(",", ":"))
    fw = fw.replace('},{"id"', '},\n\t{"id"')
    write_file(f"{sys.argv[1]}.json", fw)


if __name__ == "__main__":
    main()
