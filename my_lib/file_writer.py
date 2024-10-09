#!/dev/null
import gzip


def write_file(filename: str, data: str | bytes | dict, _gzip: bool = False) -> None:
    """
    输出文件
    """
    if isinstance(data, str):
        _data = data.encode("utf-8")
    elif isinstance(data, dict):
        import json

        _data = _data = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    else:
        _data = data

    if _gzip:
        gzip.open(filename, "wb", compresslevel=9).write(data)
    else:
        open(filename, "wb", 1048576).write(_data)
