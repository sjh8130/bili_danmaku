import contextlib
import json

with contextlib.suppress(ImportError):
    import pyperclip
f = input("input:")
data: dict = json.loads(f)
try:
    data["cmd"]
    data = data["data"]
except KeyError:
    ...
res = "| key\t| type\t| value |\n|-|-|-|\n"
for key, value in data.items():
    res += f"| {key}\t| {type(value).__name__.replace('int', 'num').replace('dict', 'obj').replace('list', '[]')}\t| |\n"
print(res)
pyperclip.copy(res)
