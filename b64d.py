import base64
import brotli
import json
while True:
	a = bytes(input(),"utf-8")
	b=base64.decodebytes(a)
	c=brotli.decompress(b[16:])
	d=json.loads(c[16:])
	e=json.dumps(d,ensure_ascii=False,separators=(",",":"))
	print(e)