"""@file add_watermark.py
@brief Use case: add a watermark to the current picture.
"""

from watermark_image import constants
from watermark_image.application.errors import NoImageError
from watermark_image.application.image_reader import ImageReader
from watermark_image.application.image_view import ImageView
from watermark_image.application.watermark_renderer import WatermarkRenderer
from watermark_image.application.watermark_request import WatermarkRequest
from watermark_image.application.workspace import Workspace
from watermark_image.domain.logo_watermark import LogoWatermark
from watermark_image.domain.position import Position
from watermark_image.domain.text_watermark import TextWatermark
from watermark_image.domain.watermark import Watermark


class AddWatermark:
    """@brief Draws a text or logo watermark on the current Image, unchanged."""

    def __init__(
        self, reader: ImageReader, renderer: WatermarkRenderer, workspace: Workspace
    ) -> None:
        """@brief Build the use case.

        @param reader The port that reads the logo file.
        @param renderer The port that draws the watermark.
        @param workspace The holder of the current Image and WatermarkedImage.
        """
        self._reader = reader
        self._renderer = renderer
        self._workspace = workspace

    def execute(self, request: WatermarkRequest) -> ImageView:
        """@brief Draw the watermark and keep the result as the marked picture.

        @param request What the user chose.
        @return The watermarked picture to show.
        @throws NoImageError when no Image is loaded.
        @throws InvalidWatermarkError when a value of the request is refused.
        @throws ImageReadError when the logo file is not a readable picture.
        In every case nothing changes.
        """
        image = self._workspace.current_image()
        if image is None:
            raise NoImageError(constants.ERROR_NO_IMAGE)
        watermark = self._build_watermark(request)
        position = Position(request.anchor, constants.DEFAULT_MARGIN)
        marked = self._renderer.render(image, watermark, position)
        self._workspace.replace_marked(marked)
        return ImageView(marked.width, marked.height, marked.pixels)

    def _build_watermark(self, request: WatermarkRequest) -> Watermark:
        if request.logo_source is not None:
            return LogoWatermark(
                opacity=request.opacity,
                logo=self._reader.read(request.logo_source),
                scale_percent=request.logo_scale_percent,
            )
        return TextWatermark(
            opacity=request.opacity,
            text=request.text,
            font_size=request.font_size,
            colour=request.colour,
        )
