"""@file save_image.py
@brief Use case: save the watermarked picture to a file.
"""

from pathlib import Path

from watermark_image import constants
from watermark_image.application.confirmation import Confirmation
from watermark_image.application.errors import NoMarkedImageError
from watermark_image.application.image_writer import ImageWriter
from watermark_image.application.workspace import Workspace
from watermark_image.domain.errors import OverwriteOriginalError


class SaveImage:
    """@brief Stores the current WatermarkedImage, never over the original."""

    def __init__(self, writer: ImageWriter, workspace: Workspace) -> None:
        """@brief Build the use case.

        @param writer The port that writes the file.
        @param workspace The holder of the current Image and WatermarkedImage.
        """
        self._writer = writer
        self._workspace = workspace

    def execute(self, target: Path) -> Confirmation:
        """@brief Write the watermarked picture to the target file.

        @param target The file to create.
        @return A Confirmation holding the target.
        @throws NoMarkedImageError when no WatermarkedImage exists.
        @throws OverwriteOriginalError when the target is the file the Image
            came from.
        @throws ImageWriteError when the file cannot be written.
        In every case the Image and the WatermarkedImage stay as they were.
        """
        marked = self._workspace.current_marked()
        if marked is None:
            raise NoMarkedImageError(constants.ERROR_NO_MARKED_IMAGE)
        if marked.image.is_source(target):
            raise OverwriteOriginalError(constants.ERROR_OVERWRITE_ORIGINAL)
        self._writer.write(marked, target)
        return Confirmation(target)
