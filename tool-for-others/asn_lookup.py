import os
import sys
import ipaddress
import socket


class ip:
    ip_addr: str
    region: str
    desc: str
    status: str

    def __init__(self, ip_cidr, region, desc, status) -> None:
        self.ip_addr = ip_cidr
        self.region = region
        self.desc = desc
        self.status = status

    def __str__(self) -> str:
        return f"{self.ip_addr}\t{self.region}\t{self.desc}\t{self.status}"


def init(overwrite=False) -> None:
    PATH_BASE = "Z:\\"
    URL_BASE = "https://ftp.apnic.net/stats"
    URL = [
        f"{URL_BASE}/iana/delegated-iana-latest",
        f"{URL_BASE}/apnic/delegated-apnic-latest",
        f"{URL_BASE}/arin/delegated-arin-extended-latest",
        f"{URL_BASE}/ripe-ncc/delegated-ripencc-latest",
        f"{URL_BASE}/lacnic/delegated-lacnic-latest",
        f"{URL_BASE}/afrinic/delegated-afrinic-latest",
    ]
    tld_url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
    download_file(tld_url, PATH_BASE + "tlds-alpha-by-domain.txt", overwrite)
    process_tld(PATH_BASE + "tlds-alpha-by-domain.txt")
    for url in URL:
        file_name = PATH_BASE + url.split("/")[-1]
        download_file(url, file_name, overwrite)
        process_file(file_name)


ISO3166_1 = [
    "ad",
    "ae",
    "af",
    "ag",
    "ai",
    "al",
    "am",
    "ao",
    "aq",
    "ar",
    "as",
    "at",
    "au",
    "aw",
    "ax",
    "az",
    "ba",
    "bb",
    "bd",
    "be",
    "bf",
    "bg",
    "bh",
    "bi",
    "bj",
    "bl",
    "bm",
    "bn",
    "bo",
    "bq",
    "br",
    "bs",
    "bt",
    "bv",
    "bw",
    "by",
    "bz",
    "ca",
    "cc",
    "cd",
    "cf",
    "cg",
    "ch",
    "ci",
    "ck",
    "cl",
    "cm",
    "cn",
    "co",
    "cr",
    "cu",
    "cv",
    "cw",
    "cx",
    "cy",
    "cz",
    "de",
    "dj",
    "dk",
    "dm",
    "do",
    "dz",
    "ec",
    "ee",
    "eg",
    "eh",
    "er",
    "es",
    "et",
    "fi",
    "fj",
    "fk",
    "fm",
    "fo",
    "fr",
    "ga",
    "gb",
    "gd",
    "ge",
    "gf",
    "gg",
    "gh",
    "gi",
    "gl",
    "gm",
    "gn",
    "gp",
    "gq",
    "gr",
    "gs",
    "gt",
    "gu",
    "gw",
    "gy",
    "hk",
    "hm",
    "hn",
    "hr",
    "ht",
    "hu",
    "id",
    "ie",
    "il",
    "im",
    "in",
    "io",
    "iq",
    "ir",
    "is",
    "it",
    "je",
    "jm",
    "jo",
    "jp",
    "ke",
    "kg",
    "kh",
    "ki",
    "km",
    "kn",
    "kp",
    "kr",
    "kw",
    "ky",
    "kz",
    "la",
    "lb",
    "lc",
    "li",
    "lk",
    "lr",
    "ls",
    "lt",
    "lu",
    "lv",
    "ly",
    "ma",
    "mc",
    "md",
    "me",
    "mf",
    "mg",
    "mh",
    "mk",
    "ml",
    "mm",
    "mn",
    "mo",
    "mp",
    "mq",
    "mr",
    "ms",
    "mt",
    "mu",
    "mv",
    "mw",
    "mx",
    "my",
    "mz",
    "na",
    "nc",
    "ne",
    "nf",
    "ng",
    "ni",
    "nl",
    "no",
    "np",
    "nr",
    "nu",
    "nz",
    "om",
    "pa",
    "pe",
    "pf",
    "pg",
    "ph",
    "pk",
    "pl",
    "pm",
    "pn",
    "pr",
    "ps",
    "pt",
    "pw",
    "py",
    "qa",
    "re",
    "ro",
    "rs",
    "ru",
    "rw",
    "sa",
    "sb",
    "sc",
    "sd",
    "se",
    "sg",
    "sh",
    "si",
    "sj",
    "sk",
    "sl",
    "sm",
    "sn",
    "so",
    "sr",
    "ss",
    "st",
    "sv",
    "sx",
    "sy",
    "sz",
    "tc",
    "td",
    "tf",
    "tg",
    "th",
    "tj",
    "tk",
    "tl",
    "tm",
    "tn",
    "to",
    "tr",
    "tt",
    "tv",
    "tw",
    "tz",
    "ua",
    "ug",
    "um",
    "us",
    "uy",
    "uz",
    "va",
    "vc",
    "ve",
    "vg",
    "vi",
    "vn",
    "vu",
    "wf",
    "ws",
    "ye",
    "yt",
    "za",
    "zm",
    "zw",
] + [
    "xx",  # extra description
    "zz",  # iana
]

