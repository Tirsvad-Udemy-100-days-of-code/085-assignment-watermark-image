"""Tests of the PreviewImage scaling (no window needed)."""

from watermark_image import constants
from watermark_image.application.image_view import ImageView
from watermark_image.presentation.preview_image import PreviewImage


def make_view(width: int, height: int) -> ImageView:
    return ImageView(width, height, bytes([1, 2, 3, 255]) * (width * height))


def test_large_picture_is_scaled_down_to_fit() -> None:
    max_width, max_height = constants.PREVIEW_MAX_SIZE
    scaled = PreviewImage().scale_to_fit(make_view(max_width * 2, max_height * 2))
    assert scaled.size == (max_width, max_height)


def test_wide_picture_keeps_its_shape() -> None:
    scaled = PreviewImage().scale_to_fit(make_view(1600, 400))
    assert scaled.size == (constants.PREVIEW_MAX_SIZE[0], 160)


def test_small_picture_is_not_enlarged() -> None:
    assert PreviewImage().scale_to_fit(make_view(10, 5)).size == (10, 5)


def test_scaled_picture_is_rgba() -> None:
    assert PreviewImage().scale_to_fit(make_view(2, 2)).mode == constants.PIXEL_MODE
