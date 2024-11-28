import json

try:
    import pyperclip
except:
    pass

# 读取json数据
f = input("input:")
data = json.loads(f)
# 初始化结果字符串
try:
    data["cmd"]
    data = data["data"]
except KeyError:
    ...
res = f"| key\t| type\t| value |\n|-|-|-|\n"
for key, value in data.items():
    res += f"| {key}\t| {type(value).__name__.replace('int','num').replace('dict','obj').replace('list','[]')}\t| |\n"
print(res)
pyperclip.copy(res)