"""@file fakes.py
@brief Test doubles and builders shared by the unit tests.
"""

from pathlib import Path

from watermark_image import constants
from watermark_image.domain.image import Image


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
