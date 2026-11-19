"""@file fakes.py
@brief Test doubles and builders shared by the unit tests.
"""

from pathlib import Path

from watermark_image import constants
from watermark_image.application.watermark_request import WatermarkRequest
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.image import Image
from watermark_image.domain.position import Position
from watermark_image.domain.text_watermark import TextWatermark
from watermark_image.domain.watermark import Watermark
from watermark_image.domain.watermarked_image import WatermarkedImage


def make_image(source: str = "photo.png", width: int = 2, height: int = 3) -> Image:
    """@brief Build a valid Image of one colour."""
    pixels = bytes([10, 20, 30, 255]) * (width * height)
    assert len(pixels) == width * height * constants.BYTES_PER_PIXEL
    return Image(Path(source), width, height, pixels)


class FakeImageReader:
    """@brief An ImageReader that returns a prepared Image or raises an error."""

    def __init__(
        self, image: Image | None = None, error: Exception | None = None
    ) -> None:
        self._image = image
        self._error = error
        self.read_sources: list[Path] = []

    def read(self, source: Path) -> Image:
        """@brief Record the call and return the prepared Image or raise."""
        self.read_sources.append(source)
        if self._error is not None:
            raise self._error
        assert self._image is not None
        return self._image


def make_text_watermark(
    text: str = "Mark", font_size: int = 12, colour: str = "#ffffff", opacity: int = 50
) -> TextWatermark:
    """@brief Build a valid TextWatermark."""
    return TextWatermark(opacity=opacity, text=text, font_size=font_size, colour=colour)


def make_request(
    text: str = "Mark",
    font_size: int = 12,
    colour: str = "#ffffff",
    anchor: Anchor = Anchor.CENTER,
    opacity: int = 50,
) -> WatermarkRequest:
    """@brief Build a WatermarkRequest for a text watermark."""
    return WatermarkRequest(
        text=text, font_size=font_size, colour=colour, anchor=anchor, opacity=opacity
    )


class FakeWatermarkRenderer:
    """@brief A WatermarkRenderer that marks the first pixel and records calls."""

    def __init__(self) -> None:
        self.calls: list[tuple[Image, Watermark, Position]] = []

    def render(
        self, image: Image, watermark: Watermark, position: Position
    ) -> WatermarkedImage:
        """@brief Record the call and return a copy with the first pixel white."""
        self.calls.append((image, watermark, position))
        pixels = bytes([255, 255, 255, 255]) + image.pixels[constants.BYTES_PER_PIXEL :]
        return WatermarkedImage(
            image, watermark, position, image.width, image.height, pixels
        )
