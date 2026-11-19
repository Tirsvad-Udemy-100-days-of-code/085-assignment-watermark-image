"""@file image_writer.py
@brief Port: writes a watermarked picture to a file.
"""

from pathlib import Path
from typing import Protocol

from watermark_image.domain.watermarked_image import WatermarkedImage


class ImageWriter(Protocol):
    """@brief What the use cases need to store a picture in a file."""

    def write(self, marked: WatermarkedImage, target: Path) -> None:
        """@brief Write the picture to the target file.

        @param marked The picture to store; it is not modified.
        @param target The file to create; its ending chooses the format.
        @throws ImageWriteError when the ending is not supported or the file
            cannot be written.
        """
        ...
