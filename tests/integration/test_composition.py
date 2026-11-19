"""Tests of the CompositionRoot."""

from pathlib import Path

from PIL import Image as PillowImage

from watermark_image.infrastructure.composition import CompositionRoot


def test_built_view_model_uploads_a_real_file(tmp_path: Path) -> None:
    path = tmp_path / "pic.png"
    PillowImage.new("RGB", (3, 2)).save(path)
    view_model = CompositionRoot().build_view_model()
    view_model.upload_image(path)
    assert view_model.status == "Loaded pic.png"
    assert view_model.preview is not None
    assert view_model.preview.width == 3
