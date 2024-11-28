import logging
import math
import os
import struct
import sys
import zlib

from enum import IntEnum, StrEnum

from PIL import Image

# PNG signature
_PNG_SIGNATURE = b"\x89PNG\x0d\x0a\x1a\x0a"
_BRD_S32 = 2**32 - 1
_BRD_S16 = 2**16 - 1
_BRD_S8 = 2**8 - 1
_IEND = b"\x00\x00\x00\x00IEND\xae\x42\x60\x82"
# _IEND =  sign_chunk(b"IEND", b"")
_NULL_SEPARATOR = b"\x00"

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PNG_encoder")


class _PNG_COLOR_TYPE(IntEnum):
    GRAY = 0
    GREYSCALE = GRAY
    Greyscale = GRAY
    TRUECOLOR = 2
    RGB = TRUECOLOR
    RGB24 = TRUECOLOR
    RGB48 = TRUECOLOR
    Truecolor = TRUECOLOR
    INDEXED_COLOR = 3
    PALETTE = INDEXED_COLOR
    GREYSCALE_WITH_ALPHA = 4
    GRAY_A = GREYSCALE_WITH_ALPHA
    GRAY_ALPHA = GREYSCALE_WITH_ALPHA
    GREYSCALE_ALPHA = GREYSCALE_WITH_ALPHA
    Greyscale_with_alpha = GREYSCALE_WITH_ALPHA
    TRUECOLOR_WITH_ALPHA = 6
    RGBA = TRUECOLOR_WITH_ALPHA
    RGB32 = TRUECOLOR_WITH_ALPHA
    RGB64 = TRUECOLOR_WITH_ALPHA
    Truecolor_with_alpha = TRUECOLOR_WITH_ALPHA


_ALLOWED_DEPTH_LIST = {
    _PNG_COLOR_TYPE.GRAY: [1, 2, 4, 8, 16],
    _PNG_COLOR_TYPE.TRUECOLOR: [8, 16],
    _PNG_COLOR_TYPE.INDEXED_COLOR: [1, 2, 4, 8, 16],
    _PNG_COLOR_TYPE.GRAY_ALPHA: [8, 16],
    _PNG_COLOR_TYPE.TRUECOLOR_WITH_ALPHA: [8, 16],
}


class _APNG_DISPOSE_OP(IntEnum):
    APNG_DISPOSE_OP_NONE = 0
    APNG_DISPOSE_OP_BACKGROUND = 1
    APNG_DISPOSE_OP_PREVIOUS = 2


class _APNG_BLEND_OP(IntEnum):
    APNG_BLEND_OP_SOURCE = 0
    APNG_BLEND_OP_OVER = 1


class _ZLIB_COMPRESSION_LEVEL(IntEnum):
    COMPRESSION_LEVEL_NONE = 0
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
    cICP = "cICP"  # Coding-independent code points for video signal type identification
    mDCv = "mDCv"  # Mastering Display Color Volume
    cLLi = "cLLi"  # Content Light Level Information
    # Textual information
    iTXt = "iTXt"
    tEXt = "tEXt"
    zTXt = "zTXt"
    # Miscellaneous information
    bKGD = "bKGD"  # Background color
    hIST = "hIST"
    pHYs = "pHYs"
    sPLT = "sPLT"
    eXIf = "eXIf"
    # Time information
    tIME = "tIME"
    # Animation information
    acTL = "acTL"
    fcTL = "fcTL"
    fdAT = "fdAT"


def sign_chunk(chunk_type: bytes | str, data: bytes) -> bytes:
    if isinstance(chunk_type, str):
        chunk_type = chunk_type.encode()
    chunk_length = len(data)
    chunk_crc = struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
    logger.debug(f"chunk_type={str(chunk_type,'utf-8')}, {chunk_length=}")
    return struct.pack(">I", chunk_length) + chunk_type + data + chunk_crc


