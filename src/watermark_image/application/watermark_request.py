"""@file watermark_request.py
@brief Data transfer object: what the user chose for a watermark.
"""

from dataclasses import dataclass
from pathlib import Path

from watermark_image import constants
from watermark_image.domain.anchor import Anchor


@dataclass(frozen=True, slots=True, kw_only=True)
class WatermarkRequest:
    """@brief The text or logo choices, the place and the opacity."""

    text: str
    font_size: int
    colour: str
    logo_source: Path | None = None
    logo_scale_percent: int = constants.DEFAULT_LOGO_SCALE
    anchor: Anchor
    opacity: int
