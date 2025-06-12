import csv
import dataclasses
import ipaddress
import json
import socket
import sys
from pathlib import Path

import requests


@dataclasses.dataclass
class IP:
    ip_cidr: str = ""
    region: str = ""
    """ISO 3166-1"""
    desc: str = ""
    status: str = ""

    def __str__(self) -> str:
        return f"{self.ip_cidr}\t{self.region}\t{self.desc}\t{self.status}"

    def __hash__(self) -> int:
        return hash(self.ip_cidr + self.region)


def _init(*, overwrite: bool = False) -> None:
    PATH_BASE = Path("Z:\\")
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
    _download_file(tld_url, PATH_BASE / "tlds-alpha-by-domain.txt", overwrite=overwrite)
    _process_tld(PATH_BASE / "tlds-alpha-by-domain.txt")
    for url in URL:
        file_name = PATH_BASE / url.split("/")[-1]
        _download_file(url, file_name, overwrite=overwrite)
        _process_file(file_name)


_ISO3166_1: set[str] = {
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
    "xx",  # extra description
    "zz",  # iana
}
_IPS_DEFAULT = {
    IP("0.0.0.0/8", "XX", "[IANA]This network", "reserved"),
    IP("0.0.0.0/32", "XX", "[IANA]This host on this network", "reserved"),
    IP("10.0.0.0/8", "XX", "[IANA]Private-Use", "reserved"),
    IP("100.64.0.0/10", "XX", "[IANA]Shared Address Space", "reserved"),
    IP("127.0.0.0/8", "XX", "[IANA]Loopback", "reserved"),
    IP("169.254.0.0/16", "XX", "[IANA]Link Local", "reserved"),
    IP("172.16.0.0/12", "XX", "[IANA]Private-Use", "reserved"),
    IP("192.0.0.0/24", "XX", "[IANA]IETF Protocol Assignments", "reserved"),
    IP("192.0.0.0/29", "XX", "[IANA]IPv4 Service Continuity Prefix", "reserved"),
    IP("192.0.0.8/32", "XX", "[IANA]IPv4 dummy address", "reserved"),
    IP("192.0.0.9/32", "XX", "[IANA]Port Control Protocol Anycast", "reserved"),
    IP("192.0.0.10/32", "XX", "[IANA]Traversal Using Relays around NAT Anycast", "reserved"),
    IP("192.0.0.170/32", "XX", "[IANA]NAT64/DNS64 Discovery", "reserved"),
    IP("192.0.0.171/32", "XX", "[IANA]NAT64/DNS64 Discovery", "reserved"),
    IP("192.0.2.0/24", "XX", "[IANA]Documentation (TEST-NET-1)", "reserved"),
    IP("192.31.196.0/24", "XX", "[IANA]AS112-v4", "reserved"),
    IP("192.52.193.0/24", "XX", "[IANA]AMT", "reserved"),
    IP("192.88.99.0/24", "XX", "[IANA]Deprecated (6to4 Relay Anycast)", "reserved"),
    IP("192.168.0.0/16", "XX", "[IANA]Private-Use", "reserved"),
    IP("192.175.48.0/24", "XX", "[IANA]Direct Delegation AS112 Service", "reserved"),
    IP("198.18.0.0/15", "XX", "[IANA]Benchmarking", "reserved"),
    IP("198.51.100.0/24", "XX", "[IANA]Documentation (TEST-NET-2)", "reserved"),
    IP("203.0.113.0/24", "XX", "[IANA]Documentation (TEST-NET-3)", "reserved"),
    IP("240.0.0.0/4", "XX", "[IANA]Reserved", "reserved"),
    IP("255.255.255.255/32", "XX", "[IANA]Limited Broadcast", "reserved"),
    IP("224.0.0.0/28", "XX", "Multicast", "reserved"),
    IP("2000::/3", "XX", "global", "reserved"),
    IP("fe80::/10", "XX", "local", "reserved"),
    IP("fc00::/7", "XX", "local", "reserved"),
    IP("::1/128", "XX", "loopback", "reserved"),
    IP("::/128", "XX", "listening", "reserved"),
    IP("::/80", "XX", "ipv4-in-ipv6", "reserved"),
    IP("103.21.244.0/22", "US", "Cloudflare", "allocated"),
    IP("103.22.200.0/22", "US", "Cloudflare", "allocated"),
    IP("103.31.4.0/22", "US", "Cloudflare", "allocated"),
    IP("104.16.0.0/13", "US", "Cloudflare", "allocated"),
    IP("104.24.0.0/14", "US", "Cloudflare", "allocated"),
    IP("108.162.192.0/18", "US", "Cloudflare", "allocated"),
    IP("131.0.72.0/22", "US", "Cloudflare", "allocated"),
    IP("141.101.64.0/18", "US", "Cloudflare", "allocated"),
    IP("162.158.0.0/15", "US", "Cloudflare", "allocated"),
    IP("172.64.0.0/13", "US", "Cloudflare", "allocated"),
    IP("173.245.48.0/20", "US", "Cloudflare", "allocated"),
    IP("188.114.96.0/20", "US", "Cloudflare", "allocated"),
    IP("190.93.240.0/20", "US", "Cloudflare", "allocated"),
    IP("197.234.240.0/22", "US", "Cloudflare", "allocated"),
    IP("198.41.128.0/17", "US", "Cloudflare", "allocated"),
    IP("8.8.8.8/32", "US", "Google_DNS", "allocated"),
    IP("8.8.4.4/32", "US", "Google_DNS", "allocated"),
    IP("9.9.9.9/32", "US", "IBM_Quad9_DNS", "allocated"),
    IP("2400:cb00::/32", "US", "Cloudflare", "allocated"),
    IP("2405:8100::/32", "US", "Cloudflare", "allocated"),
    IP("2405:b500::/32", "US", "Cloudflare", "allocated"),
    IP("2606:4700::/32", "US", "Cloudflare", "allocated"),
    IP("2803:f800::/32", "US", "Cloudflare", "allocated"),
    IP("2a06:98c0::/29", "US", "Cloudflare", "allocated"),
    IP("2c0f:f248::/32", "US", "Cloudflare", "allocated"),
    IP("2001:4860:4860::8888/128", "US", "Google_DNS", "allocated"),
    IP("2001:4860:4860::8844/128", "US", "Google_DNS", "allocated"),
}
ips: set[IP] = set()
_tld = set()
"""iana top-level domains"""
_CIDR_CALC: dict[str | int, str] = {
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
    4294967296: "0",
    2147483648: "1",
    1073741824: "2",
    536870912: "3",
    268435456: "4",
    134217728: "5",
    67108864: "6",
    33554432: "7",
    16777216: "8",
    8388608: "9",
    4194304: "10",
    2097152: "11",
    1048576: "12",
    524288: "13",
    262144: "14",
    131072: "15",
    65536: "16",
    32768: "17",
    16384: "18",
    8192: "19",
    4096: "20",
    2048: "21",
    1024: "22",
    512: "23",
    256: "24",
    128: "25",
    64: "26",
    32: "27",
    16: "28",
    8: "29",
    4: "30",
    2: "31",
    1: "32",
}


