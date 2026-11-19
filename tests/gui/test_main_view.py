"""Graphical tests of the MainView; they run only in the Docker harness."""

import math
import os
from pathlib import Path

import pytest
from PIL import Image as PillowImage
from PIL import ImageDraw, ImageGrab

from watermark_image.domain.anchor import Anchor
from watermark_image.infrastructure.composition import CompositionRoot
from watermark_image.presentation.main_view import MainView

pytestmark = pytest.mark.gui

SAMPLE_SIZE = (1200, 800)
LOGO_SIZE = 200


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


def make_logo(path: Path) -> None:
    """A blue circle with a white star on a transparent background."""
    size = LOGO_SIZE
    emblem = PillowImage.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(emblem)
    draw.ellipse((4, 4, size - 5, size - 5), fill=(220, 40, 40, 255))
    centre = size / 2
    points = []
    for index in range(10):
        radius = size * 0.38 if index % 2 == 0 else size * 0.16
        angle = math.pi * index / 5 - math.pi / 2
        points.append(
            (centre + radius * math.cos(angle), centre + radius * math.sin(angle))
        )
    draw.polygon(points, fill=(255, 255, 255, 255))
    emblem.save(path)


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

        logo = tmp_path / "emblem.png"
        make_logo(logo)
        view_model.upload_image(sample)
        view.refresh()
        view._type.set("Logo")
        view_model.choose_logo(logo)
        view._scale.set(25)
        view._place_buttons[Anchor.TOP_LEFT].invoke()
        view._opacity.set(100)
        view._add_button.invoke()
        assert view_model.status == "Logo watermark added"
        assert screenshot(view, "step-3-logo.png").exists()

        view._place_buttons[Anchor.BOTTOM_RIGHT].invoke()
        view._opacity.set(70)
        assert view_model.status == "Logo watermark added"
        assert screenshot(view, "step-3-placed.png").exists()

        view_model.upload_image(sample)
        view.refresh()
        view._type.set("Text")
        view._text.set("Sample watermark")
        view._place_buttons[Anchor.BOTTOM_RIGHT].invoke()
        view._opacity.set(70)
        view._add_button.invoke()
        assert view_model.can_save
        assert str(view._save_button["state"]) == "normal"
        assert screenshot(view, "step-4-save.png").exists()

        saved = tmp_path / "saved.png"
        view_model.save_image(saved)
        view.refresh()
        assert view_model.status == "Saved saved.png"
        assert saved.exists()
        assert screenshot(view, "step-4-saved.png").exists()
    finally:
        view.window.destroy()
