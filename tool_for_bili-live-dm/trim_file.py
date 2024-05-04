import sys

def trim_file(input_file_path: str):
    # 读取文件内容
    with open(input_file_path, 'r', encoding="utf-8") as input_file, \
    open(f"{input_file_path}1", 'a', encoding="utf-8") as output_file:
        for line in input_file.readlines():
            output_file.writelines(line[0:13]+line[16:])


# 调用函数，按日分割文件
trim_file(sys.argv[1])
# split_file_by_day("Z://11.jsonl")
