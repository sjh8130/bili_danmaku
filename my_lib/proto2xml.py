from my_lib.attr import Danmaku_ATTR_TYPE
try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2


def fp(a: str, b: int): return f"{a}:{b} " if b else ""


def proto2xml(this: dm_pb2.DanmakuElem, exdata: bool, enable_weight: int = 0):
	Extended_Data = ""
	id_ = this.id
	progress = this.progress
	mode = this.mode
	fontsize = this.fontsize
	color = this.color
	midHash = this.midHash
	content = this.content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
	sendtime = this.ctime
	if enable_weight: weight = this.weight
	else: weight = "9"
	action = this.action
	pool = this.pool
	idStr = this.idStr
	attr = Danmaku_ATTR_TYPE(this.attr)
	usermid = fp("mid", this.usermid)
	likes = fp("Likes", this.likes)
	reply_count = fp("Reply", this.reply_count)
	animation = this.animation
	this = None
	if str(id_) != idStr: print("[XML]: id&idStr mismatch:", id_, idStr)
	if exdata: Extended_Data = f"<!-- {attr}{usermid}{likes}{reply_count} -->".replace("  ", " ")
	return f"\t<d p=\"{format(progress/1000, '.5f')},{mode},{fontsize},{color},{sendtime},{pool},{midHash},{id_},{weight}\">{content}</d>{Extended_Data}\x0a"
