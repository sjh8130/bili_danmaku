import math
import os
import struct
import sys
import zlib

from PIL import Image

# PNG signature
PNG_SIGNATURE = b"\x89PNG\x0d\x0a\x1a\x0a"
BRD_CHECK_S32 = 2**32 - 1
BRD_CHECK_S16 = 2**16 - 1
BRD_CHECK_S8 = 2**8 - 1
IEND = b"\x00\x00\x00\x00IEND\xae\x42\x60\x82"
NULL_SEPARATOR = b"\x00"
# IEND =  sign_chunk(b"IEND", b"")


class PNG_COLOR_TYPE(enumerate):
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


ALLOWED_DEPTH_LIST = {
    PNG_COLOR_TYPE.GRAY: [1, 2, 4, 8, 16],
    PNG_COLOR_TYPE.TRUECOLOR: [8, 16],
    PNG_COLOR_TYPE.INDEXED_COLOR: [1, 2, 4, 8, 16],
    PNG_COLOR_TYPE.GRAY_ALPHA: [8, 16],
    PNG_COLOR_TYPE.TRUECOLOR_WITH_ALPHA: [8, 16],
}


class APNG_DISPOSE_OP(enumerate):
    APNG_DISPOSE_OP_NONE = 0
    APNG_DISPOSE_OP_BACKGROUND = 1
    APNG_DISPOSE_OP_PREVIOUS = 2


class APNG_BLEND_OP(enumerate):
    APNG_BLEND_OP_SOURCE = 0
    APNG_BLEND_OP_OVER = 1


class COMPRESSION_LEVEL(enumerate):
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


class SRGB_RENDERING_INTENT(enumerate):
    SRGB_RENDERING_INTENT_PERCEPTUAL = 0
    SRGB_RENDERING_INTENT_RELATIVE_COLORIMETRIC = 1
    SRGB_RENDERING_INTENT_SATURATION = 2
    SRGB_RENDERING_INTENT_ABSOLUTE_COLORIMETRIC = 3


class PHYS_UNIT(enumerate):
    PHYS_UNIT_UNKNOWN = 0
    PHYS_UNIT_METER = 1


CHUNK_TYPE = dict(
    # Critical chunks
    IHDR=b"IHDR",  # Image header
    PLTE=b"PLTE",  # color Palette
    IDAT=b"IDAT",  # Image data
    IEND=b"IEND",  # Image trailer
    tRNS=b"tRNS",  # Transparency
    # Color space information
    cHRM=b"cHRM",  # Primary chromaticities and white point
    gAMA=b"gAMA",  # Image gamma
    iCCP=b"iCCP",  # Embedded ICC profile
    sBIT=b"sBIT",  # Significant bits
    sRGB=b"sRGB",  # Standard RGB color space
    cICP=b"cICP",  # Coding-independent code points for video signal type identification
    mDCv=b"mDCv",  # Mastering Display Color Volume
    cLLi=b"cLLi",  # Content Light Level Information
    # Textual information
    iTXt=b"iTXt",
    tEXt=b"tEXt",
    zTXt=b"zTXt",
    # Miscellaneous information
    bKGD=b"bKGD",  # Background color
    hIST=b"hIST",
    pHYs=b"pHYs",
    sPLT=b"sPLT",
    eXIf=b"eXIf",
    # Time information
    tIME=b"tIME",
    # Animation information
    acTL=b"acTL",
    fcTL=b"fcTL",
    fdAT=b"fdAT",
)


