import json
import sys
import re
from tqdm import tqdm
import time

start_time = time.time()
jsonData = ""
HDD_Write_Count = 0
input_file = sys.argv[1]
outputFile = input_file.replace(".json", ".xml")
write_split = 20000     # 磁盘IO <<----小----  分块大小 ----大---->> 处理时间

with open(input_file, "r", encoding="utf-8")as f:
    jsonData = f.read()

try:
    jsonData = json.loads(jsonData)
except json.decoder.JSONDecodeError:
    print(
        "\033[41m==============================ERROR=============================\033[0m")
    if len(jsonData) == 1 or len(jsonData) == 0:
        print("\033[41m Empty File\033[0m")
    else:
        pass
    sys.exit(1)

cid = re.split("_", sys.argv[1])[3]
item = ""

with open(outputFile, "w", encoding="utf-8")as first_clear:
    first_clear.write("")
    HDD_Write_Count += 1
    first_clear.close()


XML_items = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"

progress_bar = tqdm(total=(len(jsonData["elems"])), leave=False)
for i in range((len(jsonData["elems"]))):
    # ================================ content ================================
    try:
        content = jsonData["elems"][i]["content"]
    except KeyError:
        # print("\n\033[43m content   ERROR", jsonData["elems"][i]["id"], "\033[0m")
        continue
        # content = "_CONTENT_ERROR_"

    content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # ================================ progress ================================
    try:
        progress = jsonData["elems"][i]["progress"]
    except KeyError:
        # print("\n progress ERROR", i)
        progress = 0.0

    progress = format(progress/1000, ".5f")
    # ================================ mode ================================
    mode = jsonData["elems"][i]["mode"]
    # ================================ fontsize ================================
    fontsize = jsonData["elems"][i]["fontsize"]
    # ================================ color ================================
    try:
        color = jsonData["elems"][i]["color"]
    except KeyError:
        # print("\n color    ERROR", i)
        color = 0
    # ================================ midHash ================================
    midHash = jsonData["elems"][i]["midHash"]
    # ================================ ctime ================================
    ctime = jsonData["elems"][i]["ctime"]
    # ================================ weight ================================
    weight = jsonData["elems"][i]["weight"]

    # ================================ idStr ================================
    # try:
    #     idstr = jsonData["elems"][i]["idstr"]
    # except KeyError:
    #     # print("\n idstr    ERROR", 1)
    #     idstr = "0"

    # ================================ id ================================
    id = jsonData["elems"][i]["id"]

    # ================================ id|idStr ================================
    # if id != idstr:
    #     print("\n id idstr mismatch:", id, idstr)

    # ================================ pool ================================
    try:
        pool = jsonData["elems"][i]["pool"]
    except KeyError:
        pool = 0

    item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>\n".format(progress, mode, fontsize, color, ctime, pool, midHash, id, weight - 1, content)
    XML_items += item
    if i % write_split == 0:
        with open(outputFile, "a", encoding="utf-8")as h:
            h.write(XML_items)
            HDD_Write_Count += 1
            XML_items = ""

    progress_bar.update(1)
progress_bar.close()

XML_items += "</i>"

with open(outputFile, "a", encoding="utf-8")as g:
    g.write(XML_items)
    HDD_Write_Count += 1
    g.close()
end_time = time.time()
print(f"Write Split: {write_split}\tDisk Writes Count: {HDD_Write_Count-1}\tTime Used: {end_time-start_time}")
