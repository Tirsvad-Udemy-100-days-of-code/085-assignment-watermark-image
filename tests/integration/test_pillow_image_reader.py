"""Tests of the PillowImageReader against real files."""

from pathlib import Path

import pytest
from PIL import Image as PillowImage

from watermark_image import constants
from watermark_image.application.errors import ImageReadError
from watermark_image.infrastructure.pillow_image_reader import PillowImageReader

FORMATS = [
    ("sample.png", "RGB"),
    ("sample.PNG", "RGBA"),
    ("sample.jpg", "RGB"),
    ("sample.jpeg", "RGB"),
    ("sample.bmp", "RGB"),
    ("sample.gif", "P"),
    ("sample.webp", "RGB"),
]


@pytest.mark.parametrize(("name", "mode"), FORMATS)
def test_read_loads_each_supported_format_as_rgba(
    tmp_path: Path, name: str, mode: str
) -> None:
    path = tmp_path / name
    PillowImage.new(mode, (7, 5)).save(path)
    image = PillowImageReader().read(path)
    assert (image.width, image.height) == (7, 5)
    assert len(image.pixels) == 7 * 5 * constants.BYTES_PER_PIXEL
    assert image.source == path


def test_read_keeps_the_colours(tmp_path: Path) -> None:
    path = tmp_path / "red.png"
    PillowImage.new("RGB", (2, 2), (200, 10, 20)).save(path)
    assert PillowImageReader().read(path).pixels[:4] == bytes([200, 10, 20, 255])


def test_read_refuses_a_corrupt_file_and_keeps_the_cause(tmp_path: Path) -> None:
    path = tmp_path / "broken.png"
    path.write_bytes(b"this is not a png")
    with pytest.raises(ImageReadError, match="Not a readable image") as caught:
        PillowImageReader().read(path)
    assert caught.value.__cause__ is not None


def test_read_refuses_a_missing_file(tmp_path: Path) -> None:
    with pytest.raises(ImageReadError) as caught:
        PillowImageReader().read(tmp_path / "missing.png")
    assert isinstance(caught.value.__cause__, OSError)


def test_read_refuses_an_unsupported_ending(tmp_path: Path) -> None:
    path = tmp_path / "notes.txt"
    path.write_text("hello")
    with pytest.raises(ImageReadError):
        PillowImageReader().read(path)
