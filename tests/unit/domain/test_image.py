"""Tests of the Image value object."""

import dataclasses
from pathlib import Path

import pytest

from tests.unit.fakes import make_image
from watermark_image.domain.errors import DomainError
from watermark_image.domain.image import Image


def test_image_holds_its_values() -> None:
    image = make_image(width=2, height=3)
    assert (image.width, image.height) == (2, 3)
    assert len(image.pixels) == 24


def test_image_is_immutable() -> None:
    image = make_image()
    with pytest.raises(dataclasses.FrozenInstanceError):
        image.width = 5  # type: ignore[misc]


@pytest.mark.parametrize("length", [0, 23, 25])
def test_image_refuses_pixels_that_do_not_fill_the_size(length: int) -> None:
    with pytest.raises(DomainError):
        Image(Path("a.png"), 2, 3, bytes(length))


@pytest.mark.parametrize(("width", "height"), [(0, 1), (1, 0), (-1, 1)])
def test_image_refuses_a_size_below_one(width: int, height: int) -> None:
    with pytest.raises(DomainError):
        Image(Path("a.png"), width, height, b"")


def test_smallest_image_is_accepted() -> None:
    assert Image(Path("a.png"), 1, 1, bytes(4)).width == 1


def test_is_source_true_for_the_same_file(tmp_path: Path) -> None:
    image = make_image(source=str(tmp_path / "a.png"))
    assert image.is_source(tmp_path / "sub" / ".." / "a.png")


def test_is_source_false_for_another_file(tmp_path: Path) -> None:
    image = make_image(source=str(tmp_path / "a.png"))
    assert not image.is_source(tmp_path / "b.png")
