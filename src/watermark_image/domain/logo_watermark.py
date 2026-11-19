"""@file logo_watermark.py
@brief The LogoWatermark value object: a picture drawn on a picture.
"""

from dataclasses import dataclass

from watermark_image import constants
from watermark_image.domain.errors import InvalidWatermarkError
from watermark_image.domain.image import Image
from watermark_image.domain.watermark import Watermark


@dataclass(frozen=True, slots=True)
class LogoWatermark(Watermark):
    """@brief A logo Image and its size, besides the shared opacity."""

    logo: Image
    scale_percent: int

    def __post_init__(self) -> None:
        """@brief Refuse a scale outside the limits."""
        Watermark.__post_init__(self)
        if (
            not constants.MIN_LOGO_SCALE
            <= self.scale_percent
            <= constants.MAX_LOGO_SCALE
        ):
            raise InvalidWatermarkError(
                f"The logo scale must be from {constants.MIN_LOGO_SCALE} "
                f"to {constants.MAX_LOGO_SCALE} percent"
            )
