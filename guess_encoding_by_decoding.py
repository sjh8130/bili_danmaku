import contextlib

ALL_UNICODE_ENCODINGS = [
    "ascii",
    "big5",
    "big5hkscs",
    "charmap",
    "cp037",
    "cp1006",
    "cp1026",
    "cp1125",
    "cp1140",
    "cp1250",
    "cp1251",
    "cp1252",
    "cp1253",
    "cp1254",
    "cp1255",
    "cp1256",
    "cp1257",
    "cp1258",
    "cp424",
    "cp437",
    "cp500",
    "cp720",
    "cp737",
    "cp775",
    "cp850",
    "cp852",
    "cp855",
    "cp856",
    "cp857",
    "cp858",
    "cp860",
    "cp861",
    "cp862",
    "cp863",
    "cp864",
    "cp865",
    "cp866",
    "cp869",
    "cp874",
    "cp875",
    "cp932",
    "cp949",
    "cp950",
    "euc_jis_2004",
    "euc_jisx0213",
    "euc_jp",
    "euc_kr",
    "gb18030",
    "gb2312",
    "gbk",
    "hp_roman8",
    "hz",
    "idna",
    "iso2022_jp",
    "iso2022_jp_1",
    "iso2022_jp_2",
    "iso2022_jp_2004",
    "iso2022_jp_3",
    "iso2022_jp_ext",
    "iso2022_kr",
    "iso8859_1",
    "iso8859_10",
    "iso8859_11",
    "iso8859_13",
    "iso8859_14",
    "iso8859_15",
    "iso8859_16",
    "iso8859_2",
    "iso8859_3",
    "iso8859_4",
    "iso8859_5",
    "iso8859_6",
    "iso8859_7",
    "iso8859_8",
    "iso8859_9",
    "johab",
    "koi8_r",
    "koi8_t",
    "koi8_u",
    "kz1048",
    "latin_1",
    "mac_cyrillic",
    "mac_greek",
    "mac_iceland",
    "mac_latin2",
    "mac_roman",
    "mac_turkish",
    "palmos",
    "ptcp154",
    "punycode",
    "raw_unicode_escape",
    "shift_jis",
    "shift_jis_2004",
    "shift_jisx0213",
    "tis_620",
    "unicode_escape",
    "utf_16",
    "utf_16_be",
    "utf_16_le",
    "utf_7",
    "utf_8",
]


def safe_print(s: str):
    s = s.replace("\x00", "\\x00")
    s = s.replace("\x01", "\\x01")
    s = s.replace("\x02", "\\x02")
    s = s.replace("\x03", "\\x03")
    s = s.replace("\x04", "\\x04")
    s = s.replace("\x05", "\\x05")
    s = s.replace("\x06", "\\x06")
    s = s.replace("\x07", "\\x07")
    s = s.replace("\x08", "\\x08")
    s = s.replace("\x09", "\\x09")
    s = s.replace("\x0a", "\\x0a")
    s = s.replace("\x0b", "\\x0b")
    s = s.replace("\x0c", "\\x0c")
    s = s.replace("\x0d", "\\x0d")
    s = s.replace("\x0e", "\\x0e")
    s = s.replace("\x0f", "\\x0f")
    s = s.replace("\x10", "\\x10")
    s = s.replace("\x11", "\\x11")
    s = s.replace("\x12", "\\x12")
    s = s.replace("\x13", "\\x13")
    s = s.replace("\x14", "\\x14")
    s = s.replace("\x15", "\\x15")
    s = s.replace("\x16", "\\x16")
    s = s.replace("\x17", "\\x17")
    s = s.replace("\x18", "\\x18")
    s = s.replace("\x19", "\\x19")
    s = s.replace("\x1a", "\\x1a")
    s = s.replace("\x1b", "\\x1b")
    s = s.replace("\x1c", "\\x1c")
    s = s.replace("\x1d", "\\x1d")
    s = s.replace("\x1e", "\\x1e")
    s = s.replace("\x1f", "\\x1f")
    print(s)


def guess_encoding_by_decoding(byte_data: str) -> None:
    final_set = set()
    for enc in ALL_UNICODE_ENCODINGS:
        try:
            bb = byte_data.encode(enc)
            for dec in ALL_UNICODE_ENCODINGS:
                with contextlib.suppress(Exception):
                    final_set.add(bb.decode(dec))
        except:
            pass
    for x in sorted(final_set):
        safe_print(x)
    # print(sorted(final_set))


def main():
    while True:
        guess_encoding_by_decoding(input())


if __name__ == "__main__":
    main()
