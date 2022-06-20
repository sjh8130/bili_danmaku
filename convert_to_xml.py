import json
import sys
import re
from tqdm import tqdm

a = {}
with open(sys.argv[1], "r", encoding="utf-8")as f:
    a = f.read()
print(a)
print("================================================================")
a=a.replace("}]}{\"elems\": [{","}, {")
a=a.replace("}]}\n{\"elems\": [{","}, {")
print(a)
# json.decoder.JSONDecodeError: Extra data: line *** column *** (char ***)
# During handling of the above exception, another exception occurred:
try:
    jsonData = json.loads(a)
except json.decoder.JSONDecodeError:
    print("========================ERROR===================================")
    a = a.rstrip("{}")+"}"
    if len(a) == 1:
        print("LEN=0")
        sys.exit(1)
    print(a)
    jsonData = json.loads(a)

cid = re.split("_", sys.argv[1])[3]
item = ""

XML_items = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>"+cid+"</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"

progress_bar = tqdm(total=(len(jsonData["elems"])), ncols=100)
for i in range((len(jsonData["elems"]))):
    # KeyError: 'progress'
    try:
        progress = jsonData["elems"][i]["progress"]
    except KeyError:
        progress = 0.0

    try:
        weight = jsonData["elems"][i]["weight"]
    except KeyError:
        weight = 10

    if jsonData["elems"][i]["id"] != jsonData["elems"][i]["idstr"]:
        print("id idstr mismatch")

    content = jsonData["elems"][i]["content"]
    item = "\t<d p=\"" + str(format(progress/1000, ".5f")) + "," + str(jsonData["elems"][i]["mode"]) + "," + str(jsonData["elems"][i]["fontsize"]) + "," + str(jsonData["elems"][i]["color"]) + "," + str(jsonData["elems"][i]["ctime"]) + ","+"0"+"," + jsonData["elems"][i]["midHash"] + "," + jsonData["elems"][i]["id"] + "," + str(weight) + "\">" + str(content).replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;") + "</d>\n"
    XML_items += item
    progress_bar.update(1)
progress_bar.close()

XML_items += "</i>"

with open(sys.argv[1].replace(".json", ".xml"), "w", encoding="utf-8")as g:
    g.write(XML_items)
print(XML_items)