def create_ihdr(
    width: int,
    height: int,
    bit_depth: int,
    color_type: _PNG_COLOR_TYPE,
    compression_method: int = 0,
    filter_method: int = 0,
    interlace_method: int = 0,
):
    if bit_depth not in _ALLOWED_DEPTH_LIST[color_type]:
        raise ValueError("Invalid bit depth for color type")
    if compression_method != 0:
        raise ValueError("Invalid compression method")
    if filter_method != 0:
        raise ValueError("Invalid filter method")
    if interlace_method != 0:
        raise ValueError("Invalid interlace method")
    if width > _BRD_S32 or height > _BRD_S32:
        raise ValueError("Invalid image size")
    if width <= 0 or height <= 0:
        raise ValueError("Invalid image size")

    data = struct.pack(
        ">IIBBBBB",
        width,
        height,
        bit_depth,
        color_type,
        compression_method,
        filter_method,
        interlace_method,
    )
    return sign_chunk(_CHUNK_TYPE.IHDR, data)


def create_plte(palette: list[tuple[int, int, int]]):
    data = b""
    for color in palette:
        data += struct.pack(">BBB", color[0], color[1], color[2])
    return sign_chunk(_CHUNK_TYPE.PLTE, data)


def compress_xdat(image_data: bytes, width: int, height: int, bit_depth: int, color_type: _PNG_COLOR_TYPE, chunk_size: int, compression_level: _ZLIB_COMPRESSION_LEVEL | int, fdat: int = 0):
    if width > _BRD_S32 or height > _BRD_S32:
        raise ValueError("Invalid image size")
    if width <= 0 or height <= 0:
        raise ValueError("Invalid image size")
    if bit_depth not in _ALLOWED_DEPTH_LIST[color_type]:
        raise ValueError("Invalid bit depth for color type")
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Invalid compression level")

    compressor = zlib.compressobj(compression_level)
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
        if fdat:
            yield sign_chunk(_CHUNK_TYPE.fdAT, struct.pack(">I", fdat) + chunk_data)
        else:
            yield sign_chunk(_CHUNK_TYPE.IDAT, chunk_data)


def create_trns(transparency: list[int]):
    data = b""
    for alpha in transparency:
        data += struct.pack(">B", alpha)
    return sign_chunk(_CHUNK_TYPE.tRNS, data)


def create_gama(gamma: float):
    data = struct.pack(">I", int(gamma * 100000))
    return sign_chunk(_CHUNK_TYPE.gAMA, data)


def create_iccp(profile_name: str, profile_data: bytes):
    data = profile_name.encode() + b"\x00" + profile_data
    return sign_chunk(_CHUNK_TYPE.iCCP, data)


def create_srgb(rendering_intent: _SRGB_RENDERING_INTENT = _SRGB_RENDERING_INTENT.SRGB_RENDERING_INTENT_PERCEPTUAL):
    data = struct.pack(">B", rendering_intent)
    return sign_chunk(_CHUNK_TYPE.sRGB, data)


def create_actl(num_frames: int, num_plays: int):
    if num_frames < 1 or num_frames > _BRD_S32:
        raise ValueError("Invalid number of frames")
    if num_plays < 0 or num_plays > _BRD_S16:
        raise ValueError("Invalid number of plays")

    data = struct.pack(">II", num_frames, num_plays)
    return sign_chunk(_CHUNK_TYPE.acTL, data)


