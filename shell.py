a = input()
END="\033[0m"
cc_arr = [0, 1, 2, 4, 7, 8]
color_arr = range(0,8)
for cc in cc_arr:
	for bgcolor in color_arr:
		for text in color_arr:
			print(f"\033[{cc};3{text};4{bgcolor}m{a}{END} 4{bgcolor} 3{text}\t", end="")
		print()
	print(cc)
