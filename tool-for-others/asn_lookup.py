import os
import sys
import ipaddress


def init():
	PATH_BASE = "Z:\\"
	FILEPATH = (
		f"{PATH_BASE}delegated-iana-latest",#互联网号码分配局#~1500
		f"{PATH_BASE}delegated-apnic-latest",#亚太互联网络信息中心#~160,000
		f"{PATH_BASE}delegated-arin-latest",#美洲互联网号码注册管理机构#~70000
		f"{PATH_BASE}delegated-ripencc-latest",#欧洲IP网络资源协调中心#~120,000
		f"{PATH_BASE}delegated-lacnic-latest",#拉丁美洲及加勒比地区互联网地址注册管理机构#~20000
		f"{PATH_BASE}delegated-afrinic-latest",#非洲网络信息中心#~9000
	)
	URL_BASE = "https://ftp.apnic.net/stats"
	URL = (
		f"{URL_BASE}/iana/delegated-iana-latest",
		f"{URL_BASE}/apnic/delegated-apnic-latest",
		f"{URL_BASE}/arin/delegated-arin-extended-latest",
		f"{URL_BASE}/ripe-ncc/delegated-ripencc-latest",
		f"{URL_BASE}/lacnic/delegated-lacnic-latest",
		f"{URL_BASE}/afrinic/delegated-afrinic-latest",
	)
	for url, filepath in zip(URL, FILEPATH):
		download_file(url, filepath)
		process_cidr(filepath)


ISO3166_1 = ["AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ",
			 "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ",
			 "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ",
			 "DE", "DJ", "DK", "DM", "DO", "DZ",
			 "EC", "EE", "EG", "EH", "ER", "ES", "ET",
			 "FI", "FJ", "FK", "FM", "FO", "FR",
			 "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY",
			 "HK", "HM", "HN", "HR", "HT", "HU",
			 "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT",
			 "JE", "JM", "JO", "JP",
			 "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ",
			 "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY",
			 "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ",
			 "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ",
			 "OM",
			 "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY",
			 "QA",
			 "RE", "RO", "RS", "RU", "RW",
			 "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ",
			 "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ",
			 "UA", "UG", "UM", "US", "UY", "UZ",
			 "VA", "VC", "VE", "VG", "VI", "VN", "VU",
			 "WF", "WS",
			 "YE", "YT",
			 "ZA", "ZM", "ZW",
			 ]

ips = [
	["0.0.0.0/8",			"XX", "listening", "reserved"],
	["10.0.0.0/8",			"XX", "PRIVATE-A", "reserved"],
	["127.0.0.0/8",			"XX", "Loopback", "reserved"],
	["169.254.0.0/16",		"XX", "LinkLocal", "reserved"],
	["172.16.0.0/12",		"XX", "PRIVATE-B", "reserved"],
	["192.168.0.0/16",		"XX", "PRIVATE-C", "reserved"],
	["224.0.0.0/28",		"XX", "Multicast", "reserved"],
	["240.0.0.0/28",		"XX", "Reserved-E", "reserved"],
	["255.255.255.255/32",	"XX", "Broadcast", "reserved"],
	["2000::/3",			"XX", "Global", "reserved"],
	["fe80::/10",			"XX", "local", "reserved"],
	["fc00::/7",			"XX", "local", "reserved"],
	["::1/128",				"XX", "Loopback", "reserved"],
	["::/128",				"XX", "listening", "reserved"],
	["::/80",				"XX", "ipv4-in-ipv6", "reserved"],
	["2400:cb00::/32",		"US", "Cloudflare", "allocated"],
	["2606:4700::/32",		"US", "Cloudflare", "allocated"],
	["2803:f800::/32",		"US", "Cloudflare", "allocated"],
	["2405:b500::/32",		"US", "Cloudflare", "allocated"],
	["2405:8100::/32",		"US", "Cloudflare", "allocated"],
	["2a06:98c0::/29",		"US", "Cloudflare", "allocated"],
	["2c0f:f248::/32",		"US", "Cloudflare", "allocated"],
	["173.245.48.0/20",		"US", "Cloudflare", "allocated"],
	["103.21.244.0/22",		"US", "Cloudflare", "allocated"],
	["103.22.200.0/22",		"US", "Cloudflare", "allocated"],
	["103.31.4.0/22",		"US", "Cloudflare", "allocated"],
	["141.101.64.0/18",		"US", "Cloudflare", "allocated"],
	["108.162.192.0/18",	"US", "Cloudflare", "allocated"],
	["190.93.240.0/20",		"US", "Cloudflare", "allocated"],
	["188.114.96.0/20",		"US", "Cloudflare", "allocated"],
	["197.234.240.0/22",	"US", "Cloudflare", "allocated"],
	["198.41.128.0/17",		"US", "Cloudflare", "allocated"],
	["162.158.0.0/15",		"US", "Cloudflare", "allocated"],
	["104.16.0.0/13",		"US", "Cloudflare", "allocated"],
	["104.24.0.0/14",		"US", "Cloudflare", "allocated"],
	["172.64.0.0/13",		"US", "Cloudflare", "allocated"],
	["131.0.72.0/22",		"US", "Cloudflare", "allocated"],
]

