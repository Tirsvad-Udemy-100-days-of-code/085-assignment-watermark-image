"""Tests of the PillowImageWriter against real files."""

from pathlib import Path

import pytest
from PIL import Image as PillowImage

from tests.unit.fakes import make_marked
from watermark_image import constants
from watermark_image.application.errors import ImageWriteError
from watermark_image.domain.watermarked_image import WatermarkedImage
from watermark_image.infrastructure.pillow_image_writer import PillowImageWriter

WIDTH = 8
HEIGHT = 6


def make_picture(pixels: bytes) -> WatermarkedImage:
    base = make_marked()
    return WatermarkedImage(
        base.image, base.watermark, base.position, WIDTH, HEIGHT, pixels
    )


def make_varied(alpha: int) -> WatermarkedImage:
    return make_picture(
        b"".join(
            bytes([x * 30, y * 40, 120, alpha])
            for y in range(HEIGHT)
            for x in range(WIDTH)
        )
    )


def make_flat(colour: tuple[int, int, int, int]) -> WatermarkedImage:
    return make_picture(bytes(colour) * (WIDTH * HEIGHT))


def read_rgba(path: Path) -> bytes:
    with PillowImage.open(path) as saved:
        return saved.convert(constants.PIXEL_MODE).tobytes()


def test_write_png_round_trips_every_pixel(tmp_path: Path) -> None:
    picture = make_varied(alpha=200)
    target = tmp_path / "out.png"
    PillowImageWriter().write(picture, target)
    assert read_rgba(target) == picture.pixels


@pytest.mark.parametrize("name", ["out.jpg", "out.JPEG"])
def test_write_jpeg_is_readable_and_close_in_colour(tmp_path: Path, name: str) -> None:
    target = tmp_path / name
    PillowImageWriter().write(make_flat((100, 150, 200, 255)), target)
    with PillowImage.open(target) as saved:
        assert saved.format == "JPEG"
    first = read_rgba(target)[:3]
    assert all(
        abs(got - want) < 8 for got, want in zip(first, (100, 150, 200), strict=True)
    )


def test_write_jpeg_lays_transparency_over_white(tmp_path: Path) -> None:
    target = tmp_path / "out.jpg"
    PillowImageWriter().write(make_flat((0, 0, 0, 0)), target)
    assert min(read_rgba(target)[:3]) > 245


def test_write_refuses_an_unsupported_ending(tmp_path: Path) -> None:
    target = tmp_path / "out.bmp"
    with pytest.raises(ImageWriteError):
        PillowImageWriter().write(make_varied(255), target)
    assert not target.exists()


def test_write_refuses_an_unwritable_folder(tmp_path: Path) -> None:
    target = tmp_path / "missing" / "out.png"
    with pytest.raises(ImageWriteError) as caught:
        PillowImageWriter().write(make_varied(255), target)
    assert isinstance(caught.value.__cause__, OSError)
