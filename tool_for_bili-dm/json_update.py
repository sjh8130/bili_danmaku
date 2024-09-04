#!/usr/bin/python3
import json
import sys

input_File = sys.argv[1]
infile = open(input_File, "r", encoding="utf-8").read()
outputFile = "update_" + input_File

j1 = json.loads(infile)
is_live_record = False

for this in j1["elems"]:

    try:
        if this["attr"] == 2 and (not is_live_record):
            is_live_record = True
    except KeyError:
        pass

    this["usermid"] = int(this["usermid"])
    if j1["info"]["dmk_Ver"] in [1, 2, 3]:
        this["ctime"] = int(this["ctime"])
        this["stime"] = this["progress"]
        try:
            del this["progress"]
        except KeyError:
            ...

        try:
            del this["fontsize"]
            this["size"] = this["fontsize"]
        except KeyError:
            ...

        this["uhash"] = this["midHash"]
        try:
            del this["midHash"]
        except KeyError:
            ...

        this["text"] = this["content"]
        try:
            del this["content"]
        except KeyError:
            ...

        this["date"] = this["ctime"]
        try:
            del this["ctime"]
        except KeyError:
            ...

        this["dmid"] = this["id"]
        try:
            del this["id"]
        except KeyError:
            ...

    elif j1["info"]["dmk_Ver"] in [4]:
        try:
            if this["size"] == 25:
                del this["size"]
        except KeyError:
            this["size"] = 0

    try:
        if this["test20"] == "0":
            del this["test20"]
    except KeyError:
        pass
    try:
        if this["test21"] == "0":
            del this["test21"]
    except KeyError:
        pass
    try:
        if this["mode"] == 1:
            del this["mode"]
    except KeyError:
        this["mode"] = 0
    try:
        if this["color"] == 16777215:
            del this["color"]
    except KeyError:
        this["color"] = 0
    try:
        del this["likes"]
    except KeyError:
        pass
    try:
        del this["weight"]
    except KeyError:
        pass

j1_info = {}
j1_info["Ver"] = "V6_20230601"
j1_info["dmk_Ver"] = 4
################
try:
    j1_info["owner"] = j1["info"]["owner"]
except KeyError:
    j1_info["owner"] = {}

    try:
        j1_info["owner"]["mid"] = str(j1["info"]["owner_mid"])
    except KeyError:
        j1_info["owner"]["mid"] = "0"

    try:
        j1_info["owner"]["name"] = j1["info"]["owner_name"]
    except KeyError:
        j1_info["owner"]["name"] = ""

    j1_info["owner"]["face"] = ""
################
try:
    j1_info["bvid"] = j1["info"]["bvid"]
except KeyError:
    j1_info["bvid"] = ""
################
try:
    j1_info["avid"] = j1["info"]["avid"]
except KeyError:
    j1_info["avid"] = 0
################
try:
    j1_info["V_Name"] = j1["info"]["V_Name"]
except KeyError:
    j1_info["V_Name"] = ""
################
try:
    j1_info["pubdate"] = j1["info"]["pubdate"]
except KeyError:
    j1_info["pubdate"] = 0
################
try:
    j1_info["ctime"] = j1["info"]["ctime"]
except KeyError:
    try:
        j1_info["ctime"] = j1["info"]["i_ctime"]
    except KeyError:
        j1_info["ctime"] = 0
################
try:
    j1_info["P_Name"] = j1["info"]["P_Name"]
except KeyError:
    j1_info["P_Name"] = ""
################
j1_info["cid"] = j1["info"]["cid"]
j1_info["duration"] = j1["info"]["duration"]
j1_info["segment_count"] = j1["info"]["segment_count"]
################
try:
    j1_info["danmaku_count"] = j1["info"]["danmaku_count"]
except KeyError:
    j1_info["danmaku_count"] = len(j1["elems"])
################
try:
    j1_info["danmaku_web_reported"] = j1["info"]["danmaku_web_reported"]
except KeyError:
    j1_info["danmaku_web_reported"] = 0
################
try:
    j1_info["danmaku_proto_reported"] = j1["info"]["danmaku_proto_reported"]
except KeyError:
    j1_info["danmaku_proto_reported"] = 0
################
try:
    j1_info["File_Create_Time"] = j1["info"]["File_Create_Time"]
except KeyError:
    j1_info["File_Create_Time"] = 0
# V4
try:
    j1_info["File_Create_Time_Start"] = j1["info"]["File_Create_Time_Start"]
except KeyError:
    j1_info["File_Create_Time_Start"] = j1["info"]["File_Create_Time"]
################
j1_info["is_live_record"] = is_live_record

try:
    del j1["File_Ver"]
except KeyError:
    pass

j1["info"] = j1_info
with open(outputFile, "w", encoding="utf-8") as file_out:
    file_out.write(
        json.dumps(j1, ensure_ascii=False, separators=(",", ":")).replace(
            '},{"id"', '},\n{"id"'
        )
    )
