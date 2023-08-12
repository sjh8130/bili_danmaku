#!/dev/null
try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

def Proto2XML(this: dm_pb2.DanmakuElem, extra_data: bool, enable_weight: bool) -> str: ...
