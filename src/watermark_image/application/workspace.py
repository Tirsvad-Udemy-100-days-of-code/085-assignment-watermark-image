"""@file workspace.py
@brief Holder of the current Image.
"""

from watermark_image.domain.image import Image


class Workspace:
    """@brief Keeps the Image the user is working on."""

    def __init__(self) -> None:
        """@brief Start with no Image."""
        self._image: Image | None = None

    def current_image(self) -> Image | None:
        """@brief Give the current Image, or None before the first upload."""
        return self._image

    def replace_image(self, image: Image) -> None:
        """@brief Make the given Image the current one.

        @param image The new Image.
        """
        self._image = image
