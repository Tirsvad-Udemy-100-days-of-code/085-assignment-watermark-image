"""@file preview_image.py
@brief Helper: turns an ImageView into a picture the window can draw.
"""

from PIL import Image as PillowImage
from PIL import ImageTk

from watermark_image import constants
from watermark_image.application.image_view import ImageView


class PreviewImage:
    """@brief Scales a picture to fit the preview area."""

    def scale_to_fit(self, view: ImageView) -> PillowImage.Image:
        """@brief Scale a picture down to the preview size, keeping its shape.

        @param view The picture to scale; a small picture is not enlarged.
        @return The scaled picture.
        """
        picture = PillowImage.frombytes(
            constants.PIXEL_MODE, (view.width, view.height), view.pixels
        )
        picture.thumbnail(constants.PREVIEW_MAX_SIZE)
        return picture

    def to_photo_image(self, view: ImageView) -> ImageTk.PhotoImage:
        """@brief Make a picture Tkinter can draw, scaled to fit.

        @param view The picture to show.
        @return The scaled picture; needs a Tk root window to exist.
        """
        return ImageTk.PhotoImage(self.scale_to_fit(view))
