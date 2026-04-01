# cython:language_level=3
import re
from datetime import datetime, timedelta, timezone
from enum import IntEnum
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from io import TextIOWrapper

_TZ = timezone(timedelta(hours=8))
LRU_SIZE: int = 100000


class SplitMode(IntEnum):
    YEAR = 0
    Y = 0
    MONTH = 1
    M = 1
    DAY = 2
    D = 2
    HOUR = 3
    H = 3
    MINUTE = 4
    SECOND = 5
    S = 5
    MILLISECOND = 5
    MS = 5


@lru_cache(LRU_SIZE)
def _s0(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(LRU_SIZE)
def _s1(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(LRU_SIZE)
def _s2(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=0, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(LRU_SIZE)
def _s3(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=a.hour, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(LRU_SIZE)
def _s4(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=a.hour, minute=a.minute, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(LRU_SIZE)
def _s5(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=a.hour, minute=a.minute, second=a.second, microsecond=0, tzinfo=_TZ)


@lru_cache(LRU_SIZE)
def _s6(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=_TZ)


def split_file_by_time(in_path: Path, b_name: Path, sp_type: SplitMode) -> None:
    if sp_type == SplitMode.YEAR:
        gd = _s0
        fmt = "%Y"
    elif sp_type == SplitMode.MONTH:
        gd = _s1
        fmt = "%Y-%m"
    elif sp_type == SplitMode.DAY:
        gd = _s2
        fmt = "%Y-%m-%d"
    elif sp_type == SplitMode.HOUR:
        gd = _s3
        fmt = "%Y-%m-%d_%H"
    elif sp_type == SplitMode.MINUTE:
        gd = _s4
        fmt = "%Y-%m-%d_%H%M"
    elif sp_type == SplitMode.SECOND:
        gd = _s5
        fmt = "%Y-%m-%d_%H%M%S"
    elif sp_type == SplitMode.SECOND:
        gd = _s6
        fmt = "%Y-%m-%d_%H%M%S_%f"
    else:
        gd = _s2
        fmt = "%Y-%m-%d"
    in_path = in_path.resolve()
    fps: dict[datetime, TextIOWrapper] = {}
    with open(str(in_path), encoding="utf-8") as input_file:  # noqa: PTH123
        for line in input_file:
            timestamp_match: re.Match[str] | None = re.search(r"^(\d+)", line)
            if timestamp_match:
                timestamp: str = timestamp_match.group(1)[0:13]
                date: datetime = gd(int(timestamp) // 1_000)
                fp: TextIOWrapper | None = fps.get(date)
                if fp is None:
                    fs = str(in_path.parent / f"{b_name.stem}-{date.strftime(fmt)}{in_path.suffix}")
                    fp = open(fs, "a", 10485760, "utf-8")  # noqa: PTH123, SIM115
                    fps[date] = fp
                fp.write(line)

    # for fp in fps.values():
    #     fp.close()
