import dataclasses
import json
import sys
from decimal import Decimal
from pathlib import Path

try:
    import simdjson
except ImportError:
    simdjson = json


@dataclasses.dataclass
class FFProbeFilePackets:
    codec_type: str
    data_hash: str
    dts_time: Decimal
    dts: int
    duration_time: Decimal
    duration: int
    flags: str
    pos: int
    pts_time: Decimal
    pts: int
    size: int
    stream_index: int

    def __init__(self, d: dict) -> None:
        self.codec_type = d.get("codec_type", "")
        self.data_hash = d.get("data_hash", "")
        self.dts = int(d.get("dts", -1))
        self.dts_time = Decimal(d.get("dts_time", "0"))
        self.duration = int(d.get("duration", -1))
        self.duration_time = Decimal(d.get("duration_time", "0"))
        self.pos = int(d.get("pos", -1))
        self.pts = int(d.get("pts", -1))
        self.pts_time = Decimal(d.get("pts_time", "0"))
        self.size = int(d.get("size", -1))
        self.stream_index = int(d.get("stream_index", -1))


@dataclasses.dataclass
class FFProbeFile:
    packets: list[FFProbeFilePackets]

    def __init__(self, packet_list: list[dict[str, int | str]]) -> None:
        if self.packets is None:
            self.packets = []
        self.packets = [FFProbeFilePackets(pl) for pl in packet_list]

    def __len__(self) -> int:
        return len(self.packets)

    def __getitem__(self, *k, **kw) -> FFProbeFilePackets:
        return self.packets.__getitem__(*k, **kw)


def _main() -> None:
    """FFprobe json[data-hash] to txt."""
    in_path = Path(sys.argv[1])
    with open(in_path, encoding="utf-8") as fp:
        d: FFProbeFile = FFProbeFile(simdjson.load(fp))
    if not d:
        sys.exit()
    switch = False
    if not d.packets:
        return
    for preload, i in enumerate(d.packets):
        if preload >= 150:
            break
        if i.stream_index > 0:
            switch = True
    if switch:
        with (
            open(in_path.with_suffix("V.txt"), "w", encoding="utf-8") as f1,
            open(in_path.with_suffix("A.txt"), "w", encoding="utf-8") as f2,
        ):
            for i in d.packets:
                if i.stream_index == 0:
                    f1.write(i.data_hash + "\n")
                elif i.stream_index == 1:
                    f2.write(i.data_hash + "\n")
    else:
        with open(in_path.with_suffix(".txt"), "w", encoding="utf-8") as f:
            for i in d.packets:
                f.write(i.data_hash + "\n")


if __name__ == "__main__":
    _main()
