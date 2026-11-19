"""@file image.py
@brief The Image value object: a loaded picture in memory.
"""

from dataclasses import dataclass
from pathlib import Path

from watermark_image import constants
from watermark_image.domain.errors import DomainError


@dataclass(frozen=True, slots=True)
class Image:
    """@brief A loaded picture: its source file, size and RGBA pixels."""

    source: Path
    width: int
    height: int
    pixels: bytes

    def __post_init__(self) -> None:
        """@brief Refuse a size below 1 or pixels that do not fill the size."""
        if self.width < 1 or self.height < 1:
            raise DomainError("An image needs a width and a height of at least 1")
        expected = self.width * self.height * constants.BYTES_PER_PIXEL
        if len(self.pixels) != expected:
            raise DomainError(
                f"Pixels hold {len(self.pixels)} bytes, expected {expected}"
            )

    def is_source(self, target: Path) -> bool:
        """@brief Tell whether the target names the file this image came from.

        @param target The file name to compare with the source.
        @return True when both paths point to the same file.
        """
        return self.source.resolve() == target.resolve()