def create_fctl(
    seq: int,
    width: int,
    height: int,
    x_offset: int,
    y_offset: int,
    delay_num: int = 1,
    delay_den: int = 30,
    dispose_op: _APNG_DISPOSE_OP = _APNG_DISPOSE_OP.APNG_DISPOSE_OP_NONE,
    blend_op: _APNG_BLEND_OP = _APNG_BLEND_OP.APNG_BLEND_OP_SOURCE,
):
    if width > _BRD_S32 or height > _BRD_S32:
        raise ValueError("Invalid image size")
    if width <= 0 or height <= 0:
        raise ValueError("Invalid image size")
    if delay_num <= 0 or delay_den <= 0:
        raise ValueError("Invalid delay")
    if seq < 0 or seq > _BRD_S16:
        raise ValueError("Invalid sequence number")
    if x_offset < 0 or x_offset > _BRD_S32:
        raise ValueError("Invalid x offset")
    if y_offset < 0 or y_offset > _BRD_S32:
        raise ValueError("Invalid y offset")
    if dispose_op not in [0, 1, 2]:
        raise ValueError("Invalid dispose operation")
    if blend_op not in [0, 1]:
        raise ValueError("Invalid blend operation")
    data = struct.pack(
        ">IiiiiHHBB",
        seq,
        width,
        height,
        x_offset,
        y_offset,
        delay_num,
        delay_den,
        dispose_op,
        blend_op,
    )
    return sign_chunk(_CHUNK_TYPE.fcTL, data)


def create_text(keyword: str, text: str) -> bytes:
    data = keyword.encode() + _NULL_SEPARATOR + text.encode()
    return sign_chunk(_CHUNK_TYPE.tEXt, data)


