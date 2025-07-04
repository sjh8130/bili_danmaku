#!/usr/bin/python3
import json
import sys
from pathlib import Path

from google.protobuf.json_format import MessageToDict

import dm_pb2
from my_lib.file_writer import write_file

if __name__ == "__main__":
    a = Path(sys.argv[1]).read_bytes()
    b = dm_pb2.DmWebViewReply()
    b.ParseFromString(a)
    data_ = json.dumps(MessageToDict(b), ensure_ascii=False, separators=(",", ":"))
    write_file(f"{sys.argv[1]}.json", data_)
