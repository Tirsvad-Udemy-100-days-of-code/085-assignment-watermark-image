"""Tests of the UploadImage use case."""

from pathlib import Path

import pytest

from tests.unit.fakes import FakeImageReader, make_image
from watermark_image.application.errors import ImageReadError
from watermark_image.application.upload_image import UploadImage
from watermark_image.application.workspace import Workspace


def test_execute_returns_a_view_of_the_image() -> None:
    image = make_image(width=4, height=2)
    use_case = UploadImage(FakeImageReader(image), Workspace())
    view = use_case.execute(Path("photo.png"))
    assert (view.width, view.height, view.pixels) == (4, 2, image.pixels)


def test_execute_reads_the_given_file_and_keeps_the_image() -> None:
    image = make_image()
    reader = FakeImageReader(image)
    workspace = Workspace()
    UploadImage(reader, workspace).execute(Path("x.png"))
    assert reader.read_sources == [Path("x.png")]
    assert workspace.current_image() is image


def test_execute_keeps_the_earlier_image_when_reading_fails() -> None:
    workspace = Workspace()
    earlier = make_image("a.png")
    workspace.replace_image(earlier)
    failing = FakeImageReader(error=ImageReadError("Not a readable image"))
    with pytest.raises(ImageReadError):
        UploadImage(failing, workspace).execute(Path("bad.png"))
    assert workspace.current_image() is earlier
