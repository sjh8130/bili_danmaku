import io
import json
import time
import sys
from filters import FILTER_WORDS

"""
11th Intel Core : 11MB/s @4 GHz
"""
line = 0
st = time.time()
in_path = sys.argv[1]
outPath = "Z:\\test.json"
left_pos_cache = 0
right_pos_cache = -1
danmaku:str
with open(in_path, "r", 1048576, encoding="utf-8") as F_in, io.open(outPath, "w", encoding="utf-8") as F_out:
	for this_line in F_in.readlines():
		if this_line.find("DANMU_MSG") == -1: continue
		if this_line.find("DANMU_MSG:3:7:1:1:1:1") == 1: continue
		# line+=1;print(f"\r{line=}# ",end="") #-30%
		for left_pos_cache in range(len(this_line)):
			try:
				# print(this_line[left_pos_cache:right_pos_cache][0:20])
				danmaku=json.loads(this_line[left_pos_cache:right_pos_cache])
			except json.decoder.JSONDecodeError as err:
				# # print(err)
				if err.msg == "Extra data": left_pos_cache = err.pos
				if err.msg == "Expecting value":
					if this_line[left_pos_cache] == ".":left_pos_cache += 1
					else:right_pos_cache -= 1
				# time.sleep(0.1)
				continue
			else:
				break
		# if danmaku['cmd'] != 'DANMU_MSG': continue
		if danmaku['info'][0][9] != 0: continue#1:节奏风暴 2:天选时刻 9:弹幕互动游戏
		if danmaku['info'][0][12] != 0: continue#0:文本 1:表情包 2:语音
		dm_text = danmaku['info'][1]
		if dm_text in FILTER_WORDS or dm_text.lower() in FILTER_WORDS or dm_text.find("【")>0 or dm_text.find("】")>0: continue
		# dm_text = dm_text.lstrip(" ").rstrip(" ").lstrip("　").rstrip("　")
		# print(dm_text)
		# F_out.write(json.dumps({"len":len(dm_text),'text':dm_text}, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
		F_out.write(json.dumps({'text':dm_text}, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
	F_in.close()
	F_out.close()
et = time.time()
print(f"\n{et-st}")
time.sleep(5)
