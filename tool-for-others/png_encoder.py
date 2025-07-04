import math
import struct
import time
import zlib
from enum import IntEnum, StrEnum
from pathlib import Path
from typing import NamedTuple

from PIL import Image
from tqdm import trange

try:
    from loguru import logger

    logger.bind(user="PNG")
except ImportError:
    import logging

    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("PNG")
try:
    import oxipng
except ImportError:
    oxipng = None

# PNG signature
_PNG_SIGNATURE = b"\x89PNG\x0d\x0a\x1a\x0a"
_BRD_S32 = 2**32 - 1
_BRD_S16 = 2**16 - 1
_BRD_S8 = 2**8 - 1
_NULL_SEPARATOR = b"\x00"


class ColorType(IntEnum):
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


_ALLOWED_DEPTH_LIST: dict[ColorType, list[int]] = {
    ColorType.GRAY: [1, 2, 4, 8, 16],
    ColorType.TRUECOLOR: [8, 16],
    ColorType.INDEXED_COLOR: [1, 2, 4, 8, 16],
    ColorType.GRAY_ALPHA: [8, 16],
    ColorType.TRUECOLOR_WITH_ALPHA: [8, 16],
}


class Disposal(IntEnum):
    OP_NONE = 0
    OP_BACKGROUND = 1
    OP_PREVIOUS = 2


class Blend(IntEnum):
    OP_SOURCE = 0
    OP_OVER = 1


class CompressionLevel(IntEnum):
    COPY = 0
    NONE = 0
    LV_0 = 0
    LV_1 = 1
    LV_2 = 2
    LV_3 = 3
    LV_4 = 4
    LV_5 = 5
    LV_6 = 6
    LV_7 = 7
    LV_8 = 8
    LV_9 = 9
    Z_BEST_SPEED = zlib.Z_BEST_SPEED
    Z_NO_COMPRESSION = zlib.Z_NO_COMPRESSION
    Z_BEST_COMPRESSION = zlib.Z_BEST_COMPRESSION
    X_OXIPNG = 233
    MAX = zlib.Z_BEST_COMPRESSION


class _SRGB_RENDERING_INTENT(IntEnum):
    SRGB_RENDERING_INTENT_PERCEPTUAL = 0
    SRGB_RENDERING_INTENT_RELATIVE_COLORIMETRIC = 1
    SRGB_RENDERING_INTENT_SATURATION = 2
    SRGB_RENDERING_INTENT_ABSOLUTE_COLORIMETRIC = 3


class _PHYS_UNIT(IntEnum):
    PHYS_UNIT_UNKNOWN = 0
    PHYS_UNIT_METER = 1


class _CHUNK_TYPE(StrEnum):
    """https://www.w3.org/TR/png-3/#11Chunks"""

    # Critical chunks
    IHDR = "IHDR"
    """Image header"""
    PLTE = "PLTE"
    """Palette"""
    IDAT = "IDAT"
    """Image data"""
    IEND = "IEND"
    """Image trailer"""
    # Ancillary chunks
    # # Transparency information
    tRNS = "tRNS"
    """Transparency"""
    # # Color space information
    cHRM = "cHRM"
    """Primary chromaticities and white point"""
    gAMA = "gAMA"
    """Image gamma"""
    iCCP = "iCCP"
    """Embedded ICC profile"""
    sBIT = "sBIT"
    """Significant bits"""
    sRGB = "sRGB"
    """Standard RGB color space"""
    cICP = "cICP"
    """Coding-independent code points for video signal type identification***"""
    mDCv = "mDCv"
    """Mastering Display Color Volume***"""
    cLLi = "cLLi"
    """Content Light Level Information***"""
    # # Textual information
    tEXt = "tEXt"
    """Textual data"""
    zTXt = "zTXt"
    """Compressed textual data"""
    iTXt = "iTXt"
    """International textual data"""
    # # Miscellaneous information
    bKGD = "bKGD"
    """Background color***"""
    hIST = "hIST"  # ***
    """Image histogram"""
    pHYs = "pHYs"
    """Physical pixel dimensions"""
    sPLT = "sPLT"  # ***
    """Suggested palette"""
    eXIf = "eXIf"  # ***
    """Exchangeable Image File (Exif) Profile"""
    # # Time information
    tIME = "tIME"
    """Image last-modification time"""
    # # Animation information
    acTL = "acTL"
    """Animation Control Chunk"""
    fcTL = "fcTL"
    """Frame Control Chunk"""
    fdAT = "fdAT"
    """Frame Data Chunk"""


