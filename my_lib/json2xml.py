# /dev/null

import time
from zlib import crc32

_ERR_STR = "ERROR"


def json2XML_CMD(this: dict):
    """
    commandDms to xml
    """
    # commandDms 1 / 10
    dmid_1 = str(this.get("id", _ERR_STR))
    dmid_2 = str(this.get("dmid", _ERR_STR))
    if dmid_1 == _ERR_STR and dmid_2 == _ERR_STR:
        ...
    elif dmid_1 == _ERR_STR and dmid_2 != "0":
        dmid_1 = dmid_2
    elif dmid_1 != "0" and dmid_2 == _ERR_STR:
        dmid_2 = dmid_1
    elif dmid_1 != "0" and dmid_2 != "0" and dmid_1 != dmid_2:
        raise ValueError("dmid_1 != oid")

    # commandDms 2
    oid = str(this.get("oid", _ERR_STR))
    cid = str(this.get("cid", _ERR_STR))
    if cid == _ERR_STR and oid == _ERR_STR:
        ...
    elif cid == _ERR_STR and oid != "0":
        cid = oid
    elif cid != "0" and oid == _ERR_STR:
        oid = cid
    elif cid != "0" and oid != "0" and cid != oid:
        raise ValueError("cid != oid")

    mid = str(this.get("mid", "0"))
    command = str(this.get("command", ""))
    text = str(this.get("text", ""))
    stime = int(this.get("stime", "0"))
    ctime = str(this.get("ctime", "0"))
    mtime = str(this.get("mtime", "0"))
    extra = str(this.get("extra", ""))

    format_time = format(stime / 1000, ".5f")
    format_ctime = time.mktime(time.strptime(ctime + "+0800", "%Y-%m-%d %H:%M:%S%z")).__floor__().__str__()
    format_mtime = time.mktime(time.strptime(mtime + "+0800", "%Y-%m-%d %H:%M:%S%z")).__floor__().__str__()
    midHash = hex(crc32(mid.encode()))[2:].lstrip("0")
    return f'\t<d p="{format_time},1,25,16777215,{format_ctime},999,{midHash},{dmid_2},11">{text}</d><!-- SPECIAL: {command}{extra} -->\n'


def json2XML(this: dict):
    """
    Text
    """
    # dmid 1 / 12
    try:
        dmid = str(this["dmid"])
    except KeyError:
        try:
            dmid = str(this["id"])
        except KeyError:
            try:
                dmid = str(this["idStr"])
            except KeyError:
                dmid = "FAKE"
    # showtime 2
    try:
        showtime = this["ctime"]
    except KeyError:
        try:
            showtime = this["stime"]
        except KeyError:
            showtime = 0
    stime = format(showtime / 1000, ".5f")
    # mode 3
    mode = this.get("mode", "1")
    # fontsize 4
    try:
        font_size = this["fontsize"]
    except KeyError:
        try:
            font_size = this["size"]
        except KeyError:
            font_size = "25"
    # color 5
    color = this.get("color", "16777215")
    # midHash 6
    try:
        mid_hash = this["midHash"]
    except KeyError:
        try:
            mid_hash = this["uhash"]
        except KeyError:
            mid_hash = "ffffffff"
    # content 7
    try:
        content = this["content"]
    except KeyError:
        try:
            content = this["text"]
        except KeyError:
            content = ""
    content = escape_html(content)
    if content == "":
        return ""
    # send_time 8
    try:
        send_time = this["ctime"]
    except KeyError:
        try:
            send_time = this["date"]
        except KeyError:
            send_time = "1262275200"
    # weight 9
    try:
        weight = this["weight"]
    except KeyError:
        weight = "9"
    # pool 11
    try:
        pool = this["pool"]
    except KeyError:
        pool = "0"
    return f'\t<d p="{stime},{mode},{font_size},{color},{send_time},{pool},{mid_hash},{dmid},{weight}">{content}</d>\n'


def escape_html(s: str) -> str:
    if s == "":
        return s
    return s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("&", "&amp;").strip()
