#!/dev/null
from my_lib.attr import DanmakuAttrType
try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2


def fp(a: str, b: int): return f"{a}:{b} " if b else ""


def Proto2XML(this: dm_pb2.DanmakuElem, extra_data: bool, enable_weight: bool = False):
	"""
	Text
	"""
	Ext_Data = ""
	content = this.text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
	if enable_weight: weight = this.weight
	else: weight = "9"
	# action = this.action
	# animation = this.animation
	if extra_data: Ext_Data = f"<!-- {DanmakuAttrType(this.attr)}{fp('mid', this.usermid)}{fp('Likes', this.likes)}{fp('Reply', this.reply_count)} -->".replace("  ", " ")
	return f"\t<d p=\"{format(this.stime/1000, '.5f')},{this.mode},{this.size},{this.color},{this.date},{this.pool},{this.uhash},{this.id},{weight}\">{content}</d>{Ext_Data}\n"
