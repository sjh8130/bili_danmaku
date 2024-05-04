import json
from collections import Counter


def count_lines_in_file(file_path):
	with open(file_path, 'r', encoding="utf-8") as file:
		lines = file.readlines()

	# 使用Counter来统计每一行出现的次数
	line_counts = Counter(lines)

	# 转换为字典
	line_counts_dict = {line.strip(): count for line, count in line_counts.items()}

	return line_counts_dict


def save_to_json(data, output_path):
	with open(output_path, 'w', encoding="utf-8") as file:
		json.dump(data, file, ensure_ascii=False, separators=(",", ":"), indent="\t")


if __name__ == "__main__":
	input_file_path = "Z:\\test.json"	# 输入文件路径
	output_file_path = "Z:\\output.json"	# 输出文件路径

	line_counts = count_lines_in_file(input_file_path)
	save_to_json(line_counts, output_file_path)
#AI