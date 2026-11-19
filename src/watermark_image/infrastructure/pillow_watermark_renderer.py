"""@file pillow_watermark_renderer.py
@brief Adapter: draws watermarks onto pictures with Pillow.
"""

from PIL import Image as PillowImage
from PIL import ImageColor, ImageDraw, ImageFont

from watermark_image import constants
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.errors import InvalidWatermarkError
from watermark_image.domain.image import Image
from watermark_image.domain.logo_watermark import LogoWatermark
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
    """@brief Implements the WatermarkRenderer port for text and logo watermarks."""

    def render(
        self, image: Image, watermark: Watermark, position: Position
    ) -> WatermarkedImage:
        """@brief Draw the mark on a transparent layer and blend it onto a copy.

        @param image The picture; it is never modified.
        @param watermark The text or logo watermark to draw.
        @param position Where to draw it.
        @return The new picture with the watermark.
        @throws InvalidWatermarkError when the watermark is neither a text nor
            a logo, or it cannot be drawn.
        """
        if not isinstance(watermark, TextWatermark | LogoWatermark):
            raise InvalidWatermarkError("Only a text or logo watermark can be drawn")
        try:
            size = (image.width, image.height)
            base = PillowImage.frombytes(constants.PIXEL_MODE, size, image.pixels)
            if isinstance(watermark, TextWatermark):
                layer = self._draw_text(size, watermark, position)
            else:
                layer = self._draw_logo(size, watermark, position)
            blended = PillowImage.alpha_composite(base, layer)
            pixels = blended.tobytes()
        except (OSError, ValueError, MemoryError) as error:
            raise InvalidWatermarkError("The watermark cannot be drawn") from error
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
        x, y = self._origin(size, (right - left, bottom - top), position)
        draw.text(
            (x - left, y - top),
            watermark.text,
            font=font,
            fill=(red, green, blue, _FULL_ALPHA),
        )
        return self._fade(layer, watermark.opacity)

    def _draw_logo(
        self, size: tuple[int, int], watermark: LogoWatermark, position: Position
    ) -> PillowImage.Image:
        logo = watermark.logo
        source = PillowImage.frombytes(
            constants.PIXEL_MODE, (logo.width, logo.height), logo.pixels
        )
        width = max(
            1, round(size[0] * watermark.scale_percent / constants.MAX_LOGO_SCALE)
        )
        height = max(1, round(logo.height * width / logo.width))
        scaled = self._fade(
            source.resize((width, height), PillowImage.Resampling.LANCZOS),
            watermark.opacity,
        )
        layer = PillowImage.new(constants.PIXEL_MODE, size, (0, 0, 0, 0))
        # Paste replaces the layer pixels, alpha included; the blend with the
        # picture happens once in render.
        layer.paste(scaled, self._origin(size, (width, height), position))
        return layer

    def _origin(
        self, size: tuple[int, int], extent: tuple[int, int], position: Position
    ) -> tuple[int, int]:
        """@brief Top left corner of a box of the given extent at the position."""
        anchor = position.anchor
        x = self._place(
            anchor in _LEFT, anchor in _RIGHT, size[0], extent[0], position.margin
        )
        y = self._place(
            anchor in _TOP, anchor in _BOTTOM, size[1], extent[1], position.margin
        )
        return x, y

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
