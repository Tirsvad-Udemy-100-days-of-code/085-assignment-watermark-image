"""@file pillow_image_writer.py
@brief Adapter: writes picture files with Pillow.
"""

from pathlib import Path

from PIL import Image as PillowImage

from watermark_image import constants
from watermark_image.application.errors import ImageWriteError
from watermark_image.domain.watermarked_image import WatermarkedImage

_JPEG_EXTENSIONS = (".jpg", ".jpeg")


class PillowImageWriter:
    """@brief Implements the ImageWriter port for JPEG and PNG files."""

    def write(self, marked: WatermarkedImage, target: Path) -> None:
        """@brief Write the picture in the format its file ending names.

        JPEG has no transparency, so the pixels are laid on a white background.

        @param marked The picture to store; it is not modified.
        @param target The file to create.
        @throws ImageWriteError when the ending is not supported or the file
            cannot be written.
        """
        extension = target.suffix.lower()
        if extension not in constants.SUPPORTED_WRITE_EXTENSIONS:
            raise ImageWriteError(constants.ERROR_UNSUPPORTED_ENDING)
        try:
            picture = PillowImage.frombytes(
                constants.PIXEL_MODE, (marked.width, marked.height), marked.pixels
            )
            if extension in _JPEG_EXTENSIONS:
                self._write_jpeg(picture, target)
            else:
                picture.save(target, format="PNG")
        except (OSError, ValueError) as error:
            raise ImageWriteError(constants.ERROR_NOT_WRITABLE) from error

    def _write_jpeg(self, picture: PillowImage.Image, target: Path) -> None:
        background = PillowImage.new(
            constants.PIXEL_MODE, picture.size, constants.JPEG_BACKGROUND
        )
        flat = PillowImage.alpha_composite(background, picture).convert("RGB")
        flat.save(target, format="JPEG", quality=constants.JPEG_QUALITY)
