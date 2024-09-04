# /dev/null

import time
from zlib import crc32


def json2XML_CMD(this: dict):
    """
    commandDms to json
    """
    # commandDms 1 / 10
    try:
        dmid = str(this["dmid"])
    except KeyError:
        try:
            dmid = str(this["id"])
        except KeyError:
            dmid = "0"

    # commandDms 2
    try:
        oid = str(this["oid"])
    except KeyError:
        try:
            oid = str(this["cid"])
        except KeyError:
            oid = "0"
    cid = oid

    mid = str(this["mid"])
    command = str(this["command"])
    text = str(this["text"])
    stime = str(this["stime"])
    ctime = str(this["ctime"])
    mtime = str(this["mtime"])
    extra = str(this["extra"])

    format_time = format(stime / 1000, ".5f")
    format_ctime = (
        time.mktime(time.strptime(ctime + "+0800", "%Y-%m-%d %H:%M:%S%z"))
        .__trunc__()
        .__str__()
    )
    format_mtime = (
        time.mktime(time.strptime(mtime + "+0800", "%Y-%m-%d %H:%M:%S%z"))
        .__trunc__()
        .__str__()
    )
    midHash = hex(crc32(mid.encode()))[2:].lstrip("0")
    return f'\t<d p="{format_time},1,25,16777215,{format_ctime},999,{midHash},{dmid},11">{text}</d><!-- SPECIAL: {command}{extra} -->\n'


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
    try:
        mode = this["mode"]
    except KeyError:
        mode = "1"
    # fontsize 4
    try:
        font_size = this["fontsize"]
    except KeyError:
        try:
            font_size = this["size"]
        except KeyError:
            font_size = "25"
    # color 5
    try:
        color = this["color"]
    except KeyError:
        color = "16777215"
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
    return (
        s.replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("&", "&amp;")
        .strip()
    )
