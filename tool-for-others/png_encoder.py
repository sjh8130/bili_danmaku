import math
import struct
import sys
import time
from typing import Generator
import zlib
from enum import IntEnum, StrEnum

from loguru import logger
from PIL import Image

logger.bind(user="PNG")
log = logger

# PNG signature
_PNG_SIGNATURE = b"\x89PNG\x0d\x0a\x1a\x0a"
_BRD_S32 = 2**32 - 1
_BRD_S16 = 2**16 - 1
_BRD_S8 = 2**8 - 1
_NULL_SEPARATOR = b"\x00"


class _PNG_COLOR_TYPE(IntEnum):
    GRAY = 0
    G = GRAY
    GRAYSCALE = GRAY
    GrayScale = GRAY
    Grayscale = GRAY
    grayscale = GRAY

    TRUECOLOR = 2
    TrueColor = TRUECOLOR
    Truecolor = TRUECOLOR
    truecolor = TRUECOLOR
    RGB = TRUECOLOR
    RGB24 = TRUECOLOR
    RGB48 = TRUECOLOR
    rgb = TRUECOLOR
    rgb24 = TRUECOLOR
    rgb48 = TRUECOLOR

    INDEXED_COLOR = 3
    PALETTE = INDEXED_COLOR
    palette = INDEXED_COLOR
    Palette = INDEXED_COLOR

    GRAYSCALE_WITH_ALPHA = 4
    GA = GRAYSCALE_WITH_ALPHA
    GRAY_A = GRAYSCALE_WITH_ALPHA
    GRAY_ALPHA = GRAYSCALE_WITH_ALPHA
    GRAYSCALE_ALPHA = GRAYSCALE_WITH_ALPHA
    Grayscale_with_alpha = GRAYSCALE_WITH_ALPHA
    GrayscaleWithAlpha = GRAYSCALE_WITH_ALPHA

    TRUECOLOR_WITH_ALPHA = 6
    TRUECOLORWITHALPHA = TRUECOLOR_WITH_ALPHA
    truecolorwithalpha = TRUECOLOR_WITH_ALPHA
    truecolorWithAlpha = TRUECOLOR_WITH_ALPHA
    TruecolorWithAlpha = TRUECOLOR_WITH_ALPHA
    TrueColorWithAlpha = TRUECOLOR_WITH_ALPHA
    Truecolor_with_alpha = TRUECOLOR_WITH_ALPHA
    truecolor_with_alpha = TRUECOLOR_WITH_ALPHA
    RGBA = TRUECOLOR_WITH_ALPHA
    RGBA32 = TRUECOLOR_WITH_ALPHA
    RGBA64 = TRUECOLOR_WITH_ALPHA
    RGB32 = TRUECOLOR_WITH_ALPHA
    RGB64 = TRUECOLOR_WITH_ALPHA
    rgba = TRUECOLOR_WITH_ALPHA
    rgb32 = TRUECOLOR_WITH_ALPHA
    rgb64 = TRUECOLOR_WITH_ALPHA
    rgba32 = TRUECOLOR_WITH_ALPHA
    rgba64 = TRUECOLOR_WITH_ALPHA


_ALLOWED_DEPTH_LIST: dict[_PNG_COLOR_TYPE, list[int]] = {
    _PNG_COLOR_TYPE.GRAY: [1, 2, 4, 8, 16],
    _PNG_COLOR_TYPE.TRUECOLOR: [8, 16],
    _PNG_COLOR_TYPE.INDEXED_COLOR: [1, 2, 4, 8, 16],
    _PNG_COLOR_TYPE.GRAY_ALPHA: [8, 16],
    _PNG_COLOR_TYPE.TRUECOLOR_WITH_ALPHA: [8, 16],
}


class Disposal(IntEnum):
    OP_NONE = 0
    OP_BACKGROUND = 1
    OP_PREVIOUS = 2


class Blend(IntEnum):
    OP_SOURCE = 0
    OP_OVER = 1


class _ZLIB_COMPRESSION_LEVEL(IntEnum):
    COPY = 0
    COMPRESSION_LEVEL_NONE = 0
    COMPRESSION_LEVEL_0 = 0
    COMPRESSION_LEVEL_1 = 1
    COMPRESSION_LEVEL_2 = 2
    COMPRESSION_LEVEL_3 = 3
    COMPRESSION_LEVEL_4 = 4
    COMPRESSION_LEVEL_5 = 5
    COMPRESSION_LEVEL_6 = 6
    COMPRESSION_LEVEL_7 = 7
    COMPRESSION_LEVEL_8 = 8
    COMPRESSION_LEVEL_9 = 9


