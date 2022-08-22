#!/dev/null
try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

def proto2xml(this: dm_pb2.DanmakuElem, exdata: bool, enable_weight: bool) -> str: ...
