def group_similar_strings(file_path):
    # 从文件中读取字符串列表
    with open(file_path, "r", encoding="utf-8") as file:
        input_strings = [line.strip() for line in file.readlines()]
    # 使用字典来存储相同前缀的字符串
    grouped_strings = {}
    # 遍历输入字符串列表
    for string in input_strings:
        # 提取字符串的前缀（方括号内的部分）
        prefix = string.split("_")[0]
        # 如果前缀已经在字典中，将字符串添加到对应的列表中
        if prefix in grouped_strings:
            grouped_strings[prefix].append(string)
        # 否则，为前缀创建一个新列表并添加字符串
        else:
            grouped_strings[prefix] = [string]
    # 将每一组的字符串连接成一行，并用逗号分隔
    output_strings = []
    for group in grouped_strings.values():
        output_strings.append(",".join(group))
    # 返回字符串列表，以便进一步处理（例如写入文件）
    return output_strings


# 调用函数并获取输出
input_file_path = "Z:\\111.txt"  # 输入文件路径
output_strings = group_similar_strings(input_file_path)
# 打印输出到控制台
for line in output_strings:
    print(line)
# 如果需要，也可以将输出保存到文件中
output_file_path = "Z:\\output.txt"  # 输出文件路径
with open(output_file_path, "w", encoding="utf-8") as file:
    for line in output_strings:
        file.write(line + "\n")
print(f"输出已保存到文件：{output_file_path}")
# AI
