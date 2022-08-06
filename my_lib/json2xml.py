from my_lib.attr import Danmaku_ATTR_TYPE


def json2xml(this, exdata, enable_weight: int = 0):
	try: id_ = this["id"]
	except KeyError: id_ = "FAKE"
	Extra_Data = ""
	try: progress: int = this["progress"]
	except KeyError: progress = 0
	try: mode: int = this["mode"]
	except KeyError: mode = 1
	try: fontsize = this["fontsize"]
	except KeyError: fontsize = 25
	try: color = this["color"]
	except KeyError: color = 0
	try: midHash = this["midHash"]
	except KeyError: midHash = "ffffffff"
	try: content = this["content"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace( "\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
	except KeyError: content = ""
	try: sendtime = this["ctime"]
	except KeyError: sendtime = "1262275200"
	try: weight = this["weight"]
	except KeyError: weight = "9"
	if not enable_weight: weight = "9"
	try: action = this["action"]
	except KeyError: action = ""
	try: pool = this["pool"]
	except KeyError: pool = 0
	try: idStr = this["idStr"]
	except KeyError: idStr = "0"
	try: attr = Danmaku_ATTR_TYPE(this["attr"])
	except KeyError: attr = "DM "
	try: usermid = f"mid:{this['usermid']} "
	except KeyError: usermid = ""
	try: likes = f"Likes:{this['likes']} "
	except KeyError: likes = ""
	try: animation = this["animation"]
	except KeyError: animation = ""
	if id_ != idStr: print("id idStr mismatch:", id_, idStr)
	try: replyCount = f"Reply:{this['replyCount']} "
	except KeyError: replyCount = ""
	try: t16 = f"reply_to:{this['test16']} "
	except KeyError: t16 = "0"
	try: t17 = f"reply_to:{this['test17']} "
	except KeyError: t17 = "0"
	try: t20 = f"reply_to:{this['test20']} "
	except KeyError: t20 = "0"
	try: t21 = f"reply_to:{this['test21']} "
	except KeyError: t21 = "0"
	dm_reply_to = proc_4(t16,t17,t20,t21)
	if exdata: Extra_Data = f"<!-- {attr}{usermid}{likes}{replyCount}{dm_reply_to}-->".replace("  ", " ")
	return f"\t<d p=\"{format(progress/1000, '.5f')},{mode},{fontsize},{color},{sendtime},{pool},{midHash},{id_},{weight}\">{content}</d>{Extra_Data}\x0a"

def proc_4(a,b,c,d):
	if a!=b:
		print(f"[XML_reply2]:mismatch_int:{a}|{b}")
		return f"{a}|{b}|{c}|{d} "
	if c!=d:
		print(f"[XML_reply2]:mismatch_str:{c}|{d}")
		return f"{a}|{b}|{c}|{d} "
	if a!=c and c!="0":
		print(f"[XML_reply2]:mismatch_int-str{a}|{c}")
		return f"{a}|{b}|{c}|{d} "
	if a!="0":
		return f"{a} "
	else:
		return ""