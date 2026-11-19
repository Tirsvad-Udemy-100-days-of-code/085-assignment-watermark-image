"""@file anchor.py
@brief The Anchor enumeration: the nine places on a picture.
"""

from enum import Enum


class Anchor(Enum):
    """@brief The nine places a watermark can sit, in reading order."""

    TOP_LEFT = "top left"
    TOP_CENTER = "top centre"
    TOP_RIGHT = "top right"
    MIDDLE_LEFT = "middle left"
    CENTER = "centre"
    MIDDLE_RIGHT = "middle right"
    BOTTOM_LEFT = "bottom left"
    BOTTOM_CENTER = "bottom centre"
    BOTTOM_RIGHT = "bottom right"
