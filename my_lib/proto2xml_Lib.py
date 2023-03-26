#!/dev/null
from my_lib.attr import Danmaku_ATTR_TYPE
try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2


def fp(a: str, b: int): return f"{a}:{b} " if b else ""


def proto2xml(this: dm_pb2.DanmakuElem, extra_data: bool, enable_weight: bool = False):
	"""
	Text
	"""
	Ext_Data = ""
	content = this.content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
	if enable_weight: weight = this.weight
	else: weight = "9"
	# action = this.action
	# animation = this.animation
	if extra_data: Ext_Data = f"<!-- {Danmaku_ATTR_TYPE(this.attr)}{fp('mid', this.usermid)}{fp('Likes', this.likes)}{fp('Reply', this.reply_count)} -->".replace("  ", " ")
	return f"\t<d p=\"{format(this.progress/1000, '.5f')},{this.mode},{this.fontsize},{this.color},{this.ctime},{this.pool},{this.midHash},{this.id},{weight}\">{content}</d>{Ext_Data}\n"
