# /dev/null
import time
from typing import Any
from zlib import crc32

_ERR_STR = "ERROR"


def json2XML_CMD(this: dict[str, Any]) -> str:
    """CommandDms to xml."""
    # commandDms 1 / 10
    dmid_1 = str(this.get("id", _ERR_STR))
    dmid_2 = str(this.get("dmid", _ERR_STR))
    if dmid_1 == _ERR_STR and dmid_2 == _ERR_STR:
        ...
    elif dmid_1 == _ERR_STR and dmid_2 != "0":
        dmid_1 = dmid_2
    elif dmid_1 != "0" and dmid_2 == _ERR_STR:
        dmid_2 = dmid_1
    elif dmid_1 != "0" and dmid_2 not in {"0", dmid_1}:
        print("[json2XML]: dmid_1 != oid")
    # commandDms 2
    oid = str(this.get("oid", _ERR_STR))
    cid = str(this.get("cid", _ERR_STR))
    if cid == _ERR_STR and oid == _ERR_STR:
        ...
    elif cid == _ERR_STR and oid != "0":
        cid = oid
    elif cid != "0" and oid == _ERR_STR:
        oid = cid
    elif cid != "0" and oid not in {"0", cid}:
        print("[json2XML]: cid != oid")
    mid = str(this.get("mid", "0"))
    command = str(this.get("command", ""))
    text = str(this.get("text", ""))
    stime = int(this.get("stime", "0"))
    ctime = str(this.get("ctime", "0"))
    # mtime = str(this.get("mtime", "0"))
    extra = str(this.get("extra", ""))
    f_time = format(stime / 1000, ".5f")
    f_ctime = str(time.mktime(time.strptime(ctime + "+0800", "%Y-%m-%d %H:%M:%S%z")))
    # f_mtime = time.mktime(time.strptime(mtime + "+0800", "%Y-%m-%d %H:%M:%S%z")).__floor__().__str__()
    midHash = hex(crc32(mid.encode()))[2:].lstrip("0")  # noqa: FURB116
    return f'\t<d p="{f_time},1,25,16777215,{f_ctime},999,{midHash},{dmid_2},11">{text}</d><!-- SPECIAL: {command}{extra} -->'


def json2XML(this: dict[str, Any]) -> str:
    # dmid 1 / 12
    dmid = str(this.get("id", this.get("idStr", this.get("dmid", "FAKE"))))
    # showtime 2
    stime_ = this.get("ctime", this.get("stime", 0))
    stime = format(stime_ / 1000, ".5f")
    # mode 3
    mode = this.get("mode", "1")
    # fontsize 4
    font_size = this.get("fontsize", this.get("size", "25"))
    # color 5
    color = this.get("color", "16777215")
    # midHash 6
    mid_hash = this.get("midHash", this.get("uhash", "ffffffff"))
    # content 7
    content = this.get("content", this.get("text", ""))
    if content == "":  # noqa: PLC1901
        return ""
    content = escape_html(content)
    # send_time 8
    send_time = this.get("ctime", this.get("date", "1262275200"))
    # weight 9
    weight = this.get("weight", "9")
    # pool 11
    pool = this.get("pool", "0")
    return f'\t<d p="{stime},{mode},{font_size},{color},{send_time},{pool},{mid_hash},{dmid},{weight}">{content}</d>'


def escape_html(s: str) -> str:
    return s if s == "" else s.replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("&", "&amp;").strip()  # noqa: PLC1901
