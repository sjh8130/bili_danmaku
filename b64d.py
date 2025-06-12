import binascii
import enum
import getpass
import json
import struct
import sys
import zlib
from typing import NamedTuple

import brotli  # type: ignore[import-untyped]

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


def jld(a: str) -> str:
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
        lst.append((str(header)) + jld(body))
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
        return [f"[HEARTBEAT]: {header}{str(body[20:], 'utf-8')}"]
    if header.operation == Operation.HEARTBEAT_REPLY:  # 3
        return [f"[HEARTBEAT_REPLY]: {header}{str(body[20:], 'utf-8')}"]
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
        ret = (str(header)) + jld(body.decode("utf-8"))
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
        return [f"[HEARTBEAT]: {str(data[16:], 'utf-8')}|{header}"]
    if header.operation == Operation.HEARTBEAT_REPLY:  # 3
        return [f"[HEARTBEAT_REPLY]: {str(data[20:], 'utf-8')},popularity:{int.from_bytes(data[16:20], 'big')}|{header}"]
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


def decode_input() -> None:
    while True:
        try:
            a = bytes(getpass.getpass("请输入数据: "), "utf-8")
            if a in {b"", ""}:
                continue
            print("\033[1;41;33m ############################## \033[0m")
            try:
                b = binascii.a2b_hex(a)
            except binascii.Error:
                b = binascii.a2b_base64(a)
            c = decode_blc(b)
            for i in c:
                print(i)
            print("\033[1;42;33m ############################## \033[0m")
        except Exception as ex:
            print(f"处理时发生错误: {ex}")


if __name__ == "__main__":
    try:
        decode_input()
    except KeyboardInterrupt:
        sys.exit(0)