def sign_chunk(chunk_type: bytes, data: bytes) -> bytes:
    chunk_length = struct.pack(">I", len(data))
    chunk_crc = struct.pack(">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF)
    return chunk_length + chunk_type + data + chunk_crc


def create_ihdr(
    width: int,
    height: int,
    bit_depth: int,
    color_type: int,
    compression_method: int = 0,
    filter_method: int = 0,
    interlace_method: int = 0,
):
    if bit_depth not in ALLOWED_DEPTH_LIST[color_type]:
        raise ValueError("Invalid bit depth for color type")
    if compression_method != 0:
        raise ValueError("Invalid compression method")
    if filter_method != 0:
        raise ValueError("Invalid filter method")
    if interlace_method != 0:
        raise ValueError("Invalid interlace method")
    if width > BRD_CHECK_S32 or height > BRD_CHECK_S32:
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
    return sign_chunk(b"IHDR", data)


def create_plte(palette: list[tuple[int, int, int]]):
    data = b""
    for color in palette:
        data += struct.pack(">BBB", color[0], color[1], color[2])
    return sign_chunk(b"PLTE", data)


def compress_ifdat(image_data: bytes, width: int, height: int, bit_depth: int, color_type: int, chunk_size: int, compression_level: int) -> list[bytes]:
    if width > BRD_CHECK_S32 or height > BRD_CHECK_S32:
        raise ValueError("Invalid image size")
    if width <= 0 or height <= 0:
        raise ValueError("Invalid image size")
    if bit_depth not in ALLOWED_DEPTH_LIST[color_type]:
        raise ValueError("Invalid bit depth for color type")
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Invalid compression level")
    xdat_datas = []

    compresser = zlib.compressobj(compression_level)
    if color_type == 0:
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
    elif color_type == 2:
        if bit_depth == 8:
            row_size = 3 * width
        elif bit_depth == 16:
            row_size = 6 * width
    elif color_type == 3:
        if bit_depth == 1:
            row_size = math.ceil(width / 8)
        elif bit_depth == 2:
            row_size = math.ceil(width / 4)
        elif bit_depth == 4:
            row_size = math.ceil(width / 2)
        elif bit_depth == 8:
            row_size = width
    elif color_type == 4:
        if bit_depth == 8:
            row_size = 2 * width
        elif bit_depth == 16:
            row_size = 4 * width
    elif color_type == 6:
        if bit_depth == 8:
            row_size = 4 * width
        elif bit_depth == 16:
            row_size = 8 * width
    else:
        row_size = -1
        raise
    filtered_data = bytearray()

    for y in range(height):
        row_start = y * row_size
        row_end = row_start + row_size
        row = image_data[row_start:row_end]

        filtered_data.append(0)
        filtered_data.extend(row)

    compressed_data = zlib.compress(filtered_data)
    compresser.flush()

    for i in range(0, len(compressed_data), chunk_size):
        chunk_data = compressed_data[i : i + chunk_size]
        xdat_datas.append(chunk_data)
    return xdat_datas


def create_trns(transparency: list[int]):
    data = b""
    for alpha in transparency:
        data += struct.pack(">B", alpha)
    return sign_chunk(b"tRNS", data)


def create_gama(gamma: float):
    data = struct.pack(">I", int(gamma * 100000))
    return sign_chunk(b"gAMA", data)


def create_iccp(profile_name: str, profile_data: bytes):
    data = profile_name.encode() + b"\x00" + profile_data
    return sign_chunk(b"iCCP", data)


def create_srgb(rendering_intent: SRGB_RENDERING_INTENT = SRGB_RENDERING_INTENT.SRGB_RENDERING_INTENT_PERCEPTUAL):
    data = struct.pack(">B", rendering_intent)
    return sign_chunk(b"sRGB", data)


def create_actl(num_frames: int, num_plays: int):
    if num_frames < 1 or num_frames > BRD_CHECK_S32:
        raise ValueError("Invalid number of frames")
    if num_plays < 0 or num_plays > BRD_CHECK_S16:
        raise ValueError("Invalid number of plays")

    data = struct.pack(">II", num_frames, num_plays)
    return sign_chunk(b"acTL", data)


def create_fctl(
    seq: int,
    width: int,
    height: int,
    x_offset: int,
    y_offset: int,
    delay_num: int = 1,
    delay_den: int = 30,
    dispose_op: int = 0,
    blend_op: int = 0,
):
    if width > BRD_CHECK_S32 or height > BRD_CHECK_S32:
        raise ValueError("Invalid image size")
    if width <= 0 or height <= 0:
        raise ValueError("Invalid image size")
    if delay_num <= 0 or delay_den <= 0:
        raise ValueError("Invalid delay")
    if seq < 0 or seq > BRD_CHECK_S16:
        raise ValueError("Invalid sequence number")
    if x_offset < 0 or x_offset > BRD_CHECK_S32:
        raise ValueError("Invalid x offset")
    if y_offset < 0 or y_offset > BRD_CHECK_S32:
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
    return sign_chunk(b"fcTL", data)


def create_text(keyword: str, text: str) -> bytes:
    data = keyword.encode() + NULL_SEPARATOR + text.encode()
    return sign_chunk(CHUNK_TYPE["tEXt"], data)


def create_ztxt(keyword: str, text: str) -> bytes:
    data = keyword.encode() + NULL_SEPARATOR + b"\x00" + zlib.compress(text.encode(), COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
    return sign_chunk(CHUNK_TYPE["zTXt"], data)


def cerate_itxt(keyword: str, text: str, language_tag: str = "", tramslated_keyword: str = "", compression_flag: bool = False) -> bytes:
    if compression_flag:
        text = zlib.compress(text.encode(), COMPRESSION_LEVEL.COMPRESSION_LEVEL_9)
        compression_method = 0
    else:
        compression_method = 1
    data = keyword.encode() + NULL_SEPARATOR + text.encode() + struct.pack(">?B", compression_flag, compression_method) + language_tag.encode() + NULL_SEPARATOR + tramslated_keyword.encode() + NULL_SEPARATOR + text.encode()
    return sign_chunk(CHUNK_TYPE["iTXt"], data)


def create_phys(pixels_per_unit_x: int, pixels_per_unit_y: int, unit: PHYS_UNIT = 1):
    data = struct.pack(">IIB", pixels_per_unit_x, pixels_per_unit_y, unit)
    return sign_chunk(b"pHYs", data)


def create_time(year: int, month: int, day: int, hour: int, minute: int, second: int):
    data = struct.pack(">HBBBBB", year, month, day, hour, minute, second)
    return sign_chunk(b"tIME", data)


def create_sbit(significant_bits: list[int]):
    data = b""
    for bit in significant_bits:
        data += struct.pack(">B", bit)
    return sign_chunk(b"sBIT", data)


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
    color_type: int = PNG_COLOR_TYPE.RGB32,
    compression_level: int = COMPRESSION_LEVEL.COMPRESSION_LEVEL_9,
):
    if width > BRD_CHECK_S32 or height > BRD_CHECK_S32:
        raise ValueError("Invalid image size")
    if width <= 0 or height <= 0:
        raise ValueError("Invalid image size")
    if bit_depth not in ALLOWED_DEPTH_LIST[color_type]:
        raise ValueError("Invalid bit depth for color type")
    if compression_level < 0 or compression_level > 9:
        raise ValueError("Invalid compression level")
    if apng and num_frames == -1:
        num_frames = len(image_data)
    if apng and num_frames != len(image_data):
        raise ValueError("Invalid number of frames")
    if apng and delay_num <= 0 or delay_den <= 0:
        raise ValueError("Invalid delay")
    if apng and loop_times < 0 or loop_times > BRD_CHECK_S16:
        raise ValueError("Invalid loop times")

    png_data: bytes = b""
    png_data += bytes(PNG_SIGNATURE)
    png_data += create_ihdr(width, height, bit_depth, color_type)
    png_data += create_text("Software", "SJH8130:png_encoder")
    if apng:
        png_data += create_actl(num_frames, loop_times)
        if num_frames == -1:
            num_frames = len(image_data)

    idat_chunks = compress_ifdat(image_data[0], width, height, bit_depth, color_type, chunk_size, compression_level)
    for chunk in idat_chunks:
        png_data += sign_chunk(CHUNK_TYPE["IDAT"], chunk)
    del idat_chunks

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

            fdat_chunks = compress_ifdat(image_data[idx], width, height, bit_depth, color_type, chunk_size, compression_level)
            for chunk in fdat_chunks:
                png_data += sign_chunk(b"fdAT", struct.pack(">I", seq_num) + chunk)
                seq_num += 1

    png_data += IEND

    return png_data


def encode_tile_image_to_apng(tile_image_path, tile_width, tile_height, chunk_size=1048576, frame_cont=-1, fps=30):
    print(tile_image_path)
    image = Image.open(tile_image_path).convert("RGB")

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

    return create_png(tile_width, tile_height, image_data=frames, chunk_size=chunk_size, apng=True, num_frames=fc, delay_num=1, delay_den=fps, loop_times=0, bit_depth=8, color_type=PNG_COLOR_TYPE.RGB24, compression_level=9)


def recompress_png(png_path, chunk_size=1048576, compression_level=9):
    image = Image.open(png_path)
    width, height = image.size
    bit_depth = image.mode.count("1") * 1 + image.mode.count("L") * 8 + image.mode.count("P") * 8 + image.mode.count("RGB") * 8 + image.mode.count("RGBA") * 8
    match image.mode:
        case "1" | "P":
            color_type = PNG_COLOR_TYPE.INDEXED_COLOR
            color_type = PNG_COLOR_TYPE.INDEXED_COLOR
        case "L":
            color_type = PNG_COLOR_TYPE.GRAY
        case "LA":
            color_type = PNG_COLOR_TYPE.GREYSCALE_WITH_ALPHA
        case "RGB":
            color_type = PNG_COLOR_TYPE.TRUECOLOR
        case "RGBA":
            color_type = PNG_COLOR_TYPE.TRUECOLOR_WITH_ALPHA
        case _:
            color_type = -1
            raise
    image_data = image.tobytes()
    compressed_data = create_png(width, height, image_data=[image_data], chunk_size=chunk_size, apng=False, num_frames=1, delay_num=1, delay_den=1, loop_times=1, bit_depth=bit_depth, color_type=color_type, compression_level=compression_level)
    open(png_path, "wb").write(compressed_data)


if __name__ == "__main__":
    po = "Z:\\"
    xx = [
    ]
    for p in xx:
        pb = os.path.basename(p)
        open(f"{po}A_{pb}", "wb").write(encode_tile_image_to_apng(p, tile_width=256, tile_height=256, frame_cont=120, fps=30))
    # os.system("ffmpeg -r 30 -i Z:\\%d.png -compression_level 9 -plays 0 Z:\\2.apng")
    # for img in sys.argv[1:]:
    #     recompress_png(img, chunk_size=1048576, compression_level=9)
