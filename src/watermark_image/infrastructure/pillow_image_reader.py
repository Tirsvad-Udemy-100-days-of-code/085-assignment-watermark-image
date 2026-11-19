"""@file pillow_image_reader.py
@brief Adapter: reads picture files with Pillow.
"""

from pathlib import Path

from PIL import Image as PillowImage

from watermark_image import constants
from watermark_image.application.errors import ImageReadError
from watermark_image.domain.errors import DomainError
from watermark_image.domain.image import Image


class PillowImageReader:
    """@brief Implements the ImageReader port for JPEG, PNG, BMP, GIF and WebP."""

    def read(self, source: Path) -> Image:
        """@brief Read a picture file and convert it to RGBA.

        @param source The picture file.
        @return The picture as an Image.
        @throws ImageReadError when the ending is not supported or the file
            cannot be opened or decoded.
        """
        if source.suffix.lower() not in constants.SUPPORTED_READ_EXTENSIONS:
            raise ImageReadError(constants.ERROR_NOT_READABLE)
        try:
            with PillowImage.open(source) as opened:
                rgba = opened.convert(constants.PIXEL_MODE)
            width, height = rgba.size
            return Image(source, width, height, rgba.tobytes())
        except (
            OSError,
            ValueError,
            PillowImage.DecompressionBombError,
            DomainError,
        ) as error:
            raise ImageReadError(constants.ERROR_NOT_READABLE) from error
