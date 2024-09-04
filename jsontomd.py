import json

# 读取json数据
f = input("input:")
data = json.loads(f)
# 初始化结果字符串
try:
	data["cmd"]
	data = data["data"]
except KeyError:
	...
res = f"| key | type | value |\n| - | - | - |\n"
for key, value in data.items():
	res += f"| {key} | {type(value).__name__.replace('int','num').replace('dict','obj').replace('list','[]')} | |\n"
print(res)
