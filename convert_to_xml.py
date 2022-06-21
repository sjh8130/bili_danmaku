import json
import sys
import re
import time
from tqdm import tqdm

a = {}
with open(sys.argv[1], "r", encoding="utf-8")as f:
    a = f.read()

# print(a)
# print("================================================================")

a = "{" + a.lstrip("{}")
a = a.rstrip("{}") + "}"

# for h in range(1209):   # max single video duration 10h. current max:120h46m0s  BV1j x411 P7AP
#     # print(h)
#     a = a.replace("{}{}{\"elems\": [", "{}{\"elems\": [")

progress_bar = tqdm(total=600, leave=False)
for h in range(600):
    a = a.replace("{}{}{\"elems\": [", "{}{\"elems\": [")
    progress_bar.update(1)
progress_bar.close()

a = a.replace("}]}{}{\"elems\": [{", "}, {")
a = a.replace("}]}{\"elems\": [{", "}, {")
a = a.replace("}]}\n{\"elems\": [{", "}, {")
a = a.replace("}]}\n\t{\"elems\": [{", "}, {")
a = a.replace("}]}\n  {\"elems\": [{", "}, {")
a = a.replace("}]}\n    {\"elems\": [{", "}, {")

# print(a)
# json.decoder.JSONDecodeError: Extra data: line *** column *** (char ***)
# During handling of the above exception, another exception occurred:
try:
    jsonData = json.loads(a)
except json.decoder.JSONDecodeError:
    print("\033[41m==============================ERROR=============================\033[0m")
    if len(a) == 1:
        print("\033[41m Empty File\033[0m")
    else:
        time.sleep(0)
    sys.exit(1)

cid = re.split("_", sys.argv[1])[3]
item = ""

XML_items = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{0}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n".format(cid)

progress_bar = tqdm(total=(len(jsonData["elems"])), leave=False)
for i in range((len(jsonData["elems"]))):
    try:
        content = jsonData["elems"][i]["content"]
    except KeyError:
        print("\n\033[43m content   ERROR", jsonData["elems"][i]["id"], "\033[0m")
        continue
        # content = "_CONTENT_ERROR_"

    try:
        progress = jsonData["elems"][i]["progress"]
    except KeyError:
        # print("\n progress ERROR", i)
        progress = 0.0

    try:
        weight = str(jsonData["elems"][i]["weight"])
    except KeyError:
        # print("\n weight   ERROR", i)
        weight = str(10)

    try:
        idstr = jsonData["elems"][i]["idstr"]
    except KeyError:
        # print("\n idstr    ERROR", 1)
        idstr = str(0)

    id = jsonData["elems"][i]["id"]

    # if id != idstr:
    #     print("\n id idstr mismatch:", id, idstr)

    progress = str(format(progress/1000, ".5f"))
    mode = str(jsonData["elems"][i]["mode"])
    fontsize = str(jsonData["elems"][i]["fontsize"])

    try:
        color = str(jsonData["elems"][i]["color"])
    except KeyError:
        # print("\n color    ERROR", i)
        color = str(0)

    ctime = str(jsonData["elems"][i]["ctime"])
    danmakuType = str(0)
    midHash = jsonData["elems"][i]["midHash"]


    content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>\n".format(progress, mode, fontsize, color, ctime, danmakuType, midHash, id, weight, content)
    XML_items += item
    progress_bar.update(1)
progress_bar.close()

XML_items += "</i>"

with open(sys.argv[1].replace(".json", ".xml"), "w", encoding="utf-8")as g:
    g.write(XML_items)
# print(XML_items)
