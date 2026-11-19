"""@file main_view_model.py
@brief View model of the main window: what the window shows and its commands.
"""

from pathlib import Path

from watermark_image import constants
from watermark_image.application.errors import ImageReadError
from watermark_image.application.image_view import ImageView
from watermark_image.application.upload_image import UploadImage


class MainViewModel:
    """@brief Holds the state of the window and forwards its commands."""

    def __init__(self, upload: UploadImage) -> None:
        """@brief Build the view model.

        @param upload The use case that uploads a picture.
        """
        self._upload = upload
        self.status: str = constants.STATUS_EMPTY
        self.preview: ImageView | None = None

    @property
    def can_add(self) -> bool:
        """@brief True when a picture is loaded and a watermark can be added."""
        return self.preview is not None

    @property
    def can_save(self) -> bool:
        """@brief True when a watermarked picture exists; false until step 2."""
        return False

    def upload_image(self, source: Path) -> None:
        """@brief Load a picture; a failure goes to the status line.

        @param source The picture file.
        """
        try:
            self.preview = self._upload.execute(source)
        except ImageReadError as error:
            self.status = str(error)
        else:
            self.status = constants.STATUS_LOADED.format(name=source.name)