def _download_file(url: str, file_name: Path, *, overwrite: bool) -> None:
    if file_name.is_file() and (not overwrite):
        # file {} exist
        # print(f"文件 {file_name} 已存在.")
        return
    if overwrite:
        # file {} not exist, downloading...
        print(f"文件 {file_name} 正在下载...")
    else:
        # file {} not exist, downloading...
        print(f"文件 {file_name} 不存在，正在下载...")
    response = requests.get(url, headers={"Accept-Encoding": "gzip, deflate, bzip2, br, zstd"})
    if response.status_code == 200:
        with file_name.open("wb") as file:
            file.write(response.content)
        # print(f"文件 {file_name} 下载完成.")


def _process_file(file_name: Path) -> None:
    """处理CIDR数据,返回IPv4和IPv6的字典
    The version line:
    0       1        2      3       4         5       6
    version|registry|serial|records|start-date|end-date|UTCoffset
    The summary line:
    0        1 2    3 4     [5]
    registry|*|type|*|count|summary
    Record format:
    0        1  2    3     4     5    6       7
    registry|cc|type|start|value|date|status[|extensions...]
    """
    # import math
    with file_name.open(encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="|")
        for line in reader:
            if line[0].startswith("#"):
                continue
            if line[1] in {"afrinic", "apnic", "arin", "iana", "lacnic", "ripe-ncc", "ripencc"}:
                continue
            region = "XX" if line[1] == "" else line[1]
            if line[5] == "summary":
                continue
            if line[3] in {"", "\t"}:
                continue
            if line[2] == "asn":
                continue
            if line[2] == "ipv4":
                cidr = f"{line[3]}/{_CIDR_CALC[line[4]]}" if line[4] in _CIDR_CALC else f"{line[3]}+{line[4]}"
                ips.add(IP(cidr, region, line[0], line[6]))
            elif line[2] == "ipv6":
                cidr = f"{line[3]}/{line[4]}"
                ips.add(IP(cidr, region, line[0], line[6]))


