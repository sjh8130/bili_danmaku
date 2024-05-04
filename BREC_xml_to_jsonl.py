import json
import sys

from lxml import etree

file_path = sys.argv[1]
# file_path = "Z:\\1.xml"

preload = open(file_path, "rb").read(512)
if preload.find(b"encoding="):
	file = open(file_path, "rb").read()
elif preload[0:2] == b"\xef\xbb\xbf":
	file = open(file_path, "r", encoding="utf-8").read()[2:]
else:
	file = open(file_path, "r", encoding="utf-8").read()


tree = etree.XML(file)
a = tree.findall(".//d")
# print(a)
with open("Z:\\test.json", "a", encoding="utf-8") as w:
	for i in a:
		w.writelines(json.dumps({"cmd": "DANMU_MSG", "info": json.loads(i.attrib["raw"])}, ensure_ascii=False, separators=(",", ":"))+"\n")
		# print(i.attrib["raw"])
		# b = 1