class _SRGB_RENDERING_INTENT(IntEnum):
    SRGB_RENDERING_INTENT_PERCEPTUAL = 0
    SRGB_RENDERING_INTENT_RELATIVE_COLORIMETRIC = 1
    SRGB_RENDERING_INTENT_SATURATION = 2
    SRGB_RENDERING_INTENT_ABSOLUTE_COLORIMETRIC = 3


class _PHYS_UNIT(IntEnum):
    PHYS_UNIT_UNKNOWN = 0
    PHYS_UNIT_METER = 1


class _CHUNK_TYPE(StrEnum):
    # Critical chunks
    IHDR = "IHDR"  # Image header
    PLTE = "PLTE"  # color Palette
    IDAT = "IDAT"  # Image data
    IEND = "IEND"  # Image trailer
    tRNS = "tRNS"  # Transparency
    # Color space information
    cHRM = "cHRM"  # Primary chromaticities and white point
    gAMA = "gAMA"  # Image gamma
    iCCP = "iCCP"  # Embedded ICC profile
    sBIT = "sBIT"  # Significant bits
    sRGB = "sRGB"  # Standard RGB color space
    cICP = "cICP"  # Coding-independent code points for video signal type identification***
    mDCv = "mDCv"  # Mastering Display Color Volume***
    cLLi = "cLLi"  # Content Light Level Information***
    # Textual information
    iTXt = "iTXt"
    tEXt = "tEXt"
    zTXt = "zTXt"
    # Miscellaneous information
    bKGD = "bKGD"  # Background color***
    hIST = "hIST"  # ***
    pHYs = "pHYs"
    sPLT = "sPLT"  # ***
    eXIf = "eXIf"  # ***
    # Time information
    tIME = "tIME"
    # Animation information
    acTL = "acTL"
    fcTL = "fcTL"
    fdAT = "fdAT"