def _process_tld(file_name: Path) -> None:
    with file_name.open(encoding="utf-8") as file:
        for i in file:
            if i.startswith("#"):
                continue
            _tld.add(f".{i.lower().strip()}")


def _query_ip(d: str) -> None:
    try:
        ipaddress.ip_network(d, strict=False)
    except ValueError:
        print("resolving " + d)
        for i in _resolve_dns(d):
            print("resolved " + i)
            _query_ip(i)
        print("done " + d)
        return
    ip: IP
    for ip in ips:
        if d == ip.ip_cidr:
            print("".join(str(ip)))
        elif "/" in ip.ip_cidr:
            if _ip_in_range(d, ip.ip_cidr):
                print(ip)
        elif "+" in ip.ip_cidr and _ip_in_custom_range(d, ip.ip_cidr):
            print(ip)


def _resolve_dns(host: str) -> list[str]:
    try:
        ip_addresses = socket.getaddrinfo(host, None)
        return [str(addr[4][0]) for addr in ip_addresses]
    except socket.gaierror as e:
        print(f"Failed to resolve DNS for {host}: {e}")
        return []


def _query_region(d: str) -> None:
    for ip in ips:
        if d == ip.region:
            print(ip)


def _query_desc(d: str) -> None:
    for ip in ips:
        if d == ip.desc:
            print(ip)


def _query_status(d: str) -> None:
    for ip in ips:
        if d == ip.status:
            print(ip)


def _list_all() -> None:
    for ip in ips:
        print(ip)


def _ip_in_range(ip: str, ipr: str) -> bool:
    """检查IP地址是否在CIDR范围内."""
    try:
        ip_network: ipaddress.IPv4Network | ipaddress.IPv6Network = ipaddress.ip_network(ipr, strict=False)
        ip_address: ipaddress.IPv4Address | ipaddress.IPv6Address = ipaddress.ip_address(ip)
        return ip_address in ip_network
    except ValueError:
        return False


def _ip_in_custom_range(ip: str, ip_range: str) -> bool:
    if ":" in ip or "/" in ip:
        return _ip_in_range(ip, ip_range)
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
    ips = _IPS_DEFAULT.copy()
    _init()
    try:
        while True:
            # input ipv4 or ipv6 or domain, 'exit' to exit
            query_string = input("请输入IP地址（输入'exit'退出）: ").strip().lower()
            match query_string:
                case "":
                    continue
                case "exit":
                    raise SystemExit(0)
                case "all":
                    _list_all()
                case "len" | "len()" | "length":
                    print(len(ips))
                case "dump" | "export" | "save":
                    j = json.dumps(ips, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
                    Path("Z:\\dump.json").open("w", encoding="utf-8").write(j)
                    del j
                case "afrinic" | "apnic" | "arin" | "iana" | "lacnic" | "ripe-ncc" | "ripencc":
                    _query_desc(query_string)
                case "allocated" | "assigned" | "reserved" | "available":
                    _query_status(query_string)
                case "update":
                    ips.clear()
                    ips = _IPS_DEFAULT.copy()
                    _init(overwrite=True)
                case _:
                    if query_string in _ISO3166_1:
                        _query_region(query_string.upper())
                    elif ":" in query_string or "." in query_string:
                        _query_ip(query_string)
    except KeyboardInterrupt:
        # print("exit")
        sys.exit(0)
