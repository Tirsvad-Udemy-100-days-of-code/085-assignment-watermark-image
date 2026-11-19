"""Tests of the shared constants."""

from watermark_image import constants
from watermark_image.domain.anchor import Anchor


def test_read_extensions_are_lower_case_with_a_dot() -> None:
    for extension in constants.SUPPORTED_READ_EXTENSIONS:
        assert extension.startswith(".")
        assert extension == extension.lower()


def test_write_extensions_are_a_subset_of_read_extensions() -> None:
    assert set(constants.SUPPORTED_WRITE_EXTENSIONS) <= set(
        constants.SUPPORTED_READ_EXTENSIONS
    )


def test_default_opacity_lies_between_the_limits() -> None:
    assert constants.MIN_OPACITY <= constants.DEFAULT_OPACITY <= constants.MAX_OPACITY


def test_default_logo_scale_lies_between_the_limits() -> None:
    assert (
        constants.MIN_LOGO_SCALE
        <= constants.DEFAULT_LOGO_SCALE
        <= constants.MAX_LOGO_SCALE
    )


def test_default_font_size_is_not_below_the_minimum() -> None:
    assert constants.DEFAULT_FONT_SIZE >= constants.MIN_FONT_SIZE


def test_there_is_one_place_caption_per_anchor() -> None:
    assert len(constants.PLACE_CAPTIONS) == len(Anchor)
    assert len(Anchor) == constants.PLACE_GRID_COLUMNS**2
