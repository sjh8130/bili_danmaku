#!/dev/null
import gzip


def FileWriter(filename: str, data: str | bytes | dict, _gzip: bool = False) -> None:
	"""
	输出文件
	"""
	_type = type(data)
	if _type == str:
		_data = bytes(data, encoding="utf-8")
	elif _type == dict:
		import json
		_data = bytes(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
	else:
		_data = data

	if _gzip:
		gzip.open(filename, 'wb', compresslevel=9).write(data)
	else:
		open(filename, "wb", 1048576).write(_data)
