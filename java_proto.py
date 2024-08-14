import re
from functools import lru_cache


PFC = ['public', 'final', 'class']
PFC2 = ['public', 'static', 'final', 'class']
PFU = ['public', 'enum']
ITM = ['public', 'static', 'final', 'int']
MSG = "message"
ENUM = "enum"


@lru_cache
def camel_to_snake_improved(name):
    a = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    b = re.sub('([a-z0-9])([A-Z])', r'\1_\2', a)
    c = re.sub('([A-Za-z])([0-9]+)', r'\1_\2', b)
    return c.lower()


@lru_cache
def get_type(a: str):
    match a:
        case "String" | "StringValue": return "string"

        case "UInt32Value" | "UInt32Value" | "UInt32Value": return "uint32"
        case "UInt64Value" | "UInt64Value" | "UInt64Value": return "uint64"

        case "int" | "Integer" | "Int32Value": return "int32"
        case "long" | "Long" | "Int64Value": return "int64"

        case "Internal.IntList": return "repeated int32"
        case "Internal.LongList": return "repeated int64"

        case "Internal.FloatList": return "repeated float"
        case "Internal.FloatList": return "repeated float"

        case "FloatValue": return "float"
        case "DoubleValue": return "double"

        case "boolean" | "BoolValue": return "bool"
        case "ByteString" | "BytesValue": return "bytes"
        case _:
            if a.startswith("Internal.ProtobufList"):
                return "repeated " + get_type(a[22:-1])
            elif a.startswith("MapFieldLite"):
                b = a[13:-1].split(",")
                return "map<" + get_type(b[0]) + ", " + get_type(b[1]) + ">"
            else:
                return a


def combine_msg(s1, s2):
    sort_s1_l = []
    form_s2 = []
    ret_str = ""
    for i in s1:
        sort_s1_l.append(i[1])
    sort_s1_l = sorted(sort_s1_l)
    for i in s2:
        form_s2.append([camel_to_snake_improved(i[0]), get_type(i[1]), i[0]])
    for i in sort_s1_l:
        ret_str += "    //\n    "
        for j in s1:
            if j[1] == i:
                for k in form_s2:
                    if j[0] == k[0]:
                        ret_str += f"{k[1]} {j[0]} = {j[1]};"
                    elif j[0] == k[2].lower():
                        ret_str += f"{k[1]} {k[2]} = {j[1]};"
        ret_str += "\n"
    return ret_str


def combine_enum(s1):
    sort_s1_l = []
    ret_str = ""
    for i in s1:
        sort_s1_l.append(i[1])
    sort_s1_l = sorted(sort_s1_l)
    for i in sort_s1_l:
        for j in s1:
            if i == j[1]:
                ret_str += f"    {j[0][0:-6]} = {j[1]}; // \n"
    return ret_str


def process(data):
    msg_type = ""
    name = ""
    s1 = []
    s2 = []
    i: str
    for i in data:
        strs = i.rstrip(";").split(" ")
        if msg_type == "":
            if strs[0:3] == PFC:
                msg_type = MSG
                name = strs[3]
            elif strs[0:4] == PFC2:
                msg_type = MSG
                name = strs[4]
            elif strs[0:2] == PFU:
                msg_type = ENUM
                name = strs[2]
            continue
        elif msg_type == MSG:
            if strs[0:4] == ITM:
                s1.append([strs[4][0:-13].lower(), int(strs[6])])
            elif strs[0] == "private":
                if len(strs) != 3 and strs[4] == "DEFAULT_INSTANCE":
                    continue
                elif strs[2] == "volatile":
                    continue
                else:
                    s2.append([strs[2].rstrip("_"), strs[1]])
        elif msg_type == ENUM:
            if strs[0:4] == ITM:
                s1.append([strs[4], strs[6]])
    print("=============")
    print("\n//")
    if msg_type == MSG:
        combine_str = combine_msg(s1, s2)
        print(f"{msg_type} {name} "+"{")
        print(combine_str, end="")
        print("}\n")
    elif msg_type == ENUM:
        combine_str = combine_enum(s1)
        print(f"{msg_type} {name} "+"{")
        print(combine_str, end="")
        print("}\n")


def main():
    in_strings: list[str] = []
    while True:
        a = input().replace(", ", ",").strip()
        if a == "clean":
            in_strings = []
        elif a == "/* compiled from: BL */":
            process(in_strings)
            in_strings = []
        else:
            in_strings.append(a)


if __name__ == "__main__":
    main()