IPS = [
    ip("0.0.0.0/8", "XX", "listening", "reserved"),
    ip("10.0.0.0/8", "XX", "PRIVATE-A", "reserved"),
    ip("127.0.0.0/8", "XX", "loopback", "reserved"),
    ip("169.254.0.0/16", "XX", "LinkLocal", "reserved"),
    ip("172.16.0.0/12", "XX", "PRIVATE-B", "reserved"),
    ip("192.168.0.0/16", "XX", "PRIVATE-C", "reserved"),
    ip("224.0.0.0/28", "XX", "Multicast", "reserved"),
    ip("240.0.0.0/28", "XX", "Reserved-E", "reserved"),
    ip("255.255.255.255/32", "XX", "Broadcast", "reserved"),
    ip("2000::/3", "XX", "global", "reserved"),
    ip("fe80::/10", "XX", "local", "reserved"),
    ip("fc00::/7", "XX", "local", "reserved"),
    ip("::1/128", "XX", "loopback", "reserved"),
    ip("::/128", "XX", "listening", "reserved"),
    ip("::/80", "XX", "ipv4-in-ipv6", "reserved"),
    ip("173.245.48.0/20", "US", "Cloudflare", "allocated"),
    ip("103.21.244.0/22", "US", "Cloudflare", "allocated"),
    ip("103.22.200.0/22", "US", "Cloudflare", "allocated"),
    ip("103.31.4.0/22", "US", "Cloudflare", "allocated"),
    ip("141.101.64.0/18", "US", "Cloudflare", "allocated"),
    ip("108.162.192.0/18", "US", "Cloudflare", "allocated"),
    ip("190.93.240.0/20", "US", "Cloudflare", "allocated"),
    ip("188.114.96.0/20", "US", "Cloudflare", "allocated"),
    ip("197.234.240.0/22", "US", "Cloudflare", "allocated"),
    ip("198.41.128.0/17", "US", "Cloudflare", "allocated"),
    ip("162.158.0.0/15", "US", "Cloudflare", "allocated"),
    ip("104.16.0.0/13", "US", "Cloudflare", "allocated"),
    ip("104.24.0.0/14", "US", "Cloudflare", "allocated"),
    ip("172.64.0.0/13", "US", "Cloudflare", "allocated"),
    ip("131.0.72.0/22", "US", "Cloudflare", "allocated"),
    ip("8.8.8.8/32", "US", "Google_DNS", "allocated"),
    ip("8.8.4.4/32", "US", "Google_DNS", "allocated"),
    ip("9.9.9.9/32", "US", "IBM_Quad9_DNS", "allocated"),
    ip("2400:cb00::/32", "US", "Cloudflare", "allocated"),
    ip("2606:4700::/32", "US", "Cloudflare", "allocated"),
    ip("2803:f800::/32", "US", "Cloudflare", "allocated"),
    ip("2405:b500::/32", "US", "Cloudflare", "allocated"),
    ip("2405:8100::/32", "US", "Cloudflare", "allocated"),
    ip("2a06:98c0::/29", "US", "Cloudflare", "allocated"),
    ip("2c0f:f248::/32", "US", "Cloudflare", "allocated"),
    ip("2001:4860:4860::8888/128", "US", "Google_DNS", "allocated"),
    ip("2001:4860:4860::8844/128", "US", "Google_DNS", "allocated"),
]
ips = IPS

tld = []

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


def download_file(url: str, file_name: str, overwrite: bool) -> None:
    # 检查文件是否存在
    if os.path.isfile(file_name) and (not overwrite):
        # file exist
        print(f"文件 {file_name} 已存在.")
        pass
    else:
        import requests

        if overwrite:
            # file {} not exist, downloading...
            print(f"文件 {file_name} 正在下载...")
        else:
            # file {} not exist, downloading...
            print(f"文件 {file_name} 不存在，正在下载...")

        response = requests.get(
            url, headers={"Accept-Encoding": "gzip, deflate, br, zstd"}
        )
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)
        # print(f"文件 {file_name} 下载完成.")


