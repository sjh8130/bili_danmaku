#!/usr/bin/env python
"""
Read a mitmproxy dump file.
"""

import enum
import json
import struct
import sys
import zlib
from typing import NamedTuple

import brotli
from mitmproxy import dns, http, io
from mitmproxy.exceptions import FlowReadException

HEADER_STRUCT = struct.Struct(">I2H2I")


class AuthReplyCode(enum.IntEnum):
    OK = 0
    TOKEN_ERROR = -101


class ProtoVer(enum.IntEnum):
    NORMAL = 0
    HEARTBEAT = 1
    DEFLATE = 2
    BROTLI = 3


class Operation(enum.IntEnum):
    HANDSHAKE = 0
    HANDSHAKE_REPLY = 1
    HEARTBEAT = 2
    HEARTBEAT_REPLY = 3
    SEND_MSG = 4
    SEND_MSG_REPLY = 5
    DISCONNECT_REPLY = 6
    AUTH = 7
    AUTH_REPLY = 8
    RAW = 9
    PROTO_READY = 10
    PROTO_FINISH = 11
    CHANGE_ROOM = 12
    CHANGE_ROOM_REPLY = 13
    REGISTER = 14
    REGISTER_REPLY = 15
    UNREGISTER = 16
    UNREGISTER_REPLY = 17


class HeaderTuple(NamedTuple):
    pack_len: int
    raw_header_size: int
    protover: int
    operation: Operation
    seq_id: int


def jld(a: str | dict) -> str:
    if isinstance(a, dict):
        return json.dumps(a, ensure_ascii=False, separators=(",", ":"))
    return json.dumps(json.loads(a), ensure_ascii=False, separators=(",", ":"))


def unpack_2(data: bytes) -> list[str]:
    if len(data) <= 16:
        return []
    lst = []
    offset = 0
    try:
        header = HeaderTuple(*HEADER_STRUCT.unpack_from(data, offset))
    except struct.error:
        return []
    while True:
        body = data[offset + header.raw_header_size : offset + header.pack_len]
        lst.append(jld(body.decode("utf-8")))
        offset += header.pack_len
        if offset >= len(data):
            break
        try:
            header = HeaderTuple(*HEADER_STRUCT.unpack_from(data, offset))
        except struct.error:
            break
    return lst


def _parse_business_message(header: HeaderTuple, body: bytes) -> list[str]:
    ret: str = ""
    if header.operation == Operation.HEARTBEAT:  # 2
        return [jld({"cmd": "HEARTBEAT", "data": str(body[16:], "utf-8")})]
    if header.operation == Operation.HEARTBEAT_REPLY:  # 3
        return [jld({"cmd": "HEARTBEAT_REPLY", "popularity": int.from_bytes(body[16:20], "big"), "data": str(body[20:], "utf-8")})]
    if header.operation == Operation.SEND_MSG_REPLY:  # 5
        if header.protover == ProtoVer.BROTLI:
            body = brotli.decompress(body)
            return unpack_2(body)
        if header.protover == ProtoVer.DEFLATE:
            body = zlib.decompress(body)
            return unpack_2(body)
        if header.protover == ProtoVer.NORMAL:
            if len(body) != 0:
                try:
                    ret = jld(body.decode("utf-8"))
                    return [ret]
                except Exception as e:
                    print(e)
                    return [repr(body)]
        else:
            ret = repr(body)
    elif header.operation in {Operation.AUTH, Operation.AUTH_REPLY}:  # 7
        ret = jld(body.decode("utf-8"))
    else:
        ret = repr(body)
    return [ret]


def decode_blc(data: bytes) -> list[str]:
    if len(data) <= 16:
        return []
    lst: list = []
    offset = 0
    try:
        header = HeaderTuple(*HEADER_STRUCT.unpack_from(data, offset))
    except struct.error:
        return lst
    if header.operation == Operation.HEARTBEAT:  # 2
        return [jld({"cmd": "HEARTBEAT", "data": str(data[16:], "utf-8")})]
    if header.operation == Operation.HEARTBEAT_REPLY:  # 3
        return [jld({"cmd": "HEARTBEAT_REPLY", "popularity": int.from_bytes(data[16:20], "big"), "data": str(data[20:], "utf-8")})]
    while True:
        body = data[offset + header.raw_header_size : offset + header.pack_len]
        lst += _parse_business_message(header, body)
        offset += header.pack_len
        if offset >= len(data):
            break
        try:
            header = HeaderTuple(*HEADER_STRUCT.unpack_from(data, offset))
        except struct.error:
            break
    return lst


def main():
    with open(sys.argv[1], "rb") as logfile:
        freader = io.FlowReader(logfile)
        try:
            for frame in freader.stream():
                if isinstance(frame, http.HTTPFlow):
                    if frame.request.method == "POST":
                        continue
                    if frame.websocket:
                        if "live-comet" in frame.request.headers.get(b"Host", "") and "chat.bilibili.com" in frame.request.headers.get(b"Host", ""):
                            pass
                        else:
                            continue
                        frame_uuid = frame.id
                        for seq, msg in enumerate(frame.websocket.messages):
                            if msg.from_client and seq == 0:
                                continue
                            if msg.content:
                                pass
                                # continue
                            ts = (str(msg.timestamp).replace(".", "") + "00000000")[:16]
                            dms = decode_blc(msg.content)
                            if dms == ['{"code":0}'] or dms == ['{"code": 0}']:
                                continue
                            if not dms:
                                continue
                            with open(f"{frame_uuid}.jsonl", "a", encoding="utf-8") as fp:
                                fp.writelines((ts + dm + "\n") for dm in dms)
                        print(frame.request.get_state())
                        print(frame)
                elif isinstance(frame, dns.DNSFlow):
                    pass
            # print(f)
            # break
        except FlowReadException as e:
            print(f"Flow file corrupted: {e}")


if __name__ == "__main__":
    main()
