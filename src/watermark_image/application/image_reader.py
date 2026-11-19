"""@file image_reader.py
@brief Port: reads a picture file into an Image.
"""

from pathlib import Path
from typing import Protocol

from watermark_image.domain.image import Image


class ImageReader(Protocol):
    """@brief What the use cases need to load a picture from a file."""

    def read(self, source: Path) -> Image:
        """@brief Read a picture file.

        @param source The picture file.
        @return The picture as an Image.
        @throws ImageReadError when the file is not a readable picture.
        """
        ...
