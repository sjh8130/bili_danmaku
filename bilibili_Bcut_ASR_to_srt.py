#!/usr/bin/python3
import json
import sys
import time

def convert_srt_time(t):return f"{(t//3600000):02d}:{(t//60000%60):02d}:{(t//1000%60):02d},{(t%1000):03d}"
def convert_lrc_time(t):return f"[{(t//60000):02d}:{(t//1000%60):02d}.{(t%1000//10):02d}]"
def proc_ASS(item):
	fi___itm = ""
	fi_k_itm = ""
	start_time= item['start_time']
	end_time=   item['end_time']
	def ass_time(time):return f"{(time//3600000):01d}:{(time//60000%60):02d}:{(time//1000%60):02d}.{(time%1000):03d}"[0:-1]
	def proc_karaoke(karaoke_item):
		v = f"\x7b\\K{int((karaoke_item[0]['end_time']-karaoke_item[0]['start_time'])/10)}\x7d{karaoke_item[0]['label']}"
		for w in range(len(karaoke_item)):
			if w == 0:continue
			v+=f"\x7b\\K{int((karaoke_item[w]['end_time']-karaoke_item[w-1]['end_time'])/10)}\x7d{karaoke_item[w]['label']}"
		return v
	fi___itm = f"Dialogue: 0,{ass_time(start_time)},{ass_time(end_time)},A,,0,0,0,,{item['transcript']}\n"
	fi_k_itm = f"Dialogue: 1,{ass_time(start_time)},{ass_time(end_time)},B,,0,0,0,,{proc_karaoke(item['words'])}\n".replace("{\k0}","")
	return fi___itm+fi_k_itm

Start_Time = time.time()
input_File = sys.argv[1]

output_SRT = input_File.rsplit(".", 1)[-2]+"_P.srt"
output_ASS = input_File.rsplit(".", 1)[-2]+"_P.ass"
output_LRC = input_File.rsplit(".", 1)[-2]+"_P.lrc"
output_TXT = input_File.rsplit(".", 1)[-2]+"_P.txt"
input_File = open(input_File, "r", encoding="utf-8").read()

Loaded_JSON = json.loads(input_File)
del input_File
srt_index = 0

try: Subtitle_Count = len(Loaded_JSON["utterances"])
except KeyError: Subtitle_Count = 0

if Subtitle_Count == 0:
	print("No Data")
	sys.exit()

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

for line in Loaded_JSON["utterances"]:
	srt_index += 1
	Final_SRT_Content += f"{srt_index}\n{convert_srt_time(line['start_time'])} --> {convert_srt_time(line['end_time'])}\n{line['transcript']}\n\n"
	Final_LRC_Content += f"{convert_lrc_time(line['start_time'])}{line['transcript']}\n"
	Final_TXT_Content += f"{line['transcript']}\n"
	Final_ASS_Content += proc_ASS(line)
	print(f"\rProgress: {srt_index}/{Subtitle_Count}, Time: {round(time.time()-Start_Time,3)}",end="")
print()
# print(Final_SRT_Content)
# print(Final_ASS_Content)
# print(Final_LRC_Content)
# print(Final_TXT_Content)
open(output_SRT, "w", encoding="utf-8").write(Final_SRT_Content)
open(output_ASS, "w", encoding="utf-8").write(Final_ASS_Content)
# open(output_LRC, "w", encoding="utf-8").write(Final_LRC_Content)
# open(output_TXT, "w", encoding="utf-8").write(Final_TXT_Content)
End_Time = time.time()
print(f"\r{Subtitle_Count}, 总计用时：{round(End_Time-Start_Time, 4)}                     ")
