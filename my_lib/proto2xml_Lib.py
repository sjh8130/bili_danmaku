#!/dev/null
import dm_pb2


def proto_to_xml(this: dm_pb2.DanmakuElem) -> str:
	"""
	Text
	"""
	if content == "":
		return ""
	content = this.text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
	return f"\t<d p=\"{format(this.stime/1000, '.5f')},{this.mode},{this.size},{this.color},{this.date},{this.pool},{this.uhash},{this.id},{this.weight}\">{content}</d>\n"
