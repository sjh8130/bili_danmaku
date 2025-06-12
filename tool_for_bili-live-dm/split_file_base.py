# cython:language_level=3
import re
from datetime import datetime, timedelta, timezone
from enum import IntEnum
from functools import lru_cache
from pathlib import Path

_TZ = timezone(timedelta(hours=8))


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


@lru_cache(10000)
def _s0(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(10000)
def _s1(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(10000)
def _s2(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=0, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(10000)
def _s3(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=a.hour, minute=0, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(10000)
def _s4(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=a.hour, minute=a.minute, second=0, microsecond=0, tzinfo=_TZ)


@lru_cache(10000)
def _s5(timestamp: int) -> datetime:
    a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(year=a.year, month=a.month, day=a.day, hour=a.hour, minute=a.minute, second=a.second, microsecond=0, tzinfo=_TZ)


@lru_cache(10000)
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
    lines_by_day: dict[datetime, list[str]] = {}
    base_name, ext = b_name.stem, in_path.suffix
    in_path = in_path.resolve()
    directory = in_path.parent
    with in_path.open(encoding="utf-8") as input_file:
        for line in input_file:
            timestamp_match = re.search(r"^(\d+)", line)
            if timestamp_match:
                timestamp = timestamp_match.group(1)[0:13]
                date: datetime = gd(int(timestamp) // 1_000)
                if date not in lines_by_day:
                    lines_by_day[date] = []
                lines_by_day[date].append(line)
    for date, lines_1 in lines_by_day.items():
        output_file_name = f"{base_name}-{date.strftime(fmt)}{ext}"
        out_path = directory / output_file_name
        with out_path.open("a", 1048576, "utf-8") as output_file:
            output_file.writelines(lines_1)
