"""@file watermark_renderer.py
@brief Port: draws a watermark onto a picture.
"""

from typing import Protocol

from watermark_image.domain.image import Image
from watermark_image.domain.position import Position
from watermark_image.domain.watermark import Watermark
from watermark_image.domain.watermarked_image import WatermarkedImage


class WatermarkRenderer(Protocol):
    """@brief What the use cases need to put a watermark on a picture."""

    def render(
        self, image: Image, watermark: Watermark, position: Position
    ) -> WatermarkedImage:
        """@brief Draw the watermark on a copy of the picture.

        @param image The picture; it is never modified.
        @param watermark The text or logo to draw, with its opacity.
        @param position Where to draw it.
        @return The new picture with the watermark.
        @throws InvalidWatermarkError when the watermark cannot be drawn.
        """
        ...
