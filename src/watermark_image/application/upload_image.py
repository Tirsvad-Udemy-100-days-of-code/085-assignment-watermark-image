"""@file upload_image.py
@brief Use case: upload a picture.
"""

from pathlib import Path

from watermark_image.application.image_reader import ImageReader
from watermark_image.application.image_view import ImageView
from watermark_image.application.workspace import Workspace


class UploadImage:
    """@brief Loads a picture file and makes it the current Image."""

    def __init__(self, reader: ImageReader, workspace: Workspace) -> None:
        """@brief Build the use case.

        @param reader The port that reads the file.
        @param workspace The holder of the current Image.
        """
        self._reader = reader
        self._workspace = workspace

    def execute(self, source: Path) -> ImageView:
        """@brief Read the file and keep it as the current Image.

        @param source The picture file.
        @return The picture to show.
        @throws ImageReadError when the file is not a readable picture; the
            earlier Image stays as it was.
        """
        image = self._reader.read(source)
        self._workspace.replace_image(image)
        return ImageView(image.width, image.height, image.pixels)
