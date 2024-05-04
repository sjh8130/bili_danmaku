import io
import json
import time
import sys

"""
11th Intel Core : 60MB/s @4 GHz
"""
line = 0
st = time.time()
in_path = sys.argv[1]
outPath = "Z:\\test.json"
left_pos_cache = 0
right_pos_cache = -1

with open(in_path, "r", 1048576, encoding="utf-8") as F_in, io.open(outPath, "w", encoding="utf-8") as F_out:
	for this_line in F_in.readlines():
		for left_pos_cache in range(len(this_line)):
			try:
				load_line=json.loads(this_line[left_pos_cache:right_pos_cache])
			except json.decoder.JSONDecodeError as err:
				if err.msg == "Extra data": left_pos_cache = err.pos
				if err.msg == "Expecting value":
					if this_line[left_pos_cache] == ".":left_pos_cache += 1
					else:right_pos_cache -= 1
				continue
			else:
				break
		if load_line['cmd'] != 'DANMU_MSG':
			continue
	F_out.write(json.dumps({'text':dm_text}, ensure_ascii=False, indent=None, separators=(",", ":")) + "\n")
	F_in.close()
	F_out.close()
et = time.time()
print(f"\n{et-st}")
# time.sleep(5)