def process_file(file_name: str) -> None:
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
    with open(file_name, "r") as file:
        reader = csv.reader(file, delimiter="|")
        for line in reader:
            if line[0].startswith("#"):
                continue
            if line[1] in [
                "afrinic",
                "apnic",
                "arin",
                "iana",
                "lacnic",
                "ripe-ncc",
                "ripencc",
            ]:
                continue
            elif line[1] == "":
                region = "XX"
            else:
                region = line[1]
            if line[5] == "summary":
                continue
            if line[3] in ["", "\t"]:
                continue
            if line[2] == "asn":
                continue
            elif line[2] == "ipv4":
                if line[4] in cidr_calc:
                    cidr = f"{line[3]}/{cidr_calc[line[4]]}"
                else:
                    cidr = f"{line[3]}+{line[4]}"
                ips.append(ip(cidr, region, line[0], line[6]))
            elif line[2] == "ipv6":
                cidr = f"{line[3]}/{line[4]}"
                ips.append(ip(cidr, region, line[0], line[6]))


# iana top-level domains
def process_tld(file_name: str) -> None:
    with open(file_name, "r") as file:
        tlds = file.readlines()
    for i in tlds:
        if i.startswith("#"):
            continue
        tld.append(f".{i.lower().strip()}")


def query_0(d: str):
    try:
        ipaddress.ip_network(d, strict=False)
        pass
    except ValueError:
        print("resolving " + d)
        for i in resolve_dns(d):
            print("resolved " + i)
            query_0(i)
        print("done " + d)
        return
    item: ip
    for item in ips:
        if d == item.ip_addr:
            print(str.join(item))
        elif "/" in item.ip_addr:
            if ip_in_range(d, item.ip_addr):
                print(item)
        elif "+" in item.ip_addr:
            if ip_in_custom_range(d, item.ip_addr):
                print(item)


def resolve_dns(host):
    try:
        ip_addresses = socket.getaddrinfo(host, None)
        return [addr[4][0] for addr in ip_addresses]
    except socket.gaierror as e:
        print(f"Failed to resolve DNS for {host}: {e}")
        return []


def query_1(d: str):
    for item in ips:
        if d == item.region:
            print(item)


def query_2(d: str):
    for item in ips:
        if d == item.desc:
            print(item)


def query_3(d: str):
    for item in ips:
        if d == item.status:
            print(item)


def list_all():
    for item in ips:
        print(item)


def ip_in_range(ip: str, ipr: str) -> bool:
    """
    检查IP地址是否在CIDR范围内。
    """
    try:
        ip_network = ipaddress.ip_network(ipr, strict=False)
        ip_address = ipaddress.ip_address(ip)
        return ip_address in ip_network
    except ValueError:
        return False


def ip_in_custom_range(ip: str, ip_range: str) -> bool:
    if ":" in ip or "/" in ip:
        return ip_in_range(ip, ip_range)
    # 解析自定义IP范围字符串
    start_ip_str, count_str = ip_range.split("+")
    try:
        start_ip = int(ipaddress.IPv4Address(start_ip_str))
    except ipaddress.AddressValueError:
        return False
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
            # input ipv4 or ipv6 or domain, 'exit' to exit
            query_string = input("请输入IP地址（输入'exit'退出）: ").strip().lower()
            match query_string:
                case "":
                    continue
                case "exit":
                    raise KeyboardInterrupt
                case "all":
                    list_all()
                case "clear" | "cls":
                    if sys.platform == "win32":
                        os.system("cls")
                    else:
                        os.system("clear")
                case "len" | "len()" | "length":
                    print(len(ips))
                case "dump":
                    import json

                    j = json.dumps(ips, ensure_ascii=False, separators=(",", ":"))
                    open("Z:\\dump.json", "w", encoding="utf-8").write(j)
                    del j
                case (
                    "afrinic"
                    | "apnic"
                    | "arin"
                    | "iana"
                    | "lacnic"
                    | "ripe-ncc"
                    | "ripencc"
                ):
                    query_2(query_string)
                case "allocated" | "assigned" | "reserved" | "available":
                    query_3(query_string)
                case "update":
                    ips = IPS
                    init(overwrite=True)
                case _:
                    if query_string in ISO3166_1:
                        query_1(query_string.upper())
                        continue
                    query_0(query_string)
    except KeyboardInterrupt:
        # print("exit")
        exit(0)
