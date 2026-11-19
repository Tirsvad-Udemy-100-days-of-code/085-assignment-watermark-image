"""@file composition.py
@brief The composition root: the one place that builds the adapters.
"""

from watermark_image.application.add_watermark import AddWatermark
from watermark_image.application.upload_image import UploadImage
from watermark_image.application.workspace import Workspace
from watermark_image.infrastructure.pillow_image_reader import PillowImageReader
from watermark_image.infrastructure.pillow_watermark_renderer import (
    PillowWatermarkRenderer,
)
from watermark_image.presentation.main_view_model import MainViewModel


class CompositionRoot:
    """@brief Joins the ports to their adapters and builds the view model."""

    def build_view_model(self) -> MainViewModel:
        """@brief Build the view model with every object it needs.

        @return A view model ready for the window.
        """
        workspace = Workspace()
        upload = UploadImage(PillowImageReader(), workspace)
        add = AddWatermark(PillowWatermarkRenderer(), workspace)
        return MainViewModel(upload, add)
