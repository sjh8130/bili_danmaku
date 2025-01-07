#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# mypy: ignore-errors
import re

import string
import sys

from enum import StrEnum

import pyperclip


def camel_to_snake_improved(name: str) -> list[str]:
    """将 camelCase 格式的字符串转换为 snake_case 格式。"""
    a = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    b = re.sub("([a-z0-9])([A-Z])", r"\1_\2", a)
    c = re.sub("([a-zA-Z])([0-9])", r"\1_\2", b)
    d = re.sub("([0-9])([A-Z])", r"\1_\2", c)
    # sys.stderr("\n")
    # sys.stderr(f"{name= }" + "\n")
    # sys.stderr(f"{a= }" + "\n")
    # sys.stderr(f"{b= }" + "\n")
    # sys.stderr(f"{c= }" + "\n")
    # sys.stderr(f"{d= }" + "\n")
    return [a, b, c, d, a.lower(), b.lower(), c.lower(), d.lower()]


PROTO_DICT = {
    "StringValue": "google.protobuf.StringValue",
    "FloatValue": "google.protobuf.FloatValue",
    "DoubleValue": "google.protobuf.DoubleValue",
    "BoolValue": "google.protobuf.BoolValue",
    "BytesValue": "google.protobuf.BytesValue",
    "UInt32Value": "google.protobuf.UInt32Value",
    "UInt64Value": "google.protobuf.UInt64Value",
    "Int32Value": "google.protobuf.Int32Value",
    "Int64Value": "google.protobuf.Int64Value",
    "Any": "google.protobuf.Any",
    "Api": "google.protobuf.Api",
    "BoolValue": "google.protobuf.BoolValue",
    "BytesValue": "google.protobuf.BytesValue",
    "DoubleValue": "google.protobuf.DoubleValue",
    "Duration": "google.protobuf.Duration",
    "Empty": "google.protobuf.Empty",
    "Enum": "google.protobuf.Enum",
    "EnumValue": "google.protobuf.EnumValue",
    "Field": "google.protobuf.Field",
    "FieldMask": "google.protobuf.FieldMask",
    "FloatValue": "google.protobuf.FloatValue",
    "Int32Value": "google.protobuf.Int32Value",
    "Int64Value": "google.protobuf.Int64Value",
    "ListValue": "google.protobuf.ListValue",
    "Method": "google.protobuf.Method",
    "Mixin": "google.protobuf.Mixin",
    "NullValue": "google.protobuf.NullValue",
    "Option": "google.protobuf.Option",
    "SourceContext": "google.protobuf.SourceContext",
    "StringValue": "google.protobuf.StringValue",
    "Struct": "google.protobuf.Struct",
    "Syntax": "google.protobuf.Syntax",
    "Timestamp": "google.protobuf.Timestamp",
    "Type": "google.protobuf.Type",
    "UInt32Value": "google.protobuf.UInt32Value",
    "UInt64Value": "google.protobuf.UInt64Value",
    "Value": "google.protobuf.Value",
    "String": "string",
    "int": "int32",
    "Integer": "int32",
    "long": "int64",
    "Long": "int64",
    "Internal.IntList": "repeated int32",
    "Internal.LongList": "repeated int64",
    "Internal.FloatList": "repeated float",
    "Internal.DoubleList": "repeated double",
    "Internal.StringList": "repeated string",
    "Internal.BytesList": "repeated bytes",
    "ByteString": "bytes",
    "boolean": "bool",
}


def get_protobuf_type(a: str) -> str:
    """根据输入字符串返回相应的数据类型。"""
    if a in PROTO_DICT:
        return PROTO_DICT[a]
    if a.startswith("Internal.ProtobufList"):
        return "repeated {0}".format(get_protobuf_type(a[22:-1]))
    elif a.startswith("MapFieldLite"):
        b = a[13:-1].split(",")
        return "map<{0}, {1}>".format(get_protobuf_type(b[0]), get_protobuf_type(b[1]))
    else:
        return a


def combine_msg(list_1: list[tuple[str, int]], list_2: list[str]) -> str:
    ids = []
    form_s2: list[str] = []
    ret_str = ""
    for i in list_1:
        ids.append(i[1])
    sorted_ids = sorted(ids)
    for i in list_2:
        form_s2.append([camel_to_snake_improved(i[0])[5], get_protobuf_type(i[1]), i[0]])
    for i in sorted_ids:
        ret_str += "    //\n    "
        for j in list_1:
            if j[1] == i:
                for k in form_s2:
                    if j[0] == k[0]:
                        ret_str += f"{k[1]} {j[0]} = {j[1]};"
                    elif j[0] == k[2].lower():
                        ret_str += f"{k[1]} {k[2]} = {j[1]};"
        ret_str += "\n"
    return ret_str


def combine_enum(list_1: list[tuple[str, int]]) -> str:
    ids = []
    ret_str = ""
    for id in list_1:
        ids.append(id[1])
    ids = sorted(ids)
    for id in ids:
        for j in list_1:
            if id == j[1] and id != -1:
                ret_str += f"    {j[0][0:-6]} = {j[1]};\n"
    for id in ids:
        for j in list_1:
            if id == j[1] and id == -1:
                ret_str += f"    {j[0][0:-6]} = {j[1]};\n"
                return ret_str
    return ret_str