cidr_calc = {
	"4294967296": "0",
	"2147483648": "1",
	"1073741824": "2",
	"536870912": "3",
	"268435456": "4",
	"134217728": "5",
	"67108864": "6",
	"33554432": "7",
	"16777216": "8",
	"8388608": "9",
	"4194304": "10",
	"2097152": "11",
	"1048576": "12",
	"524288": "13",
	"262144": "14",
	"131072": "15",
	"65536": "16",
	"32768": "17",
	"16384": "18",
	"8192": "19",
	"4096": "20",
	"2048": "21",
	"1024": "22",
	"512": "23",
	"256": "24",
	"128": "25",
	"64": "26",
	"32": "27",
	"16": "28",
	"8": "29",
	"4": "30",
	"2": "31",
	"1": "32",
}


def download_file(url: str, filepath: str):
	# 检查文件是否存在
	if not os.path.isfile(filepath):
		import requests
		print(f"文件 {filepath} 不存在，正在下载...")
		# 发送HTTP GET请求到url
		response = requests.get(url, stream=True, headers={"Accept-Encoding": "gzip, deflate, br, zstd"})
		# 检查请求是否成功(状态码为200)
		if response.status_code == 200:
			# 打开一个文件以二进制写模式
			with open(filepath, "wb") as file:
				# 使用迭代器逐块写入文件
				for chunk in response.iter_content(1024):
					file.write(chunk)
		# print(f"文件 {filepath} 下载完成.")
	else:
		# print(f"文件 {filepath} 已存在.")
		pass


def process_cidr(filepath: str):
	"""
	处理CIDR数据，返回IPv4和IPv6的字典。

	The version line:
	0       1        2      3       4         5       6
	version|registry|serial|records|startdate|enddate|UTCoffset

	The summary line:
	0        1 2    3 4     [5]
	registry|*|type|*|count|summary

	Record format:
	0        1  2    3     4     5    6       7
	registry|cc|type|start|value|date|status[|extensions...]

	"""
	import csv
	# import math
	with open(filepath, "r") as file:
		reader = csv.reader(file, delimiter="|")
		for line in reader:
			if line[0].startswith("#"):
				continue
			if line[1] in ["afrinic", "apnic", "arin", "iana", "lacnic", "ripe-ncc", "ripencc"]:
				continue
			if line[2] == "asn":
				continue
			if line[5] == "summary":
				continue
			if line[3] in ["", "\t"]:
				continue
			if line[2] == "ipv4":
				if line[4] not in cidr_calc:
					cidr = f"{line[3]}+{line[4]}"
				else:
					cidr = f"{line[3]}/{cidr_calc[line[4]]}"
				# cidr_block = str(32 - int(math.log2(int(line[4]))))
			elif line[2] == "ipv6":
				cidr = f"{line[3]}/{line[4]}"
			if line[1] == "":
				region = "XX"
			else:
				region = line[1]
			ips.append([cidr, region, line[0], line[6]])


def query_ip(ip: str):
	try:
		ipaddress.ip_network(ip, strict=False)
		# ipaddress.ip_address(ip)
		pass
	except ValueError:
		print()
		return
	for item in ips:
		if ip == item[0]:
			print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
		elif "/" in item[0]:
			if ip_in_range(ip, item[0]):
				print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")
		elif "+" in item[0]:
			if ip_in_custom_range(ip, item[0]):
				print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def query_region(region: str):
	for item in ips:
		if region == item[1]:
			print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def query_status(status: str):
	for item in ips:
		if status == item[3]:
			print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def query_all():
	for item in ips:
		print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def ip_in_range(ip: str, cidr: str) -> bool:
	"""
	检查IP地址是否在CIDR范围内。
	"""
	try:
		ip_network = ipaddress.ip_network(cidr, strict=False)
		ip_address = ipaddress.ip_address(ip)
		return ip_address in ip_network
	except ValueError:
		return False


def ip_in_custom_range(ip: str, ip_range: str) -> bool:
	if ":" in ip:
		return False
	if "/" in ip:
		return False
	# 解析自定义IP范围字符串
	start_ip_str, count_str = ip_range.split("+")
	start_ip = int(ipaddress.IPv4Address(start_ip_str))
	count = int(count_str)
	end_ip = start_ip + count - 1

	# 将给定的IP地址转换为整数表示
	ip_int = int(ipaddress.IPv4Address(ip))

	# 检查IP地址是否在范围内
	return start_ip <= ip_int <= end_ip


if __name__ == "__main__":
	init()
	try:
		while True:
			ip = input("请输入IPv4或IPv6地址（输入'exit'退出）: ").strip()
			if ip == "":
				continue
			elif ip == "exit":
				break
			elif ip.lower() == "all":
				query_all()
			elif ip.lower() in ["clear", "cls"]:
				if sys.platform == "win32":
					os.system("cls")
				else:
					os.system("clear")
			elif ip.lower() == "dump":
				import json
				open("Z:\\dump.json", "w", encoding="utf-8").write(json.dumps(ips, ensure_ascii=False, separators=(",", ":")))
			elif len(ip) == 2 and ip.upper() in ISO3166_1 or ip.upper() in ["XX", "ZZ"]:
				query_region(ip.upper())
			elif ip.lower() in ["allocated", "assigned", "reserved", "available"]:
				query_status(ip.lower())
			elif ip.lower() in ["afrinic", "apnic", "arin", "iana", "lacnic", "ripe-ncc", "ripencc"]:
				query_status(ip.lower())
			else:
				try:
					query_ip(ip)
				except Exception as e:
					print(e)
					continue
	except KeyboardInterrupt:
		# print("exit")
		exit(0)
