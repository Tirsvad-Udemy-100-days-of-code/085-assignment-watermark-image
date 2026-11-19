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
