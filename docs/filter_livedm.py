import io
import json
import time
import sys
from filters import FILTER_WORDS,FILTER_USER,FILTER_USER_CRC

line: str
start_time = time.time()
# in_path = ""
in_path = sys.argv[1]
out_path = "Z:\\test.json"
left_pos = 0
dm_text: str
danmaku: dict
extra: dict
try:
	with open(out_path, "r", encoding="utf-8") as file_out:
		final_write = json.load(file_out)
except FileNotFoundError:
	final_write = {}
with open(in_path, "r", encoding="utf-8") as file_in:
	for line in file_in.readlines():
		if "DANMU_MSG" not in line: continue
		if line.find("DANMU_MSG:3:7:1:1:1:1") == 1: continue
		left_pos = line.find('{')
		danmaku = json.loads(line[left_pos:-1])

		if danmaku['info'][0][9] != 0: continue		# 1:节奏风暴 2:天选时刻 9:弹幕互动游戏
		if danmaku['info'][0][12] != 0: continue	# 0:文本 1:表情包 2:语音

		if danmaku['info'][0][7] in FILTER_USER_CRC: continue
		if danmaku['info'][2][0] in FILTER_USER: continue

		dm_text = danmaku['info'][1]
		dm_text = dm_text.strip().strip("\u3000").strip("\u200e")
		if dm_text in FILTER_WORDS or dm_text.lower() in FILTER_WORDS:
			try:
				del final_write[dm_text]
			except:
				pass
			continue
		else:
			try:
				if json.loads(danmaku['info'][0][15]['extra'])['hit_combo'] == 1: continue
			except KeyError:
				pass
			try:
				final_write[dm_text] += 1
			except KeyError:
				final_write[dm_text] = 1
with open(out_path, "w", encoding="utf-8") as file_out:
	json.dump(final_write,file_out, ensure_ascii=False, indent="\t")
total_time = time.time() - start_time
print(f"处理完成，耗时：{total_time:.3f}秒")
