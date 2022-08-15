from my_lib.attr import Danmaku_ATTR_TYPE
try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2


def fp(a: str, b: int): return f"{a}:{b} " if b else ""


def proto2xml(this: dm_pb2.DanmakuElem, exdata: bool, enable_weight: bool = False, All_Default: bool = False):
	"""
	Text
	"""
	Extended_Data = ""
	id_ = this.id
	content = this.content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
	idStr = this.idStr
	if str(id_) != idStr: print("[Proto2XML]: id&idStr mismatch:", id_, idStr)
	if All_Default:
		mode = "1"
		fontsize = "25"
		color = "16777215"
		pool = "0"
		weight = "9"
	else:
		mode = this.mode
		fontsize = this.fontsize
		color = this.color
		pool = this.pool
		if enable_weight: weight = this.weight
		else: weight = "9"
		action = this.action
		animation = this.animation
		if exdata: Extended_Data = f"<!-- {Danmaku_ATTR_TYPE(this.attr)}{fp('mid', this.usermid)}{fp('Likes', this.likes)}{fp('Reply', this.reply_count)} -->".replace("  ", " ")
	return f"\t<d p=\"{format(this.progress/1000, '.5f')},{mode},{fontsize},{color},{this.ctime},{pool},{this.midHash},{id_},{weight}\">{content}</d>{Extended_Data}\n"
