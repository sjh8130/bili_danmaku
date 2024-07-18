#/dev/null

def json2XML(this:dict):
	"""
	Text
	"""
	try: mode = this["mode"]
	except KeyError: mode = "1"
	try: color = this["color"]
	except KeyError: color = "16777215"
	try: pool = this["pool"]
	except KeyError: pool = "0"
	try: weight = this["weight"]
	except KeyError: weight = "9"
	try: id_ = str(this["id"])
	except KeyError: id_ = "FAKE"
	try: progress: int = this["progress"]
	except KeyError: progress = 0
	try: fontsize = this["fontsize"]
	except KeyError: fontsize = "25"
	try: midHash = this["midHash"]
	except KeyError: midHash = "ffffffff"
	try: content = this["content"]
	except KeyError: content = ""
	try: sendtime = this["ctime"]
	except KeyError: sendtime = "1262275200"
	if content == "": return ""
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace( "\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\x0a", "\\n").replace("\x0d", "\\r")
	return f"\t<d p=\"{format(progress/1000, '.5f')},{mode},{fontsize},{color},{sendtime},{pool},{midHash},{id_},{weight}\">{content}</d>\n"