class Palette(NamedTuple):
    r: int | bytes
    g: int | bytes
    b: int | bytes


class P1:
    compression_level = CompressionLevel.LV_9
    apng_seq = 0
    color_type: ColorType
    data: bytes = b""

    def __init__(self, compression_level: CompressionLevel) -> None:
        self.compression_level = CompressionLevel(compression_level)
        self.data += _PNG_SIGNATURE

    def _sign(self, chunk_type: bytes | str, data: bytes, /) -> bytes:
        if isinstance(chunk_type, str):
            chunk_type = chunk_type.encode("utf-8")
        chunk_length = len(data)
        chunk_crc = struct.pack(">I", zlib.crc32(chunk_type + data, 0) & 0xFFFFFFFF)
        # logger.debug(f"chunk_type={str(chunk_type, 'utf-8')}, {chunk_length=}")
        signed_data = struct.pack(">I", chunk_length) + chunk_type + data + chunk_crc
        self.data += signed_data
        return signed_data

    def IHDR(
        self,
        width: int,
        height: int,
        bit_depth: int,
        color_type: ColorType,
        compression_method: int = 0,
        filter_method: int = 0,
        interlace_method: int = 0,
    ) -> bytes:
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
        return self._sign(_CHUNK_TYPE.IHDR, data)

    def PLTE(self, palette: list[Palette]) -> bytes:
        if 0 >= len(palette) > 256:
            raise ValueError
        data = b""
        for color in palette:
            data += struct.pack(">BBB", color[0], color[1], color[2])
        return self._sign(_CHUNK_TYPE.PLTE, data)

    def XDAT(
        self,
        image_data: bytes,
        width: int,
        height: int,
        bit_depth: int,
        color_type: ColorType,
        chunk_size: int,
        *,
        apng: bool = False,
    ) -> None:
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
            raise ValueError
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
                self._sign(_CHUNK_TYPE.fdAT, struct.pack(">I", self.apng_seq) + chunk_data)
                self.apng_seq += 1
            else:
                self._sign(_CHUNK_TYPE.IDAT, chunk_data)

    def IEND(self) -> bytes:
        return self._sign(b"IEND", b"")

    def tRNS(self, transparency: list[int]) -> bytes:
        return self._sign(_CHUNK_TYPE.tRNS, bytes(bytearray(transparency)))

    def gAMA(self, gamma: float) -> bytes:
        data = struct.pack(">I", int(gamma * 100000))
        return self._sign(_CHUNK_TYPE.gAMA, data)

    def iCCP(self, profile_name: str, profile_data: bytes) -> bytes:
        data = profile_name.encode("utf-8") + _NULL_SEPARATOR + profile_data
        return self._sign(_CHUNK_TYPE.iCCP, data)

    def sRGB(
        self,
        rendering_intent: _SRGB_RENDERING_INTENT = _SRGB_RENDERING_INTENT.SRGB_RENDERING_INTENT_PERCEPTUAL,
    ) -> bytes:
        data = struct.pack(">B", rendering_intent)
        return self._sign(_CHUNK_TYPE.sRGB, data)

    def acTL(self, num_frames: int, num_plays: int) -> bytes:
        data = struct.pack(">II", num_frames, num_plays)
        return self._sign(_CHUNK_TYPE.acTL, data)

    def fcTL(
        self,
        width: int,
        height: int,
        x_offset: int,
        y_offset: int,
        delay_num: int = 1,
        delay_den: int = 30,
        dispose_op: Disposal = Disposal.OP_NONE,
        blend_op: Blend = Blend.OP_SOURCE,
    ) -> bytes:
        data = struct.pack(
            ">IiiiiHHBB",
            self.apng_seq,
            width,
            height,
            x_offset,
            y_offset,
            delay_num,
            delay_den,
            dispose_op,
            blend_op,
        )
        self.apng_seq += 1
        return self._sign(_CHUNK_TYPE.fcTL, data)

    def tEXt(self, keyword: str, text: str) -> bytes:
        data = keyword.encode("utf-8") + _NULL_SEPARATOR + text.encode("utf-8")
        return self._sign(_CHUNK_TYPE.tEXt, data)

    def zTXt(self, keyword: str, text: str) -> bytes:
        data = keyword.encode("utf-8") + _NULL_SEPARATOR * 2 + zlib.compress(text.encode("utf-8"), CompressionLevel.LV_9)
        return self._sign(_CHUNK_TYPE.zTXt, data)

    def iTXt(self, keyword: str, text: str, language_tag: str = "", translated_keyword: str = "", *, compression_flag: bool = False) -> bytes:
        t1 = text.encode("utf-8")
        if compression_flag:
            text_: bytes = zlib.compress(t1, CompressionLevel.LV_9)
            compression_method = 0
        else:
            text_ = t1
            compression_method = 1
        data = (
            keyword.encode("utf-8")
            + _NULL_SEPARATOR
            + text_
            + struct.pack(">?B", compression_flag, compression_method)
            + language_tag.encode("utf-8")
            + _NULL_SEPARATOR
            + translated_keyword.encode("utf-8")
            + _NULL_SEPARATOR
            + text.encode("utf-8")
        )
        return self._sign(_CHUNK_TYPE.iTXt, data)

    def pHYs(
        self,
        pixels_per_unit_x: int,
        pixels_per_unit_y: int,
        unit: _PHYS_UNIT = _PHYS_UNIT.PHYS_UNIT_METER,
    ) -> bytes:
        data = struct.pack(">IIB", pixels_per_unit_x, pixels_per_unit_y, unit)
        return self._sign(_CHUNK_TYPE.pHYs, data)

    def tIME(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> bytes:
        data = struct.pack(">HBBBBB", year, month, day, hour, minute, second)
        return self._sign(_CHUNK_TYPE.tIME, data)

    def sBIT(self, significant_bits: list[int]) -> bytes:
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
    color_type: ColorType = ColorType.RGB32,
    compression_level: CompressionLevel | int = CompressionLevel.LV_9,
) -> bytes:
    if apng and num_frames == -1:
        num_frames = len(image_data)
    x = P1(min(CompressionLevel(compression_level), CompressionLevel.LV_9 if oxipng is None else CompressionLevel.Z_BEST_SPEED))
    x.IHDR(width, height, bit_depth, color_type)
    x.tEXt("Software", "SJH8130:png_encoder")
    if apng:
        x.acTL(num_frames, loop_times)
        if num_frames == -1:
            num_frames = len(image_data)
    x.XDAT(image_data[0], width, height, bit_depth, color_type, chunk_size)
    if apng and False:
        x.fcTL(width, height, 0, 0, delay_num, delay_den)
    if apng:
        for idx in trange(0, num_frames):
            x.fcTL(width, height, 0, 0, delay_num, delay_den)
            x.XDAT(image_data[idx], width, height, bit_depth, color_type, chunk_size, apng=True)
    x.IEND()
    if oxipng is not None and compression_level == CompressionLevel.X_OXIPNG:
        before = len(x.data)
        png_data = oxipng.optimize_from_memory(
            x.data,
            level=6,
            optimize_alpha=True,
            bit_depth_reduction=False,
            color_type_reduction=False,
            deflate=oxipng.Deflaters.zopfli(255),
        )
        after = len(png_data)
        logger.info(f"{before:,} -> {after:,} {(after / before):.2f}%")
        return png_data
    return x.data


