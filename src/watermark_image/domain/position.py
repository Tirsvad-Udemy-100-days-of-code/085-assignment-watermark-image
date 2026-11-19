"""@file position.py
@brief The Position value object: where a watermark sits on a picture.
"""

from dataclasses import dataclass

from watermark_image.domain.anchor import Anchor
from watermark_image.domain.errors import InvalidWatermarkError


@dataclass(frozen=True, slots=True)
class Position:
    """@brief An Anchor and the margin from the picture edge, in pixels."""

    anchor: Anchor
    margin: int

    def __post_init__(self) -> None:
        """@brief Refuse a negative margin."""
        if self.margin < 0:
            raise InvalidWatermarkError("The margin must not be negative")
