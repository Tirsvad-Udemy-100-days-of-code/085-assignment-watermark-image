"""Tests of Anchor, Position, TextWatermark and WatermarkedImage."""

import dataclasses
from pathlib import Path

import pytest

from tests.unit.fakes import make_image, make_text_watermark
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.errors import DomainError, InvalidWatermarkError
from watermark_image.domain.position import Position
from watermark_image.domain.watermark import Watermark
from watermark_image.domain.watermarked_image import WatermarkedImage


def test_anchor_has_nine_members() -> None:
    assert len(Anchor) == 9


def test_position_holds_its_values() -> None:
    position = Position(Anchor.TOP_LEFT, 16)
    assert (position.anchor, position.margin) == (Anchor.TOP_LEFT, 16)


def test_position_accepts_a_margin_of_zero() -> None:
    assert Position(Anchor.CENTER, 0).margin == 0


def test_position_refuses_a_negative_margin() -> None:
    with pytest.raises(InvalidWatermarkError):
        Position(Anchor.CENTER, -1)


def test_invalid_watermark_error_is_a_domain_error() -> None:
    assert issubclass(InvalidWatermarkError, DomainError)


def test_watermark_base_cannot_be_created() -> None:
    with pytest.raises(TypeError):
        Watermark(50)


def test_text_watermark_holds_its_values() -> None:
    mark = make_text_watermark("Hi", 20, "#a1B2c3", 70)
    assert (mark.text, mark.font_size, mark.colour, mark.opacity) == (
        "Hi",
        20,
        "#a1B2c3",
        70,
    )


def test_text_watermark_is_immutable() -> None:
    mark = make_text_watermark()
    with pytest.raises(dataclasses.FrozenInstanceError):
        mark.opacity = 5  # type: ignore[misc]


@pytest.mark.parametrize("opacity", [0, 1, 99, 100])
def test_text_watermark_accepts_opacity_inside_the_limits(opacity: int) -> None:
    assert make_text_watermark(opacity=opacity).opacity == opacity


@pytest.mark.parametrize("opacity", [-1, 101])
def test_text_watermark_refuses_opacity_outside_the_limits(opacity: int) -> None:
    with pytest.raises(InvalidWatermarkError):
        make_text_watermark(opacity=opacity)


@pytest.mark.parametrize("text", ["", " ", "   \t\n"])
def test_text_watermark_refuses_empty_or_blank_text(text: str) -> None:
    with pytest.raises(InvalidWatermarkError):
        make_text_watermark(text=text)


def test_text_watermark_accepts_unicode_text() -> None:
    assert make_text_watermark(text="Ægir ©").text == "Ægir ©"


@pytest.mark.parametrize("size", [1, 2, 500])
def test_text_watermark_accepts_a_size_of_one_or_more(size: int) -> None:
    assert make_text_watermark(font_size=size).font_size == size


@pytest.mark.parametrize("size", [0, -1])
def test_text_watermark_refuses_a_size_below_one(size: int) -> None:
    with pytest.raises(InvalidWatermarkError):
        make_text_watermark(font_size=size)


@pytest.mark.parametrize(
    "colour", ["", "ffffff", "#fff", "#fffffff", "#gggggg", "white", "#ffffff "]
)
def test_text_watermark_refuses_a_bad_colour(colour: str) -> None:
    with pytest.raises(InvalidWatermarkError):
        make_text_watermark(colour=colour)


def _marked(width: int, height: int, length: int) -> WatermarkedImage:
    return WatermarkedImage(
        make_image(),
        make_text_watermark(),
        Position(Anchor.CENTER, 0),
        width,
        height,
        bytes(length),
    )


def test_watermarked_image_holds_its_values() -> None:
    marked = _marked(2, 3, 24)
    assert (marked.width, marked.height, len(marked.pixels)) == (2, 3, 24)
    assert marked.image.source == Path("photo.png")


def test_watermarked_image_is_immutable() -> None:
    marked = _marked(2, 3, 24)
    with pytest.raises(dataclasses.FrozenInstanceError):
        marked.width = 5  # type: ignore[misc]


@pytest.mark.parametrize("length", [0, 23, 25])
def test_watermarked_image_refuses_pixels_that_do_not_fill_the_size(
    length: int,
) -> None:
    with pytest.raises(DomainError):
        _marked(2, 3, length)


@pytest.mark.parametrize(("width", "height"), [(0, 1), (1, 0), (-1, 1)])
def test_watermarked_image_refuses_a_size_below_one(width: int, height: int) -> None:
    with pytest.raises(DomainError):
        _marked(width, height, 0)


def test_smallest_watermarked_image_is_accepted() -> None:
    assert _marked(1, 1, 4).width == 1
