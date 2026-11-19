"""@file image_view.py
@brief Data transfer object: a picture the window can show.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ImageView:
    """@brief Width, height and RGBA pixels of a picture, free of domain types."""

    width: int
    height: int
    pixels: bytes
