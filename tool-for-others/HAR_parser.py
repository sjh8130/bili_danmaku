import json
import sys
jmp = 0

with open(sys.argv[1], "r", -1, "utf-8")as file:
	data = json.load(file)["log"]
print(data["pages"][0]["title"])
for item in data["entries"]:
	if item["request"]["url"].startswith("https://data.bilibili.com/v2/log/web"):jmp = 1
	if item["request"]["url"].startswith("https://s1.hdslb.com"):jmp = 1
	if item["request"]["url"].startswith("https://i0.hdslb.com"):jmp = 1
	if item["request"]["url"].startswith("https://i1.hdslb.com"):jmp = 1
	if item["request"]["url"].startswith("https://i2.hdslb.com"):jmp = 1
	if item["request"]["url"] == "https://api.live.bilibili.com/relation/v1/Feed/heartBeat":jmp = 1
	if item["request"]["url"] == "https://data.bilibili.com/v2/log/web?content_type=pbrequest&logid=021434&disable_compression=true":jmp = 1
	if item["request"]["url"].endswith(".css"):jmp = 1
	if item["request"]["url"].endswith(".js"):jmp = 1
	if item["request"]["url"].endswith(".svga"):jmp = 1
	if item["request"]["url"].endswith(".jpg"):jmp = 1
	if item["request"]["url"].endswith(".png"):jmp = 1
	if item["request"]["url"].endswith(".webp"):jmp = 1
	if item["request"]["url"].endswith(".avif"):jmp = 1
	try:
		if item["response"]["content"]["mimeType"].startswith("image"): jmp = 1
	except:
		...
	try:
		if item["response"]["_error"] != None: jmp = 1
	except:
		...
	if jmp == 0:
		for rsp in item["response"]["headers"]:
			if rsp["name"] == "mimeType" and rsp["value"].startswith("image/"):
				jmp = 1
	if jmp:
		jmp = 0
		continue
	print(item["request"]["method"], item["request"]["url"], )
	if item["response"]["status"] == 101:
		print(json.dumps(item, ensure_ascii=False))
	# print(bytes(item["response"],"utf-"))

raise
