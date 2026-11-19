"""Tests of the MainViewModel (no window needed)."""

from pathlib import Path

import pytest

from tests.unit.fakes import (
    FakeImageReader,
    FakeWatermarkRenderer,
    make_image,
    make_logo_request,
    make_request,
)
from watermark_image.application.add_watermark import AddWatermark
from watermark_image.application.errors import ImageReadError
from watermark_image.application.upload_image import UploadImage
from watermark_image.application.workspace import Workspace
from watermark_image.presentation.main_view_model import MainViewModel


def make_view_model(reader: FakeImageReader) -> MainViewModel:
    workspace = Workspace()
    return MainViewModel(
        UploadImage(reader, workspace),
        AddWatermark(reader, FakeWatermarkRenderer(), workspace),
    )


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
    failing = make_view_model(
        FakeImageReader(error=ImageReadError("Not a readable image"))
    )
    failing.preview = first
    failing.upload_image(Path("bad.png"))
    assert failing.preview is first
    assert failing.status == "Not a readable image"


def loaded_view_model() -> MainViewModel:
    view_model = make_view_model(FakeImageReader(make_image(width=4, height=2)))
    view_model.upload_image(Path("a.png"))
    return view_model


def test_add_watermark_shows_the_marked_picture() -> None:
    view_model = loaded_view_model()
    plain = view_model.preview
    view_model.add_watermark(make_request())
    assert view_model.status == "Text watermark added"
    assert view_model.preview is not None
    assert view_model.preview != plain
    assert view_model.has_watermark


def test_add_watermark_keeps_saving_disabled() -> None:
    view_model = loaded_view_model()
    view_model.add_watermark(make_request())
    assert not view_model.can_save


def test_add_watermark_without_a_picture_asks_for_an_upload() -> None:
    view_model = make_view_model(FakeImageReader(make_image()))
    view_model.add_watermark(make_request())
    assert view_model.status == "Upload an image first"
    assert view_model.preview is None
    assert not view_model.has_watermark


@pytest.mark.parametrize(
    ("values", "message"),
    [
        ({"text": ""}, "The text must not be empty"),
        ({"font_size": 0}, "The font size must be at least 1"),
        ({"colour": "red"}, "The colour must look like #rrggbb"),
        ({"opacity": 101}, "Opacity must be from 0 to 100"),
    ],
)
def test_add_watermark_shows_the_reason_and_keeps_the_preview(
    values: dict[str, object], message: str
) -> None:
    view_model = loaded_view_model()
    view_model.add_watermark(make_request())
    marked = view_model.preview
    view_model.add_watermark(make_request(**values))  # type: ignore[arg-type]
    assert view_model.status == message
    assert view_model.preview is marked
    assert view_model.has_watermark


def test_upload_after_a_watermark_clears_the_watermark_flag() -> None:
    view_model = loaded_view_model()
    view_model.add_watermark(make_request())
    view_model.upload_image(Path("b.png"))
    assert not view_model.has_watermark


def test_add_logo_watermark_shows_the_marked_picture() -> None:
    view_model = loaded_view_model()
    plain = view_model.preview
    view_model.use_logo = True
    view_model.add_watermark(make_logo_request())
    assert view_model.status == "Logo watermark added"
    assert view_model.preview != plain
    assert view_model.has_watermark


def test_choose_logo_remembers_the_file() -> None:
    view_model = loaded_view_model()
    assert view_model.logo_source is None
    view_model.choose_logo(Path("emblem.png"))
    assert view_model.logo_source == Path("emblem.png")


def test_logo_type_without_a_logo_asks_for_one() -> None:
    view_model = loaded_view_model()
    view_model.use_logo = True
    view_model.add_watermark(make_request())
    assert view_model.status == "Choose a logo first"
    assert not view_model.has_watermark


def test_unreadable_logo_shows_the_reason_and_keeps_the_preview() -> None:
    reader = FakeImageReader(make_image(width=4, height=2))
    view_model = make_view_model(reader)
    view_model.upload_image(Path("a.png"))
    view_model.add_watermark(make_request())
    marked = view_model.preview
    reader.fail_with(ImageReadError("Not a readable image"))
    view_model.use_logo = True
    view_model.add_watermark(make_logo_request("bad.png"))
    assert view_model.status == "Not a readable image"
    assert view_model.preview is marked


def test_invalid_logo_scale_shows_the_reason() -> None:
    view_model = loaded_view_model()
    view_model.use_logo = True
    view_model.add_watermark(make_logo_request(logo_scale_percent=101))
    assert view_model.status == "The logo scale must be from 1 to 100 percent"
    assert not view_model.has_watermark
