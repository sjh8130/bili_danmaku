# cython:language_level=3
import os
import re
from datetime import datetime, timedelta, timezone
from enum import IntEnum
from functools import lru_cache

_TZ = timezone(timedelta(hours=8))


class SPLIT_SEL(IntEnum):
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
    _a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(
        year=_a.year,
        month=1,
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=_TZ,
    )


@lru_cache(10000)
def _s1(timestamp: int) -> datetime:
    _a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(
        year=_a.year,
        month=_a.month,
        day=1,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=_TZ,
    )


@lru_cache(10000)
def _s2(timestamp: int) -> datetime:
    _a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(
        year=_a.year,
        month=_a.month,
        day=_a.day,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=_TZ,
    )


@lru_cache(10000)
def _s3(timestamp: int) -> datetime:
    _a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(
        year=_a.year,
        month=_a.month,
        day=_a.day,
        hour=_a.hour,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=_TZ,
    )


@lru_cache(10000)
def _s4(timestamp: int) -> datetime:
    _a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(
        year=_a.year,
        month=_a.month,
        day=_a.day,
        hour=_a.hour,
        minute=_a.minute,
        second=0,
        microsecond=0,
        tzinfo=_TZ,
    )


@lru_cache(10000)
def _s5(timestamp: int) -> datetime:
    _a = datetime.fromtimestamp(timestamp, tz=_TZ)
    return datetime(
        year=_a.year,
        month=_a.month,
        day=_a.day,
        hour=_a.hour,
        minute=_a.minute,
        second=_a.second,
        microsecond=0,
        tzinfo=_TZ,
    )


@lru_cache(10000)
def _s6(timestamp: int) -> datetime:
    return datetime.fromtimestamp(timestamp, tz=_TZ)


def split_file_by_time(in_path: str, b_name: str, sp_type: SPLIT_SEL) -> None:
    if sp_type == SPLIT_SEL.YEAR:
        gd = _s0
        _fmt = "%Y"
    elif sp_type == SPLIT_SEL.MONTH:
        gd = _s1
        _fmt = "%Y-%m"
    elif sp_type == SPLIT_SEL.DAY:
        gd = _s2
        _fmt = "%Y-%m-%d"
    elif sp_type == SPLIT_SEL.HOUR:
        gd = _s3
        _fmt = "%Y-%m-%d_%H"
    elif sp_type == SPLIT_SEL.MINUTE:
        gd = _s4
        _fmt = "%Y-%m-%d_%H%M"
    elif sp_type == SPLIT_SEL.SECOND:
        gd = _s5
        _fmt = "%Y-%m-%d_%H%M%S"
    elif sp_type == SPLIT_SEL.SECOND:
        gd = _s6
        _fmt = "%Y-%m-%d_%H%M%S_%f"
    else:
        gd = _s2
        _fmt = "%Y-%m-%d"
    lines_by_day: dict[datetime, list[str]] = {}
    base_name, ext = os.path.splitext(os.path.basename(b_name))
    directory = os.path.dirname(in_path)
    with open(in_path, encoding="utf-8") as input_file:
        for line in input_file:
            timestamp_match = re.search(r"^(\d+)", line)
            if timestamp_match:
                timestamp = timestamp_match.group(1)[0:13]
                date: datetime = gd((int(timestamp) // 1_000).__trunc__())
                if date not in lines_by_day:
                    lines_by_day[date] = []
                lines_by_day[date].append(line)
    for date, lines_1 in lines_by_day.items():
        output_file_name = f"{base_name}-{date.strftime(_fmt)}{ext}"
        out_path = os.path.join(directory, output_file_name)
        with open(out_path, "a", 1048576, "utf-8") as output_file:
            output_file.writelines(lines_1)
