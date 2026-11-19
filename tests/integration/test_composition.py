"""Tests of the CompositionRoot."""

from pathlib import Path

from PIL import Image as PillowImage

from watermark_image.application.watermark_request import WatermarkRequest
from watermark_image.domain.anchor import Anchor
from watermark_image.infrastructure.composition import CompositionRoot


def test_built_view_model_uploads_a_real_file(tmp_path: Path) -> None:
    path = tmp_path / "pic.png"
    PillowImage.new("RGB", (3, 2)).save(path)
    view_model = CompositionRoot().build_view_model()
    view_model.upload_image(path)
    assert view_model.status == "Loaded pic.png"
    assert view_model.preview is not None
    assert view_model.preview.width == 3


def test_built_view_model_adds_a_watermark_to_a_real_file(tmp_path: Path) -> None:
    path = tmp_path / "pic.png"
    PillowImage.new("RGB", (200, 100)).save(path)
    original_bytes = path.read_bytes()
    view_model = CompositionRoot().build_view_model()
    view_model.upload_image(path)
    plain = view_model.preview
    view_model.add_watermark(
        WatermarkRequest(
            text="Sample",
            font_size=32,
            colour="#ffffff",
            anchor=Anchor.BOTTOM_RIGHT,
            opacity=100,
        )
    )
    assert view_model.status == "Text watermark added"
    assert view_model.preview is not None
    assert plain is not None
    assert (view_model.preview.width, view_model.preview.height) == (200, 100)
    assert view_model.preview.pixels != plain.pixels
    assert path.read_bytes() == original_bytes


def test_built_view_model_refuses_an_empty_text(tmp_path: Path) -> None:
    path = tmp_path / "pic.png"
    PillowImage.new("RGB", (20, 10)).save(path)
    view_model = CompositionRoot().build_view_model()
    view_model.upload_image(path)
    plain = view_model.preview
    view_model.add_watermark(
        WatermarkRequest(
            text="", font_size=12, colour="#ffffff", anchor=Anchor.CENTER, opacity=50
        )
    )
    assert view_model.status == "The text must not be empty"
    assert view_model.preview is plain


def test_built_view_model_adds_a_logo_watermark_from_real_files(
    tmp_path: Path,
) -> None:
    path = tmp_path / "pic.png"
    logo = tmp_path / "logo.png"
    PillowImage.new("RGB", (200, 100)).save(path)
    PillowImage.new("RGBA", (20, 20), (255, 0, 0, 255)).save(logo)
    original_bytes = path.read_bytes()
    view_model = CompositionRoot().build_view_model()
    view_model.upload_image(path)
    view_model.use_logo = True
    view_model.add_watermark(
        WatermarkRequest(
            text="",
            font_size=12,
            colour="#ffffff",
            logo_source=logo,
            logo_scale_percent=10,
            anchor=Anchor.TOP_LEFT,
            opacity=100,
        )
    )
    assert view_model.status == "Logo watermark added"
    assert view_model.preview is not None
    start = (16 * 200 + 16) * 4
    assert view_model.preview.pixels[start : start + 4] == bytes([255, 0, 0, 255])
    assert path.read_bytes() == original_bytes


def test_built_view_model_refuses_an_unreadable_logo(tmp_path: Path) -> None:
    path = tmp_path / "pic.png"
    logo = tmp_path / "logo.png"
    PillowImage.new("RGB", (20, 10)).save(path)
    logo.write_bytes(b"not a picture")
    view_model = CompositionRoot().build_view_model()
    view_model.upload_image(path)
    plain = view_model.preview
    view_model.use_logo = True
    view_model.add_watermark(
        WatermarkRequest(
            text="",
            font_size=12,
            colour="#ffffff",
            logo_source=logo,
            anchor=Anchor.CENTER,
            opacity=50,
        )
    )
    assert view_model.status == "Not a readable image"
    assert view_model.preview is plain
