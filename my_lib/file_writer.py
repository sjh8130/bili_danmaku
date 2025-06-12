import gzip
import json


def write_file(filename: str, data: str | bytes | dict, *, _gzip: bool = False) -> None:
    """输出文件."""
    if isinstance(data, str):
        data_ = data.encode("utf-8")
    elif isinstance(data, dict):
        data_ = json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    else:
        data_ = data
    if _gzip:
        gzip.open(filename, "wb", compresslevel=9).write(data_)
    else:
        open(filename, "wb", 1048576).write(data_)
