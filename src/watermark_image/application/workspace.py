"""@file workspace.py
@brief Holder of the current Image and WatermarkedImage.
"""

from watermark_image.domain.image import Image
from watermark_image.domain.watermarked_image import WatermarkedImage


class Workspace:
    """@brief Keeps the Image the user is working on and its marked picture."""

    def __init__(self) -> None:
        """@brief Start with no Image and no WatermarkedImage."""
        self._image: Image | None = None
        self._marked: WatermarkedImage | None = None

    def current_image(self) -> Image | None:
        """@brief Give the current Image, or None before the first upload."""
        return self._image

    def current_marked(self) -> WatermarkedImage | None:
        """@brief Give the current WatermarkedImage, or None before one is made."""
        return self._marked

    def replace_image(self, image: Image) -> None:
        """@brief Make the given Image the current one and drop the marked one.

        @param image The new Image.
        """
        self._image = image
        self._marked = None

    def replace_marked(self, marked: WatermarkedImage) -> None:
        """@brief Make the given WatermarkedImage the current one.

        @param marked The new WatermarkedImage.
        """
        self._marked = marked
