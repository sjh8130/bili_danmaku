import json
import sys
import re
from tqdm import tqdm

a = {}
with open(sys.argv[1], "r", encoding="utf-8")as f:
    a = f.read()
a=a.replace("}]}{\"elems\": [{","}, {")
a=a.replace("}]}{\"elems\": [{","},\n{")
# json.decoder.JSONDecodeError: Extra data: line *** column *** (char ***)
try:
    jsonData = json.loads(a)
except json.decoder.JSONDecodeError:
    jsonData = json.loads(a)

cid = re.split("_", sys.argv[1])[3]
item = ""

XML_items = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>"+cid+"</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"

for i in range((len(jsonData["elems"]))):
    # KeyError: 'progress'
    try:
        progress = jsonData["elems"][i]["progress"]
    except KeyError:
        progress = 0.0

    content = jsonData["elems"][i]["content"]
    item = "\t<d p=\"" + str(format(progress/1000, ".5f")) + "," + str(jsonData["elems"][i]["mode"]) + "," + str(jsonData["elems"][i]["fontsize"]) + "," + str(jsonData["elems"][i]["color"]) + "," + str(jsonData["elems"][i]["ctime"]) + ","+"0"+"," + jsonData["elems"][i]["midHash"] + "," + jsonData["elems"][i]["id"] + "\">" + str(content).replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;") + "</d>\n"
    XML_items += item

XML_items += "</i>"

with open(sys.argv[1].replace(".json", ".xml"), "w", encoding="utf-8")as g:
    g.write(XML_items)
