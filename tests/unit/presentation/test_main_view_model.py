"""Tests of the MainViewModel (no window needed)."""

from pathlib import Path

from tests.unit.fakes import FakeImageReader, make_image
from watermark_image.application.errors import ImageReadError
from watermark_image.application.upload_image import UploadImage
from watermark_image.application.workspace import Workspace
from watermark_image.presentation.main_view_model import MainViewModel


def make_view_model(reader: FakeImageReader) -> MainViewModel:
    return MainViewModel(UploadImage(reader, Workspace()))


def test_new_view_model_is_empty() -> None:
    view_model = make_view_model(FakeImageReader(make_image()))
    assert view_model.status == "Upload an image to begin"
    assert view_model.preview is None
    assert not view_model.can_add
    assert not view_model.can_save


def test_upload_image_shows_the_picture_and_its_name() -> None:
    view_model = make_view_model(FakeImageReader(make_image(width=4, height=2)))
    view_model.upload_image(Path("dir") / "holiday.png")
    assert view_model.status == "Loaded holiday.png"
    assert view_model.preview is not None
    assert view_model.preview.width == 4
    assert view_model.can_add
    assert not view_model.can_save


def test_upload_image_shows_the_reason_when_reading_fails() -> None:
    reader = FakeImageReader(error=ImageReadError("Not a readable image"))
    view_model = make_view_model(reader)
    view_model.upload_image(Path("bad.png"))
    assert view_model.status == "Not a readable image"
    assert view_model.preview is None
    assert not view_model.can_add


def test_failed_upload_keeps_the_earlier_preview() -> None:
    good = make_image()
    view_model = make_view_model(FakeImageReader(good))
    view_model.upload_image(Path("a.png"))
    first = view_model.preview
    failing = MainViewModel(
        UploadImage(
            FakeImageReader(error=ImageReadError("Not a readable image")), Workspace()
        )
    )
    failing.preview = first
    failing.upload_image(Path("bad.png"))
    assert failing.preview is first
    assert failing.status == "Not a readable image"