class P1:
    compression_level = _ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9
    apng_seq = 0

    def __init__(self, compression_level) -> None:
        self.compression_level = compression_level

    def _sign(self, chunk_type: bytes | str, data: bytes, /) -> bytes:
        if isinstance(chunk_type, str):
            chunk_type = chunk_type.encode()
        chunk_length = len(data)
        chunk_crc = struct.pack(">I", zlib.crc32(chunk_type + data, 0) & 0xFFFFFFFF)
        logger.debug(f"chunk_type={str(chunk_type,'utf-8')}, {chunk_length=}")
        return struct.pack(">I", chunk_length) + chunk_type + data + chunk_crc

    def IHDR(self, width: int, height: int, bit_depth: int, color_type: _PNG_COLOR_TYPE, compression_method: int = 0, filter_method: int = 0, interlace_method: int = 0):
        data = struct.pack(">IIBBBBB", width, height, bit_depth, color_type, compression_method, filter_method, interlace_method)
        return self._sign(_CHUNK_TYPE.IHDR, data)

    def PLTE(self, palette: list[tuple[int, int, int]]):
        data = b""
        for color in palette:
            data += struct.pack(">BBB", color[0], color[1], color[2])
        return self._sign(_CHUNK_TYPE.PLTE, data)

    def XDAT(self, image_data: bytes, width: int, height: int, bit_depth: int, color_type: _PNG_COLOR_TYPE, chunk_size: int, apng: bool = False) -> Generator[bytes]:
        compressor = zlib.compressobj(self.compression_level, wbits=15, memLevel=9)
        match color_type:
            case 0:
                if bit_depth == 1:
                    row_size = math.ceil(width / 8)
                elif bit_depth == 2:
                    row_size = math.ceil(width / 4)
                elif bit_depth == 4:
                    row_size = math.ceil(width / 2)
                elif bit_depth == 8:
                    row_size = width
                elif bit_depth == 16:
                    row_size = 2 * width
                else:
                    row_size = -1
            case 2:
                if bit_depth == 8:
                    row_size = 3 * width
                elif bit_depth == 16:
                    row_size = 6 * width
                else:
                    row_size = -1
            case 3:
                if bit_depth == 1:
                    row_size = math.ceil(width / 8)
                elif bit_depth == 2:
                    row_size = math.ceil(width / 4)
                elif bit_depth == 4:
                    row_size = math.ceil(width / 2)
                elif bit_depth == 8:
                    row_size = width
                else:
                    row_size = -1
            case 4:
                if bit_depth == 8:
                    row_size = 2 * width
                elif bit_depth == 16:
                    row_size = 4 * width
                else:
                    row_size = -1
            case 6:
                if bit_depth == 8:
                    row_size = 4 * width
                elif bit_depth == 16:
                    row_size = 8 * width
                else:
                    row_size = -1
            case _:
                row_size = -1
        if row_size == -1:
            raise ValueError()
        filtered_data = bytearray()
        for y in range(height):
            row_start = y * row_size
            row_end = row_start + row_size
            row = image_data[row_start:row_end]
            filtered_data.append(0)
            filtered_data.extend(row)
        compressed_data = zlib.compress(filtered_data)
        compressor.flush()
        for i in range(0, len(compressed_data), chunk_size):
            chunk_data = compressed_data[i : i + chunk_size]
            if apng:
                yield self._sign(_CHUNK_TYPE.fdAT, struct.pack(">I", self.apng_seq) + chunk_data)
                self.apng_seq += 1
            else:
                yield self._sign(_CHUNK_TYPE.IDAT, chunk_data)

    def IEND(self):
        return self._sign(b"IEND", b"")

    def tRNS(self, transparency: list[int]):
        return self._sign(_CHUNK_TYPE.tRNS, bytes(bytearray(transparency)))

    def gAMA(self, gamma: float):
        data = struct.pack(">I", int(gamma * 100000))
        return self._sign(_CHUNK_TYPE.gAMA, data)

    def iCCP(self, profile_name: str, profile_data: bytes):
        data = profile_name.encode() + b"\x00" + profile_data
        return self._sign(_CHUNK_TYPE.iCCP, data)

    def sRGB(self, rendering_intent: _SRGB_RENDERING_INTENT = _SRGB_RENDERING_INTENT.SRGB_RENDERING_INTENT_PERCEPTUAL):
        data = struct.pack(">B", rendering_intent)
        return self._sign(_CHUNK_TYPE.sRGB, data)

    def acTL(self, num_frames: int, num_plays: int):
        data = struct.pack(">II", num_frames, num_plays)
        return self._sign(_CHUNK_TYPE.acTL, data)

    def fcTL(self, width: int, height: int, x_offset: int, y_offset: int, delay_num: int = 1, delay_den: int = 30, dispose_op: Disposal = Disposal.OP_NONE, blend_op: Blend = Blend.OP_SOURCE):
        data = struct.pack(">IiiiiHHBB", self.apng_seq, width, height, x_offset, y_offset, delay_num, delay_den, dispose_op, blend_op)
        self.apng_seq += 1
        return self._sign(_CHUNK_TYPE.fcTL, data)

    def tEXt(self, keyword: str, text: str) -> bytes:
        data = keyword.encode() + _NULL_SEPARATOR + text.encode()
        return self._sign(_CHUNK_TYPE.tEXt, data)

    def zTXt(self, keyword: str, text: str) -> bytes:
        data = keyword.encode() + _NULL_SEPARATOR + b"\x00" + zlib.compress(text.encode(), _ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
        return self._sign(_CHUNK_TYPE.zTXt, data)

    def iTXt(self, keyword: str, text: str, language_tag: str = "", translated_keyword: str = "", compression_flag: bool = False) -> bytes:
        t1 = text.encode()
        if compression_flag:
            _text: bytes = zlib.compress(t1, _ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
            compression_method = 0
        else:
            _text = t1
            compression_method = 1
        data = keyword.encode() + _NULL_SEPARATOR + _text + struct.pack(">?B", compression_flag, compression_method) + language_tag.encode() + _NULL_SEPARATOR + translated_keyword.encode() + _NULL_SEPARATOR + text.encode()
        return self._sign(_CHUNK_TYPE.iTXt, data)

    def pHYs(self, pixels_per_unit_x: int, pixels_per_unit_y: int, unit: _PHYS_UNIT = _PHYS_UNIT.PHYS_UNIT_METER):
        data = struct.pack(">IIB", pixels_per_unit_x, pixels_per_unit_y, unit)
        return self._sign(_CHUNK_TYPE.pHYs, data)

    def tIME(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        data = struct.pack(">HBBBBB", year, month, day, hour, minute, second)
        return self._sign(_CHUNK_TYPE.tIME, data)

    def sBIT(self, significant_bits: list[int]):
        data = b""
        for bit in significant_bits:
            data += struct.pack(">B", bit)
        return self._sign(_CHUNK_TYPE.sBIT, data)


def create_png(
    width: int,
    height: int,
    image_data: list[bytes],
    chunk_size: int = 16384,
    apng: bool = False,
    num_frames: int = -1,
    delay_num: int = 1,
    delay_den: int = 30,
    loop_times: int = 1,
    bit_depth: int = 8,
    color_type: _PNG_COLOR_TYPE = _PNG_COLOR_TYPE.RGB32,
    compression_level: _ZLIB_COMPRESSION_LEVEL | int = _ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9,
):
    if apng and num_frames == -1:
        num_frames = len(image_data)
    x = P1(compression_level)
    png_data: bytes = b""
    png_data += bytes(_PNG_SIGNATURE)
    png_data += x.IHDR(width, height, bit_depth, color_type)
    png_data += x.tEXt("Software", "SJH8130:png_encoder")
    if apng:
        png_data += x.acTL(num_frames, loop_times)
        if num_frames == -1:
            num_frames = len(image_data)
    for chunk in x.XDAT(image_data[0], width, height, bit_depth, color_type, chunk_size):
        png_data += chunk
    if apng and 0:
        png_data += x.fcTL(width, height, 0, 0, delay_num, delay_den)
    if apng:
        for idx in range(0, num_frames):
            png_data += x.fcTL(width, height, 0, 0, delay_num, delay_den)
            for chunk in x.XDAT(image_data[idx], width, height, bit_depth, color_type, chunk_size, True):
                png_data += chunk
    png_data += x.IEND()
    return png_data


def encode_tile_image_to_apng(path_in, path_out, tile_width, tile_height, chunk_size=1048576, frame_cont=-1, fps=30):
    logger.info(f"{path_in=},{path_out=}")
    image = Image.open(path_in).convert("RGBA")
    frames: list[bytes] = []
    fc = 0
    vertical_frames = image.height // tile_height
    horizontal_frames = image.width // tile_width
    for v in range(vertical_frames):
        for h in range(horizontal_frames):
            box = (h * tile_width, v * tile_height, (h + 1) * tile_width, (v + 1) * tile_height)
            tile = image.crop(box)
            tile.save(f"Z:\\{fc+1}.png")
            frame_data = tile.tobytes()
            frames.append(frame_data)
            fc += 1
            if fc == frame_cont:
                break
        if fc == frame_cont:
            break
    r = create_png(tile_width, tile_height, image_data=frames, chunk_size=chunk_size, apng=True, num_frames=fc, delay_num=1, delay_den=fps, loop_times=0, bit_depth=8, color_type=_PNG_COLOR_TYPE.RGB32, compression_level=_ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
    write(path_out, r)


def recompress_png(png_path, chunk_size=1048576, compression_level=_ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9):
    image = Image.open(png_path)
    log.debug(image)
    width, height = image.size
    match image.mode:
        case "1":
            color_type = _PNG_COLOR_TYPE.GRAY
            bit_depth = 1
        case "L;2":
            color_type = _PNG_COLOR_TYPE.GRAY
            bit_depth = 2
        case "L;4":
            color_type = _PNG_COLOR_TYPE.GRAY
            bit_depth = 4
        case "L":
            color_type = _PNG_COLOR_TYPE.GRAY
            bit_depth = 8
        case "I;16B":
            color_type = _PNG_COLOR_TYPE.GRAY
            bit_depth = 16
        case "P;1":
            color_type = _PNG_COLOR_TYPE.INDEXED_COLOR
            bit_depth = 1
        case "P;2":
            color_type = _PNG_COLOR_TYPE.INDEXED_COLOR
            bit_depth = 2
        case "P;4":
            color_type = _PNG_COLOR_TYPE.INDEXED_COLOR
            bit_depth = 4
        case "P":
            color_type = _PNG_COLOR_TYPE.INDEXED_COLOR
            bit_depth = 8
        case "LA":
            color_type = _PNG_COLOR_TYPE.GRAYSCALE_WITH_ALPHA
            bit_depth = 16
        case "LA;16B":
            color_type = _PNG_COLOR_TYPE.GRAYSCALE_WITH_ALPHA
            bit_depth = 32
        case "RGB":
            color_type = _PNG_COLOR_TYPE.TRUECOLOR
            bit_depth = 24
        case "RGB;16B":
            color_type = _PNG_COLOR_TYPE.TRUECOLOR
            bit_depth = 48
        case "RGBA":
            color_type = _PNG_COLOR_TYPE.TRUECOLOR_WITH_ALPHA
            bit_depth = 32
        case "RGBA;16B":
            color_type = _PNG_COLOR_TYPE.TRUECOLOR_WITH_ALPHA
            bit_depth = 64
        case _:
            color_type = -1
            bit_depth = -1
            raise
    r = create_png(width, height, image_data=[image.tobytes()], chunk_size=chunk_size, apng=False, num_frames=1, delay_num=1, delay_den=1, loop_times=1, bit_depth=bit_depth, color_type=color_type, compression_level=compression_level)
    write(png_path, r)


def write(path, data):
    if not (isinstance(data, (bytes, str))):
        raise TypeError
    if isinstance(data, str):
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(data)
        return
    with open(path, "wb") as fp:
        fp.write(data)


if __name__ == "__main__":
    for p_in in xx:
        pb = os.path.basename(p_in)
        encode_tile_image_to_apng(p_in, os.path.join(po, "A_" + pb), tile_width=256, tile_height=256, frame_cont=120, fps=30)
    # os.system("ffmpeg -r 30 -i Z:\\%d.png -compression_level 9 -plays 0 Z:\\2.apng")
    # for img in sys.argv[1:]:
    #     recompress_png(img, chunk_size=1048576, compression_level=9)