def snake_to_camel(name: str) -> str:
    """将 snake_case 格式的字符串转换为 camelCase 格式。"""
    return "".join(name.split("_"))


def combine_rpc(list_1: list[tuple[str, int]], list_2: tuple[str, str, str]) -> str:
    #                              ^                         rpc_req*,rpc_reply*,rpc_name*
    #                             rpc_name(CAMEL,UPPER),rpc_index*
    index = []
    ret_str: str = ""
    idx: int
    for _, idx in list_1:
        index.append(idx)
    index = sorted(index)
    for rpc_index in index:
        for list1_idx in list_1:
            if rpc_index == list1_idx[1]:
                for rpc_req, rpc_reply, rpc_name in list_2:
                    if rpc_name.lower() == snake_to_camel(list1_idx[0]).lower():
                        ret_str += f"\n    //\n    rpc {rpc_name} ({rpc_req}) returns ({rpc_reply});"
    return ret_str


class MsgType(StrEnum):
    enum = "enum"
    message = "message"
    service = "service"
    none = ""


def process(data: list[str]):
    E_L = ["", "", "", "", "", "", "", "", "", ""]
    msg_type = MsgType.none
    msg_name = ""
    final_str = ""
    list_1 = []
    list_2 = []
    for i in data:
        if i.startswith("/*"):
            continue
        strs: list[str] = i.strip().replace(", ", ",").rstrip(";").split(" ") + E_L
        if msg_type == MsgType.none:
            if strs[:3] == ["public", "final", "class"] and strs[4] == "extends" and strs[6] == "implements":
                msg_type = MsgType.message
                msg_name = strs[3]
            elif strs[:4] == ["public", "static", "final", "class"]:
                msg_type = MsgType.message
                msg_name = strs[4]
            elif strs[:2] == ["public", "enum"]:
                msg_type = MsgType.enum
                msg_name = strs[2]
            elif strs[:3] == ["public", "final", "class"] and strs[3] in string.ascii_letters:
                msg_type = MsgType.service
            elif strs[:4] == ["private", "static", "final", "int"] and strs[4].startswith("METHODID_"):
                msg_type = MsgType.service
        elif msg_type == MsgType.message:
            if strs[:5] == ["public", "static", "final", "String", "SERVICE_NAME"]:
                msg_type = MsgType.service
                msg_name = strs[6][1:-1]
                continue

            if strs[:4] == ["public", "static", "final", "int"]:
                list_1.append([strs[4][0:-13].lower(), int(strs[6])])
            elif strs[0] == "private":
                if strs[:3] == ["private", "static", "final"] and strs[4] == "DEFAULT_INSTANCE":
                    msg_name = strs[3]
                elif strs[:3] == ["private", "static", "volatile"] and strs[4].startswith("PARSER"):
                    ...
                else:
                    list_2.append([strs[2].rstrip("_"), strs[1]])
        elif msg_type == MsgType.enum:
            if strs[:4] == ["public", "static", "final", "int"]:
                list_1.append([strs[4], int(strs[6])])
        elif msg_type == MsgType.service:
            if strs[:5] == ["public", "static", "final", "String", "SERVICE_NAME"]:
                msg_name = strs[6][1:-1].split(".")[-1]
            elif strs[:4] == ["private", "static", "final", "int"]:
                list_1.append([strs[4][9:], int(strs[6])])
            elif strs[:4] == ["private", "static", "volatile", "x0"]:
                pass
            elif strs[:3] == ["private", "static", "volatile"] and strs[3].startswith("MethodDescriptor"):
                list_2.append(strs[3][17:-1].split(",") + [strs[4][3:-6]])

    if msg_type == MsgType.message:
        final_str += f"""
//
{MsgType.message} {msg_name} \x7b
{combine_msg(list_1, list_2)}\x7d
"""
    elif msg_type == MsgType.enum:
        final_str += f"""
//
{MsgType.enum} {msg_name} \x7b
{combine_enum(list_1)}\x7d
"""
    elif msg_type == MsgType.service:
        final_str += f"""
//
{MsgType.service} {msg_name} \x7b{combine_rpc(list_1, list_2)}
\x7d
"""
    if final_str:
        print(final_str)
        pyperclip.copy(final_str)
    else:
        sys.stderr.write("no data found\n")


def main():
    in_strings: list[str] = []
    paste = False
    while True:
        paste = False
        a = input().replace(", ", ",").strip()
        if a == "clean":
            in_strings.clear()
        elif a == "/* compiled from: BL */":
            process(in_strings)
            in_strings.clear()
        elif a.startswith("/* loaded from:"):
            continue
        elif a == "" and len(in_strings) == 0:
            if not paste:
                paste = True
                process(pyperclip.paste().splitlines())
                in_strings.clear()
        else:
            in_strings.append(a)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr("exit")
        pass
