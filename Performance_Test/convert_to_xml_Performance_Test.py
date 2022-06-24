import json
import sys
import re
# from tqdm import tqdm
import time

file_name = "BV1xxxxxxxx_av1_P1_1_PerformanceTest_pTitle_PerformanceTest.json"
time_1 = time.time()
a = {}
with open(file_name, "r", encoding="utf-8")as f:
    a = f.read()
time_2 = time.time()
try:
    jsonData = json.loads(a)
except json.decoder.JSONDecodeError:
    print("\033[41m==============================ERROR=============================\033[0m")
    if len(a) == 1:
        print("\033[41m Empty File\033[0m")
    else:
        pass
    sys.exit(1)

time_3 = time.time()

cid = re.split("_", file_name)[3]
item = ""

time_4 = time.time()

XML_items = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"

# progress_bar = tqdm(total=(len(jsonData["elems"])), leave=False)
for i in range((len(jsonData["elems"]))):
    # ================================ content ================================
    try:
        content = jsonData["elems"][i]["content"]
    except KeyError:
        print("\n\033[43m content   ERROR", jsonData["elems"][i]["id"], "\033[0m")
        continue
        # content = "_CONTENT_ERROR_"

    content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # ================================ progress ================================
    try:
        progress = jsonData["elems"][i]["progress"]
    except KeyError:
        # print("\n progress ERROR", i)
        progress = 0.0

    progress = str(format(progress/1000, ".5f"))
    # ================================ mode ================================
    mode = str(jsonData["elems"][i]["mode"])
    # ================================ fontsize ================================
    fontsize = str(jsonData["elems"][i]["fontsize"])
    # ================================ color ================================
    try:
        color = jsonData["elems"][i]["color"]
    except KeyError:
        # print("\n color    ERROR", i)
        color = 0
    # ================================ midHash ================================
    midHash = jsonData["elems"][i]["midHash"]
    # ================================ ctime ================================
    # ctime = str(jsonData["elems"][i]["ctime"])
    ctime = jsonData["elems"][i]["ctime"]
    # ================================ weight ================================
    try:
        weight = jsonData["elems"][i]["weight"]
    except KeyError:
        # print("\n weight   ERROR", i)
        weight = 10

    # ================================ idStr ================================
    try:
        idstr = jsonData["elems"][i]["idstr"]
    except KeyError:
        # print("\n idstr    ERROR", 1)
        idstr = "0"

    # ================================ id ================================
    id = jsonData["elems"][i]["id"]

    # ================================ id|idStr ================================
    # if id != idstr:
    #     print("\n id idstr mismatch:", id, idstr)

    # ================================ pool ================================
    danmakuType = "0"

    item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>\n".format(progress, mode, fontsize, str(color), ctime, danmakuType, midHash, id, str(weight), content)
    XML_items += item
    # progress_bar.update(1)
XML_items += "</i>"
# progress_bar.close()


time_5 = time.time()

with open("NUL".replace(".json", ".xml"), "w", encoding="utf-8")as g:
    g.write(XML_items)
    g.close()

time_6 = time.time()

print(f"{time_1},{time_2},{time_3},{time_4},{time_5},{time_6}")
