"""@file add_watermark.py
@brief Use case: add a watermark to the current picture.
"""

from watermark_image import constants
from watermark_image.application.errors import NoImageError
from watermark_image.application.image_view import ImageView
from watermark_image.application.watermark_renderer import WatermarkRenderer
from watermark_image.application.watermark_request import WatermarkRequest
from watermark_image.application.workspace import Workspace
from watermark_image.domain.position import Position
from watermark_image.domain.text_watermark import TextWatermark


class AddWatermark:
    """@brief Draws a text watermark on the current Image, leaving it unchanged."""

    def __init__(self, renderer: WatermarkRenderer, workspace: Workspace) -> None:
        """@brief Build the use case.

        @param renderer The port that draws the watermark.
        @param workspace The holder of the current Image and WatermarkedImage.
        """
        self._renderer = renderer
        self._workspace = workspace

    def execute(self, request: WatermarkRequest) -> ImageView:
        """@brief Draw the watermark and keep the result as the marked picture.

        @param request What the user chose.
        @return The watermarked picture to show.
        @throws NoImageError when no Image is loaded.
        @throws InvalidWatermarkError when a value of the request is refused.
        In both cases nothing changes.
        """
        image = self._workspace.current_image()
        if image is None:
            raise NoImageError(constants.ERROR_NO_IMAGE)
        watermark = TextWatermark(
            opacity=request.opacity,
            text=request.text,
            font_size=request.font_size,
            colour=request.colour,
        )
        position = Position(request.anchor, constants.DEFAULT_MARGIN)
        marked = self._renderer.render(image, watermark, position)
        self._workspace.replace_marked(marked)
        return ImageView(marked.width, marked.height, marked.pixels)
