"""@file composition.py
@brief The composition root: the one place that builds the adapters.
"""

from watermark_image.application.add_watermark import AddWatermark
from watermark_image.application.save_image import SaveImage
from watermark_image.application.upload_image import UploadImage
from watermark_image.application.workspace import Workspace
from watermark_image.infrastructure.pillow_image_reader import PillowImageReader
from watermark_image.infrastructure.pillow_image_writer import PillowImageWriter
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
        reader = PillowImageReader()
        upload = UploadImage(reader, workspace)
        add = AddWatermark(reader, PillowWatermarkRenderer(), workspace)
        save = SaveImage(PillowImageWriter(), workspace)
        return MainViewModel(upload, add, save)
