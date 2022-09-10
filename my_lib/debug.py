a = [
"计时器          1",
"错误停机        2",
"直播回放xxx     4",
"日志            8",
"输出Ext XML    16",
"不输出Json     32",
"不输出XML      64",
"输出 Protobuf 128",
"模拟运行      256",
"BAS           512",
"gzip         1024",
"UP主自定义   2048",
"is_ERROR     4096",
"Flag13有弹幕 8192",
"exit pos 1  16384",
"exit pos 2  32768",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined",
"Undefined"
]
def flag_debug(pflag):
	for i in range(len(pflag)):
		print(f"[Debug_Flag] {a[i]}\t{pflag[i]}")
	return