def encode_tile_image_to_apng(
    path_in,
    path_out,
    tile_width,
    tile_height,
    chunk_size=1048576,
    frame_cont=-1,
    fps=30,
    *,
    remove_alpha=False,
) -> None:
    if path_in == path_out:
        raise Exception(f"{path_in}=={path_out}::{path_in=}{path_out=}")
    logger.info(f"{path_in=},{path_out=}")
    image: Image.Image = Image.open(path_in).convert("RGB" if remove_alpha else "RGBA")
    frames: list[bytes] = []
    fc = 0
    vertical_frames: int = image.height // tile_height
    horizontal_frames: int = image.width // tile_width
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
    r = create_png(
        tile_width,
        tile_height,
        image_data=frames,
        chunk_size=chunk_size,
        apng=True,
        num_frames=fc,
        delay_num=1,
        delay_den=fps,
        loop_times=0,
        bit_depth=8,
        color_type=ColorType.RGB24 if remove_alpha else ColorType.RGBA32,
        compression_level=CompressionLevel.MAX,
    )
    write(path_out, r)


def recompress_png(png_path: Path, chunk_size=1048576, compression_level=CompressionLevel.LV_9) -> None:
    image = Image.open(png_path)
    logger.debug(image)
    width, height = image.size
    match image.mode:
        case "1":
            color_type = ColorType.GRAY
            bit_depth = 1
        case "L;2":
            color_type = ColorType.GRAY
            bit_depth = 2
        case "L;4":
            color_type = ColorType.GRAY
            bit_depth = 4
        case "L":
            color_type = ColorType.GRAY
            bit_depth = 8
        case "I;16B":
            color_type = ColorType.GRAY
            bit_depth = 16
        case "P;1":
            color_type = ColorType.INDEXED_COLOR
            bit_depth = 1
        case "P;2":
            color_type = ColorType.INDEXED_COLOR
            bit_depth = 2
        case "P;4":
            color_type = ColorType.INDEXED_COLOR
            bit_depth = 4
        case "P":
            color_type = ColorType.INDEXED_COLOR
            bit_depth = 8
        case "LA":
            color_type = ColorType.GRAYSCALE_WITH_ALPHA
            bit_depth = 16
        case "LA;16B":
            color_type = ColorType.GRAYSCALE_WITH_ALPHA
            bit_depth = 32
        case "RGB":
            color_type = ColorType.TRUECOLOR
            bit_depth = 24
        case "RGB;16B":
            color_type = ColorType.TRUECOLOR
            bit_depth = 48
        case "RGBA":
            color_type = ColorType.TRUECOLOR_WITH_ALPHA
            bit_depth = 32
        case "RGBA;16B":
            color_type = ColorType.TRUECOLOR_WITH_ALPHA
            bit_depth = 64
        case _:
            color_type = -1
            bit_depth = -1
            raise
    r = create_png(
        width,
        height,
        image_data=[image.tobytes()],
        chunk_size=chunk_size,
        apng=False,
        num_frames=1,
        delay_num=1,
        delay_den=1,
        loop_times=1,
        bit_depth=bit_depth,
        color_type=color_type,
        compression_level=compression_level,
    )
    write(png_path, r)


def write(path: Path, data) -> None:
    if not (isinstance(data, (bytes, str))):
        raise TypeError
    if isinstance(data, str):
        with path.open("w", encoding="utf-8") as fp:
            fp.write(data)
        return
    with path.open("wb") as fp:
        fp.write(data)


if __name__ == "__main__":
    try:
        encode_tile_image_to_apng(
            Path(),
            Path(),
            256,
            256,
            frame_cont=120,
            remove_alpha=False,
        )
    except KeyboardInterrupt:
        print()
    except Exception as e:
        logger.exception(e)
    time.sleep(10)
