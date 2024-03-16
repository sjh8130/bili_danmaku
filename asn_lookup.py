import csv
import os
import requests

PATHBASE = "Z:\\"
FILEPATH = (
	f"{PATHBASE}delegated-iana-latest",#互联网号码分配局#~1500
	f"{PATHBASE}delegated-apnic-latest",#亚太互联网络信息中心#~160,000
	f"{PATHBASE}delegated-arin-latest",#美洲互联网号码注册管理机构#~70000
	f"{PATHBASE}delegated-ripencc-latest",#欧洲IP网络资源协调中心#~120,000
	f"{PATHBASE}delegated-lacnic-latest",#拉丁美洲及加勒比地区互联网地址注册管理机构#~20000
	f"{PATHBASE}delegated-afrinic-latest",#非洲网络信息中心#~9000
)
URL_BASE1 = "https://ftp.apnic.net/stats"
URL_BASE2 = "https://ftp.arin.net/pub/stats"
URL_BASE = URL_BASE1
URL = (
	f"{URL_BASE}/iana/delegated-iana-latest",
	f"{URL_BASE}/apnic/delegated-apnic-latest",
	f"{URL_BASE}/arin/delegated-arin-extended-latest",
	f"{URL_BASE}/ripe-ncc/delegated-ripencc-latest",
	f"{URL_BASE}/lacnic/delegated-lacnic-latest",
	f"{URL_BASE}/afrinic/delegated-afrinic-latest",
)


ISO3166_1 = ["AD","AE","AF","AG","AI","AL","AM","AO","AQ","AR","AS","AT","AU","AW","AX","AZ",
	"BA","BB","BD","BE","BF","BG","BH","BI","BJ","BL","BM","BN","BO","BQ","BR","BS","BT","BV","BW","BY","BZ",
	"CA","CC","CD","CF","CG","CH","CI","CK","CL","CM","CN","CO","CR","CU","CV","CW","CX","CY","CZ",
	"DE","DJ","DK","DM","DO","DZ",
	"EC","EE","EG","EH","ER","ES","ET",
	"FI","FJ","FK","FM","FO","FR",
	"GA","GB","GD","GE","GF","GG","GH","GI","GL","GM","GN","GP","GQ","GR","GS","GT","GU","GW","GY",
	"HK","HM","HN","HR","HT","HU",
	"ID","IE","IL","IM","IN","IO","IQ","IR","IS","IT",
	"JE","JM","JO","JP",
	"KE","KG","KH","KI","KM","KN","KP","KR","KW","KY","KZ",
	"LA","LB","LC","LI","LK","LR","LS","LT","LU","LV","LY",
	"MA","MC","MD","ME","MF","MG","MH","MK","ML","MM","MN","MO","MP","MQ","MR","MS","MT","MU","MV","MW","MX","MY","MZ",
	"NA","NC","NE","NF","NG","NI","NL","NO","NP","NR","NU","NZ",
	"OM",
	"PA","PE","PF","PG","PH","PK","PL","PM","PN","PR","PS","PT","PW","PY",
	"QA",
	"RE","RO","RS","RU","RW",
	"SA","SB","SC","SD","SE","SG","SH","SI","SJ","SK","SL","SM","SN","SO","SR","SS","ST","SV","SX","SY","SZ",
	"TC","TD","TF","TG","TH","TJ","TK","TL","TM","TN","TO","TR","TT","TV","TW","TZ",
	"UA","UG","UM","US","UY","UZ",
	"VA","VC","VE","VG","VI","VN","VU",
	"WF","WS",
	"YE","YT",
	"ZA","ZM","ZW",
]

ips = [
]


def download_file(url, filepath):
	# 检查文件是否存在
	if not os.path.isfile(filepath):
		print(f"文件 {filepath} 不存在，正在下载...")
		# 发送HTTP GET请求到url
		response = requests.get(url, stream=True)
		# 检查请求是否成功(状态码为200)
		if response.status_code == 200:
			# 打开一个文件以二进制写模式
			with open(filepath, 'wb') as file:
				# 使用迭代器逐块写入文件
				for chunk in response.iter_content(1024):
					file.write(chunk)
		print(f"文件 {filepath} 下载完成.")
	else:
		# print(f"文件 {filepath} 已存在.")
		pass


def process_cidr(filepath: str):
	"""
	处理CIDR数据，返回IPv4和IPv6的字典。
	0        1  2    3     4     5    6       
	registry|cc|type|start|value|date|status[|extensions...]
	"""
	import math
	with open(filepath, "r") as file:
		reader = csv.reader(file, delimiter='|')
		for line in reader:
			if line[0].startswith("#"):
				continue
			if line[1] in ["afrinic", "apnic", "arin", "iana", "lacnic", "ripe-ncc", "ripencc"]:
				continue
			if line[2] == "asn":
				continue
			if line[5] == "summary":
				continue
			if line[2] == 'ipv4':
				cidr_block = str(32 - int(math.log2(int(line[4]))))
			elif line[2] == 'ipv6':
				cidr_block = line[4]
			ips.append([f"{line[3]}/{cidr_block}", line[1], line[0], line[6]])


def query_ip(ip):
	for item in ips:
		if ip_in_range(ip, item[0]):
			print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def query_region(region):
	for item in ips:
		if region == item[1]:
			print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def query_status(status):
	for item in ips:
		if status == item[3]:
			print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def query_all():
	for item in ips:
		print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}")


def ip_in_range(ip, cidr):
	"""
	检查IP地址是否在CIDR范围内。
	"""
	import ipaddress
	try:
		ip_network = ipaddress.ip_network(cidr, strict=False)
		ip_address = ipaddress.ip_address(ip)
		return ip_address in ip_network
	except ValueError:
		return False


if __name__ == "__main__":
	for url, filepath in zip(URL, FILEPATH):
		download_file(url, filepath)
		process_cidr(filepath)
	try:
		while True:
			ip = input("请输入IPv4或IPv6地址（输入'exit'退出）: ")
			if ip == '':
				continue
			elif ip == 'exit':
				break
			elif ip.lower() == 'all':
				query_all()
			elif len(ip) == 2 and ip.upper() in ISO3166_1 or ip.upper() in ["ZZ"]:
				query_region(ip.upper())
			elif ip.lower() in ["allocated", "assigned", "reserved", "available"]:
				query_status(ip.lower())
			elif ip.lower() in ["afrinic", "apnic", "arin", "iana", "lacnic", "ripe-ncc", "ripencc"]:
				query_status(ip.lower())
			else:
				query_ip(ip)
	except KeyboardInterrupt:
		print("exit")
		exit(0)
