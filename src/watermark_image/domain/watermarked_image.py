"""@file watermarked_image.py
@brief The WatermarkedImage value object: the result of adding a watermark.
"""

from dataclasses import dataclass

from watermark_image.domain.image import Image, ensure_pixels_fit
from watermark_image.domain.position import Position
from watermark_image.domain.watermark import Watermark


@dataclass(frozen=True, slots=True)
class WatermarkedImage:
    """@brief A picture with a watermark, and what it was made from."""

    image: Image
    watermark: Watermark
    position: Position
    width: int
    height: int
    pixels: bytes

    def __post_init__(self) -> None:
        """@brief Refuse a size below 1 or pixels that do not fill the size."""
        ensure_pixels_fit(self.width, self.height, self.pixels)
