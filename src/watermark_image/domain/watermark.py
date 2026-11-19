"""@file watermark.py
@brief The Watermark base value object: what every kind of watermark shares.
"""

from abc import ABC
from dataclasses import dataclass

from watermark_image import constants
from watermark_image.domain.errors import InvalidWatermarkError


@dataclass(frozen=True, slots=True)
class Watermark(ABC):
    """@brief The opacity shared by every watermark, in percent."""

    opacity: int

    def __post_init__(self) -> None:
        """@brief Refuse an opacity outside the limits, or a bare Watermark."""
        if type(self) is Watermark:
            raise TypeError("Watermark is abstract; use one of its kinds")
        if not constants.MIN_OPACITY <= self.opacity <= constants.MAX_OPACITY:
            raise InvalidWatermarkError(
                f"Opacity must be from {constants.MIN_OPACITY} "
                f"to {constants.MAX_OPACITY}"
            )
