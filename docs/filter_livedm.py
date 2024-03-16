import io
import json
import time
import sys
from filters import FILTER_WORDS

line = 0
start_time = time.time()
# in_path = ""
in_path = sys.argv[1]
out_path = "Z:\\test.json"
left_pos = 0
dm_text: str
danmaku: dict
extra: dict
with open(in_path, "r", encoding="utf-8") as file_in, io.open(out_path, "a", encoding="utf-8") as file_out:
	for line in file_in:
		if "DANMU_MSG" not in line: continue
		if line.find("DANMU_MSG:3:7:1:1:1:1") == 1: continue
		left_pos = line.find('{')
		danmaku = json.loads(line[left_pos:-1])

		if danmaku['info'][0][9] != 0: continue  # 1:节奏风暴 2:天选时刻 9:弹幕互动游戏
		if danmaku['info'][0][12] != 1: continue  # 0:文本 1:表情包 2:语音
		dm_text = danmaku['info'][1]
		dm_text = dm_text.strip().lstrip("　").rstrip("　")
		if dm_text in FILTER_WORDS or dm_text.lower() in FILTER_WORDS or "【" in dm_text or "】" in dm_text: continue
		try:
			if json.loads(danmaku['info'][0][15]['extra'])['hit_combo'] == 1: continue
		except KeyError:
			pass
		# F_out.write(json.dumps({"len":len(dm_text),'text':dm_text}, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
		# F_out.write(json.dumps({'text':dm_text}, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
		file_out.write(dm_text + "\n")
total_time = time.time() - start_time
print(f"处理完成，耗时：{total_time:.3f}秒")
#AI optimized