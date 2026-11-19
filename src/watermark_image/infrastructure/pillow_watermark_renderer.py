"""@file pillow_watermark_renderer.py
@brief Adapter: draws watermarks onto pictures with Pillow.
"""

from PIL import Image as PillowImage
from PIL import ImageColor, ImageDraw, ImageFont

from watermark_image import constants
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.errors import InvalidWatermarkError
from watermark_image.domain.image import Image
from watermark_image.domain.position import Position
from watermark_image.domain.text_watermark import TextWatermark
from watermark_image.domain.watermark import Watermark
from watermark_image.domain.watermarked_image import WatermarkedImage

_LEFT = (Anchor.TOP_LEFT, Anchor.MIDDLE_LEFT, Anchor.BOTTOM_LEFT)
_RIGHT = (Anchor.TOP_RIGHT, Anchor.MIDDLE_RIGHT, Anchor.BOTTOM_RIGHT)
_TOP = (Anchor.TOP_LEFT, Anchor.TOP_CENTER, Anchor.TOP_RIGHT)
_BOTTOM = (Anchor.BOTTOM_LEFT, Anchor.BOTTOM_CENTER, Anchor.BOTTOM_RIGHT)
_FULL_ALPHA = 255


class PillowWatermarkRenderer:
    """@brief Implements the WatermarkRenderer port for text watermarks."""

    def render(
        self, image: Image, watermark: Watermark, position: Position
    ) -> WatermarkedImage:
        """@brief Draw the text on a transparent layer and blend it onto a copy.

        @param image The picture; it is never modified.
        @param watermark The text watermark to draw.
        @param position Where to draw it.
        @return The new picture with the watermark.
        @throws InvalidWatermarkError when the watermark is not a text or the
            text cannot be drawn.
        """
        if not isinstance(watermark, TextWatermark):
            raise InvalidWatermarkError("Only a text watermark can be drawn")
        try:
            size = (image.width, image.height)
            base = PillowImage.frombytes(constants.PIXEL_MODE, size, image.pixels)
            layer = self._draw_text(size, watermark, position)
            blended = PillowImage.alpha_composite(base, layer)
            pixels = blended.tobytes()
        except (OSError, ValueError, MemoryError) as error:
            raise InvalidWatermarkError("The text cannot be drawn") from error
        return WatermarkedImage(
            image, watermark, position, image.width, image.height, pixels
        )

    def _draw_text(
        self, size: tuple[int, int], watermark: TextWatermark, position: Position
    ) -> PillowImage.Image:
        red, green, blue = ImageColor.getrgb(watermark.colour)[:3]
        # The layer starts in the text colour, so the soft edges keep that colour.
        layer = PillowImage.new(constants.PIXEL_MODE, size, (red, green, blue, 0))
        font = ImageFont.load_default(size=watermark.font_size)
        draw = ImageDraw.Draw(layer)
        left, top, right, bottom = (
            round(edge) for edge in draw.textbbox((0, 0), watermark.text, font=font)
        )
        x = self._place(
            position.anchor in _LEFT,
            position.anchor in _RIGHT,
            size[0],
            right - left,
            position.margin,
        )
        y = self._place(
            position.anchor in _TOP,
            position.anchor in _BOTTOM,
            size[1],
            bottom - top,
            position.margin,
        )
        draw.text(
            (x - left, y - top),
            watermark.text,
            font=font,
            fill=(red, green, blue, _FULL_ALPHA),
        )
        return self._fade(layer, watermark.opacity)

    def _place(
        self, at_start: bool, at_end: bool, room: int, extent: int, margin: int
    ) -> int:
        """@brief Offset of the text along one axis, kept inside the picture."""
        if at_start:
            offset = margin
        elif at_end:
            offset = room - margin - extent
        else:
            offset = (room - extent) // 2
        return max(0, min(offset, room - extent))

    def _fade(self, layer: PillowImage.Image, opacity: int) -> PillowImage.Image:
        """@brief Multiply the alpha of the layer by the opacity in percent."""
        table = [
            round(value * opacity / constants.MAX_OPACITY)
            for value in range(_FULL_ALPHA + 1)
        ]
        layer.putalpha(layer.getchannel("A").point(table))
        return layer
