#!/usr/bin/python3
from functools import lru_cache
import json
import sys


@lru_cache
def convert_srt_time(t: int):
	return f"{(t//3600000):02d}:{(t//60000%60):02d}:{(t//1000%60):02d},{(t%1000):03d}"


@lru_cache
def convert_lrc_time(t: int):
	return f"[{(t//60000):02d}:{(t//1000%60):02d}.{(t%1000//10):02d}]"


@lru_cache
def convert_ass_time(t: int):
	return f"{(t//3600000):01d}:{(t//60000%60):02d}:{(t//1000%60):02d}.{(t%1000):03d}"[0:-1]


def proc_karaoke(karaoke_item: dict):
	karaoke_word = f"\x7b\\K{int((karaoke_item[0]['end_time']-karaoke_item[0]['start_time'])/10)}\x7d{karaoke_item[0]['label']}"
	if karaoke_item[0]["label"].isascii():
		karaoke_word += " "
	for timed_chars in range(len(karaoke_item)):
		if timed_chars == 0:
			continue
		karaoke_word += f"""\x7b\\K{int((karaoke_item[timed_chars]["end_time"]-karaoke_item[timed_chars-1]["end_time"])/10)}\x7d{karaoke_item[timed_chars]["label"]}"""
		if karaoke_item[timed_chars]["label"].isascii() and timed_chars != len(karaoke_item):
			karaoke_word += " "
	return karaoke_word


def proc_ASS(item: dict):
	fi_k_itm = ""
	start_time = item["start_time"]
	end_time = item["end_time"]

	fi___itm = f"""Dialogue: 0,{convert_ass_time(start_time)},{convert_ass_time(end_time)},A,,0,0,0,,{item["transcript"]}\n"""
	try:
		pass
		# fi_k_itm = f"Dialogue: 1,{convert_ass_time(start_time)},{convert_ass_time(end_time)},B,,0,0,0,,{proc_karaoke(item["words"])}\n".replace("{\k0}","")
	except KeyError:
		pass
	return fi___itm + fi_k_itm.replace(" \n", "\n").replace("  ", " ").replace(",,0,0,0,, ", ",,0,0,0,,")


def write(path, data):
	open(path, "w", encoding="utf-8").write(data)


input_File = sys.argv[1]

output_SRT = input_File.rsplit(".", 1)[-2] + "_P.srt"
output_ASS = input_File.rsplit(".", 1)[-2] + "_P.ass"
output_LRC = input_File.rsplit(".", 1)[-2] + "_P.lrc"
output_TXT = input_File.rsplit(".", 1)[-2] + "_P.txt"
input_File = open(input_File, "r", encoding="utf-8").read()

Loaded_JSON = json.loads(input_File)
del input_File
srt_index = 0

Final_SRT_Content = ""
Final_LRC_Content = ""
Final_TXT_Content = ""
Final_ASS_Content = """[Script Info]
Title: ASR subtitles
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: A,Arial,60,&H00FFFFFF,&H0000FFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,0,0,10,1
Style: B,Arial,60,&H00FFFFFF,&H0000FFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,2,0,0,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
aegisub_time_overflow = False
lrc_time_overflow = False
for line in Loaded_JSON["utterances"]:
	srt_index += 1
	Final_SRT_Content += f"""{srt_index}\n{convert_srt_time(line["start_time"])} --> {convert_srt_time(line["end_time"])}\n{line["transcript"]}\n\n"""
	Final_LRC_Content += f"""{convert_lrc_time(line["start_time"])}{line["transcript"]}\n"""
	Final_TXT_Content += f"""{line["transcript"]}\n"""
	Final_ASS_Content += proc_ASS(line)
	if line["start_time"] > 36000000 or line["end_time"] > 36000000:
		aegisub_time_overflow = True
	if line["start_time"] > 3600000:
		lrc_time_overflow = True
if lrc_time_overflow:
	Final_LRC_Content += "[59:59.99]LRC时间溢出\n"
if aegisub_time_overflow:
	Final_ASS_Content += "Dialogue: 0,0:00:00.00,9:59:59.99,A,,0,0,0,,\{\\an2\}ASS时间溢出\n"
# print(Final_SRT_Content)
# print(Final_ASS_Content)
# print(Final_LRC_Content)
# print(Final_TXT_Content)
write(output_SRT, Final_SRT_Content)
# write(output_ASS, Final_ASS_Content)
# write(output_LRC, Final_LRC_Content)
# write(output_TXT, Final_TXT_Content)
