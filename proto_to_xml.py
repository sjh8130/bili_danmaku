#!/usr/bin/python3
import sys
import time
try:
	import zzzz as dm_pb2
except ModuleNotFoundError:
	import dm_pb2
Start_Time = time.time()

def Danmaku_ATTR_TYPE(attr: int):
	if attr == 0: return "DM "
	o = ""
	b = "00000000000000000000000000000000" + bin(attr).lstrip("0b")
	if b[-1 ] == "1": o += "保护 "
	if b[-2 ] == "1": o += "直播 "
	if b[-3 ] == "1": o += "高赞 "
	if b[-4 ] == "1": o += "壹 "
	if b[-5 ] == "1": o += "贰 "
	if b[-6 ] == "1": o += "叁 "
	if b[-7 ] == "1": o += "肆 "
	if b[-8 ] == "1": o += "伍 "
	if b[-9 ] == "1": o += "陆 "
	if b[-10] == "1": o += "柒 "
	if b[-11] == "1": o += "捌 "
	if b[-12] == "1": o += "玖 "
	if b[-13] == "1": o += "拾 "
	if b[-14] == "1": o += "拾壹 "
	return o

def fp(a:str,b:int): return f"{a}:{b} " if b else ""

SPLIT_2ND_SIZE = 4000
SPLIT_3RD_SIZE = 40000
XML_Data_1st_Cache = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\x0a<i>\x0a\t<chatserver>chat.bilibili.com</chatserver>\x0a\t<chatid>0</chatid>\x0a\t<mission>0</mission>\x0a\t<maxlimit>6000</maxlimit>\x0a\t<state>0</state>\x0a\t<real_name>0</real_name>\x0a\t<source>k-v</source>\x0a"
XML_Data_2nd_Cache = ""
XML_Data_3rd_Cache = ""
i = 1

try: input_File = sys.argv[1]
except IndexError:
	print("No Input")
	sys.exit(1)

itm = dm_pb2.DmSegMobileReply()
itm.ParseFromString(open(input_File, "rb").read())

this:dm_pb2.DanmakuElem
XML_Data_2nd = ""
Danmaku_Count = len(itm.elems)
for this in itm.elems:
	Extended_Data = ""
	id_ = this.id
	progress = this.progress
	mode = this.mode
	fontsize = this.fontsize
	color = this.color
	midHash = this.midHash
	content = this.content
	sendtime = this.ctime
	weight = this.weight
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
	Extended_Data = f"<!-- {attr}{usermid}{likes}{reply_count} -->".replace("  ", " ")
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x00", " ").replace("\x08", " ").replace("\x14", " ").replace("\x17", " ").replace("\n", "\\n").replace("\r", "\\r")
	XML_Data_3rd_Cache += f"\t<d p=\"{format(progress/1000, '.5f')},{mode},{fontsize},{color},{sendtime},{pool},{midHash},{id_},{weight}\">{content}</d>{Extended_Data}\x0a"
	i += 1
	if i % SPLIT_3RD_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
	if i % SPLIT_2ND_SIZE == 0:
		XML_Data_2nd_Cache += XML_Data_3rd_Cache
		XML_Data_3rd_Cache = ""
		print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}",end="")
print(f"\rProgress: {i}/{Danmaku_Count}, Time: {round(time.time()-Start_Time,3)}",end="")
itm = None
open("OUT.XML", "w", encoding="utf-8").write(XML_Data_1st_Cache+XML_Data_2nd_Cache+XML_Data_3rd_Cache+f"</i>\x0a<!-- Create Time: {int(Start_Time)} -->")
End_Time = time.time()
print(f"\r{Danmaku_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")