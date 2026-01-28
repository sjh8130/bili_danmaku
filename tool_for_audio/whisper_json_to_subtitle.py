import contextlib
import json
import sys
from pathlib import Path


def _convert_srt_time(t: int) -> str:
    return f"{(t // 3600000):02d}:{(t // 60000 % 60):02d}:{(t // 1000 % 60):02d},{(t % 1000):03d}"


def _convert_lrc_time(t: int) -> str:
    return f"[{(t // 60000):02d}:{(t // 1000 % 60):02d}.{(t % 1000 // 10):02d}]"


def _convert_ass_time(_time: int) -> str:
    return f"{(_time // 3600000):01d}:{(_time // 60000 % 60):02d}:{(_time // 1000 % 60):02d}.{(_time % 1000):03d}"[0:-1]


def _proc_ass_karaoke(word: list) -> str:
    karaoke_word = f"\x7b\\K{int((word[0]['end'] - word[0]['start']) / 10)}\x7d{word[0]['word']}"
    if word[0]["word"].isascii():
        karaoke_word += " "
    for timed_chars in range(len(word)):
        if timed_chars == 0:
            continue
        karaoke_word += f"\x7b\\K{int((word[timed_chars]['end'] - word[timed_chars - 1]['end']) / 10)}\x7d{word[timed_chars]['word']}"
        if word[timed_chars]["word"].isascii() and timed_chars != len(word):
            karaoke_word += " "
    return karaoke_word


def _proc_ass(item: dict) -> str:
    normal_line = ""
    karaoke_line = ""
    normal_line = f"Dialogue: 0,{_convert_ass_time(line_start)},{_convert_ass_time(line_end)},{language},,0,0,0,,{item['text']}\n"
    with contextlib.suppress(KeyError):
        karaoke_line = f"Dialogue: 1,{_convert_ass_time(line_start)},{_convert_ass_time(line_end)},B,,0,0,0,,{_proc_ass_karaoke(item['words'])}\n".replace("{\\k0}", "") if False else ""
    return normal_line + karaoke_line.replace(" \n", "\n").replace("  ", " ").replace(",,0,0,0,, ", ",,0,0,0,,")


input_path = Path(sys.argv[1]).resolve()
output_srt = input_path.parent / (input_path.stem + "_P.srt")
output_ass = input_path.parent / (input_path.stem + "_P.ass")
output_lrc = input_path.parent / (input_path.stem + "_P.lrc")
output_txt = input_path.parent / (input_path.stem + "_P.txt")
with input_path.open(encoding="utf-8") as fp:
    loaded_dict = json.load(fp)
srt_index = 0
try:
    language = loaded_dict["language"]
except KeyError:
    language = "A"
srt_file = ""
lrc_file = ""
txt_file = ""
ass_file = ""
ass_head = f"""[Script Info]
Title: ASR subtitles
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: {language},Arial,60,&H00FFFFFF,&H0000FFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,0,0,10,1
Style: B,Arial,60,&H00FFFFFF,&H0000FFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,0,0,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
for srt_index, line in enumerate(loaded_dict["segments"], 1):
    line_start = int(line["start"] * 1000)
    line_end = int(line["end"] * 1000)
    segment_text = line["text"].strip().replace("-->", "->")
    srt_file += f"{srt_index}\n{_convert_srt_time(line_start)} --> {_convert_srt_time(line_end)}\n{segment_text}\n\n"
    lrc_file += f"{_convert_lrc_time(line_start)}{segment_text}\n"
    txt_file += f"{segment_text}\n"
    ass_file += _proc_ass(line)
output_srt.open("w", encoding="utf-8").write(srt_file)
output_ass.open("w", encoding="utf-8").write(ass_head + ass_file)
# output_lrc.open("w", encoding="utf-8").write(lrc_file)
# output_txt.open("w", encoding="utf-8").write(txt_file)
