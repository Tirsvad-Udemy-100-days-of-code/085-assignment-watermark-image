"""@file image.py
@brief The Image value object: a loaded picture in memory.
"""

from dataclasses import dataclass
from pathlib import Path

from watermark_image import constants
from watermark_image.domain.errors import DomainError


def ensure_pixels_fit(width: int, height: int, pixels: bytes) -> None:
    """@brief Refuse a size below 1 or pixels that do not fill the size.

    @param width Width in pixels.
    @param height Height in pixels.
    @param pixels RGBA bytes of the picture.
    @throws DomainError when the size or the number of bytes is wrong.
    """
    if width < 1 or height < 1:
        raise DomainError("An image needs a width and a height of at least 1")
    expected = width * height * constants.BYTES_PER_PIXEL
    if len(pixels) != expected:
        raise DomainError(f"Pixels hold {len(pixels)} bytes, expected {expected}")


@dataclass(frozen=True, slots=True)
class Image:
    """@brief A loaded picture: its source file, size and RGBA pixels."""

    source: Path
    width: int
    height: int
    pixels: bytes

    def __post_init__(self) -> None:
        """@brief Refuse a size below 1 or pixels that do not fill the size."""
        ensure_pixels_fit(self.width, self.height, self.pixels)

    def is_source(self, target: Path) -> bool:
        """@brief Tell whether the target names the file this image came from.

        @param target The file name to compare with the source.
        @return True when both paths point to the same file.
        """
        return self.source.resolve() == target.resolve()
