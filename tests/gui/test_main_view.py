"""Graphical tests of the MainView; they run only in the Docker harness."""

import os
from pathlib import Path

import pytest
from PIL import Image as PillowImage
from PIL import ImageGrab

from watermark_image.domain.anchor import Anchor
from watermark_image.infrastructure.composition import CompositionRoot
from watermark_image.presentation.main_view import MainView

pytestmark = pytest.mark.gui

SAMPLE_SIZE = (1200, 800)


def make_gradient(path: Path) -> None:
    width, height = SAMPLE_SIZE
    picture = PillowImage.new("RGB", SAMPLE_SIZE)
    picture.putdata(
        [
            (x * 255 // width, y * 255 // height, 255 - x * 255 // width)
            for y in range(height)
            for x in range(width)
        ]
    )
    picture.save(path)


def screenshot(view: MainView, name: str) -> Path:
    folder = Path(os.environ.get("SCREENSHOT_DIR", "docs/screenshots"))
    folder.mkdir(parents=True, exist_ok=True)
    window = view.window
    window.update_idletasks()
    window.update()
    left, top = window.winfo_rootx(), window.winfo_rooty()
    right, bottom = left + window.winfo_width(), top + window.winfo_height()
    target = folder / name
    ImageGrab.grab(xdisplay=os.environ["DISPLAY"]).crop(
        (left, top, right, bottom)
    ).save(target)
    return target


def test_main_view_shows_the_empty_the_loaded_and_the_watermarked_state(
    tmp_path: Path,
) -> None:
    sample = tmp_path / "gradient.png"
    make_gradient(sample)
    view_model = CompositionRoot().build_view_model()
    view = MainView(view_model)
    try:
        view.window.geometry("+0+0")
        assert screenshot(view, "step-1-empty.png").exists()

        view_model.upload_image(sample)
        view.refresh()
        assert screenshot(view, "step-1-loaded.png").exists()
        assert view_model.status == "Loaded gradient.png"

        view._text.set("Sample watermark")
        view._size.set("64")
        view._colour.set("#ffffff")
        view._add_button.invoke()
        assert view_model.status == "Text watermark added"
        assert screenshot(view, "step-2-text.png").exists()

        view._place_buttons[Anchor.BOTTOM_RIGHT].invoke()
        view._opacity.set(70)
        assert view_model.status == "Text watermark added"
        assert screenshot(view, "step-2-placed.png").exists()
    finally:
        view.window.destroy()
