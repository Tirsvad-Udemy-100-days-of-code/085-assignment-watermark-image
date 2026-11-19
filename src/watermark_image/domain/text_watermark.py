"""@file text_watermark.py
@brief The TextWatermark value object: words drawn on a picture.
"""

import re
from dataclasses import dataclass

from watermark_image import constants
from watermark_image.domain.errors import InvalidWatermarkError
from watermark_image.domain.watermark import Watermark

_HEX_COLOUR = re.compile(constants.HEX_COLOUR_PATTERN)


@dataclass(frozen=True, slots=True)
class TextWatermark(Watermark):
    """@brief A text with its size and colour, besides the shared opacity."""

    text: str
    font_size: int
    colour: str

    def __post_init__(self) -> None:
        """@brief Refuse empty text, a size below the minimum or a bad colour."""
        Watermark.__post_init__(self)
        if not self.text.strip():
            raise InvalidWatermarkError("The text must not be empty")
        if self.font_size < constants.MIN_FONT_SIZE:
            raise InvalidWatermarkError(
                f"The font size must be at least {constants.MIN_FONT_SIZE}"
            )
        if not _HEX_COLOUR.fullmatch(self.colour):
            raise InvalidWatermarkError("The colour must look like #rrggbb")
