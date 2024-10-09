#!/dev/null
import dm_pb2


def proto_to_xml(this: dm_pb2.DanmakuElem) -> str:
    """
    Text
    """
    content = this.content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
    if not content:
        return ""
    return f"\t<d p=\"{(this.progress/1000):.5f},{this.mode},{this.fontsize},{this.color},{this.ctime},{this.pool},{this.midHash},{this.id},{this.weight}\">{content}</d>\n"