def create_ztxt(keyword: str, text: str) -> bytes:
    data = keyword.encode() + _NULL_SEPARATOR + b"\x00" + zlib.compress(text.encode(), _ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
    return sign_chunk(_CHUNK_TYPE.zTXt, data)


def cerate_itxt(keyword: str, text: str, language_tag: str = "", translated_keyword: str = "", compression_flag: bool = False) -> bytes:
    t1 = text.encode()
    if compression_flag:
        _text: bytes = zlib.compress(t1, _ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
        compression_method = 0
    else:
        _text = t1
        compression_method = 1
    data = keyword.encode() + _NULL_SEPARATOR + _text + struct.pack(">?B", compression_flag, compression_method) + language_tag.encode() + _NULL_SEPARATOR + translated_keyword.encode() + _NULL_SEPARATOR + text.encode()
    return sign_chunk(_CHUNK_TYPE.iTXt, data)


def create_phys(pixels_per_unit_x: int, pixels_per_unit_y: int, unit: _PHYS_UNIT = _PHYS_UNIT.PHYS_UNIT_METER):
    data = struct.pack(">IIB", pixels_per_unit_x, pixels_per_unit_y, unit)
    return sign_chunk(_CHUNK_TYPE.pHYs, data)


def create_time(year: int, month: int, day: int, hour: int, minute: int, second: int):
    data = struct.pack(">HBBBBB", year, month, day, hour, minute, second)
    return sign_chunk(_CHUNK_TYPE.tIME, data)


def create_sbit(significant_bits: list[int]):
    data = b""
    for bit in significant_bits:
        data += struct.pack(">B", bit)
    return sign_chunk(_CHUNK_TYPE.sBIT, data)


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
    if width > _BRD_S32 or height > _BRD_S32:
        raise ValueError("Invalid image size")
    if width <= 0 or height <= 0:
        raise ValueError("Invalid image size")
    if bit_depth not in _ALLOWED_DEPTH_LIST[color_type]:
        raise ValueError("Invalid bit depth for color type")
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Invalid compression level")
    if apng and num_frames == -1:
        num_frames = len(image_data)
    if apng and num_frames != len(image_data):
        raise ValueError("Invalid number of frames")
    if apng and delay_num <= 0 or delay_den <= 0:
        raise ValueError("Invalid delay")
    if apng and loop_times < 0 or loop_times > _BRD_S16:
        raise ValueError("Invalid loop times")

    png_data: bytes = b""
    png_data += bytes(_PNG_SIGNATURE)
    png_data += create_ihdr(width, height, bit_depth, color_type)
    png_data += create_text("Software", "SJH8130:png_encoder")
    if apng:
        png_data += create_actl(num_frames, loop_times)
        if num_frames == -1:
            num_frames = len(image_data)

    for chunk in compress_xdat(image_data[0], width, height, bit_depth, color_type, chunk_size, compression_level, 0):
        png_data += chunk

    seq_num = 0
    if apng and False:
        png_data += create_fctl(
            seq_num,
            width,
            height,
            0,
            0,
            delay_num,
            delay_den,
        )
        seq_num += 1

    if apng:
        for idx in range(0, num_frames):
            png_data += create_fctl(seq_num, width, height, 0, 0, delay_num, delay_den)
            seq_num += 1

            for chunk in compress_xdat(image_data[idx], width, height, bit_depth, color_type, chunk_size, compression_level, seq_num):
                png_data += chunk
                seq_num += 1

    png_data += _IEND

    return png_data


def encode_tile_image_to_apng(path_in, path_out, tile_width, tile_height, chunk_size=1048576, frame_cont=-1, fps=30):
    logger.info(f"{path_in=},{path_out=}")
    image = Image.open(path_in).convert("RGB")

    frames: list[bytes] = []
    fc = 0
    vertical_frames = image.height // tile_height
    horizontal_frames = image.width // tile_width

    for v in range(vertical_frames):
        for h in range(horizontal_frames):
            box = (h * tile_width, v * tile_height, (h + 1) * tile_width, (v + 1) * tile_height)
            tile = image.crop(box)
            # tile.save(f"Z:\\{fc+1}.png")
            frame_data = tile.tobytes()
            frames.append(frame_data)
            fc += 1
            if fc == frame_cont:
                break
        if fc == frame_cont:
            break

    r = create_png(tile_width, tile_height, image_data=frames, chunk_size=chunk_size, apng=True, num_frames=fc, delay_num=1, delay_den=fps, loop_times=0, bit_depth=8, color_type=_PNG_COLOR_TYPE.RGB24, compression_level=_ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
    write(path_out, r)


def recompress_png(png_path, chunk_size=1048576, compression_level=_ZLIB_COMPRESSION_LEVEL.COMPRESSION_LEVEL_9):
    image = Image.open(png_path)
    width, height = image.size
    bit_depth = image.mode.count("1") * 1 + image.mode.count("L") * 8 + image.mode.count("P") * 8 + image.mode.count("RGB") * 8 + image.mode.count("RGBA") * 8
    match image.mode:
        case "1" | "P":
            color_type = _PNG_COLOR_TYPE.INDEXED_COLOR
            color_type = _PNG_COLOR_TYPE.INDEXED_COLOR
        case "L":
            color_type = _PNG_COLOR_TYPE.GRAY
        case "LA":
            color_type = _PNG_COLOR_TYPE.GREYSCALE_WITH_ALPHA
        case "RGB":
            color_type = _PNG_COLOR_TYPE.TRUECOLOR
        case "RGBA":
            color_type = _PNG_COLOR_TYPE.TRUECOLOR_WITH_ALPHA
        case _:
            color_type = -1
            raise
    r = create_png(width, height, image_data=[image.tobytes()], chunk_size=chunk_size, apng=False, num_frames=1, delay_num=1, delay_den=1, loop_times=1, bit_depth=bit_depth, color_type=color_type, compression_level=compression_level)
    write(png_path, r)


def write(path, data):
    if not (isinstance(data, bytes) or isinstance(data, str)):
        raise TypeError
    if isinstance(data, str):
        with open(path, "w", encoding="utf-8") as fp:
            fp.write(data)
        return
    with open(path, "wb") as fp:
        fp.write(data)


if __name__ == "__main__":
    po = "Z:\\"
    xx = [
    ]
    for p_in in xx:
        pb = os.path.basename(p_in)
        encode_tile_image_to_apng(p_in, os.path.join(po, "A_" + pb), tile_width=256, tile_height=256, frame_cont=120, fps=30)
    # os.system("ffmpeg -r 30 -i Z:\\%d.png -compression_level 9 -plays 0 Z:\\2.apng")
    # for img in sys.argv[1:]:
    #     recompress_png(img, chunk_size=1048576, compression_level=9)
