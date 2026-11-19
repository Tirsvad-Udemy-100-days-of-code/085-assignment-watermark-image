"""@file main_view_model.py
@brief View model of the main window: what the window shows and its commands.
"""

from pathlib import Path

from watermark_image import constants
from watermark_image.application.add_watermark import AddWatermark
from watermark_image.application.errors import ImageReadError, NoImageError
from watermark_image.application.image_view import ImageView
from watermark_image.application.upload_image import UploadImage
from watermark_image.application.watermark_request import WatermarkRequest
from watermark_image.domain.errors import InvalidWatermarkError


class MainViewModel:
    """@brief Holds the state of the window and forwards its commands."""

    def __init__(self, upload: UploadImage, add: AddWatermark) -> None:
        """@brief Build the view model.

        @param upload The use case that uploads a picture.
        @param add The use case that adds a watermark.
        """
        self._upload = upload
        self._add = add
        self.has_watermark: bool = False
        self.status: str = constants.STATUS_EMPTY
        self.preview: ImageView | None = None

    @property
    def can_add(self) -> bool:
        """@brief True when a picture is loaded and a watermark can be added."""
        return self.preview is not None

    @property
    def can_save(self) -> bool:
        """@brief True when a watermarked picture exists; false until saving arrives."""
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
            self.has_watermark = False
            self.status = constants.STATUS_LOADED.format(name=source.name)

    def add_watermark(self, request: WatermarkRequest) -> None:
        """@brief Add a watermark; a refusal goes to the status line.

        @param request What the user chose; the preview and the earlier
            watermark stay as they were when it is refused.
        """
        try:
            self.preview = self._add.execute(request)
        except (InvalidWatermarkError, NoImageError) as error:
            self.status = str(error)
        else:
            self.has_watermark = True
            self.status = constants.STATUS_TEXT_ADDED
