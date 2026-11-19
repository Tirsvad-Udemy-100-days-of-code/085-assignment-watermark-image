"""Tests of the PillowWatermarkRenderer against known pixels."""

from pathlib import Path

import pytest
from PIL import ImageFont

from tests.unit.fakes import make_text_watermark
from watermark_image import constants
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.errors import InvalidWatermarkError
from watermark_image.domain.image import Image
from watermark_image.domain.position import Position
from watermark_image.domain.text_watermark import TextWatermark
from watermark_image.domain.watermark import Watermark
from watermark_image.infrastructure.pillow_watermark_renderer import (
    PillowWatermarkRenderer,
)

WIDTH = 300
HEIGHT = 200
MARGIN = 16
BLACK = bytes([0, 0, 0, 255])


def black_image() -> Image:
    return Image(Path("black.png"), WIDTH, HEIGHT, BLACK * (WIDTH * HEIGHT))


def changed_pixels(before: bytes, after: bytes) -> list[tuple[int, int]]:
    """Coordinates (x, y) of every pixel that differs."""
    size = constants.BYTES_PER_PIXEL
    found = []
    for index in range(WIDTH * HEIGHT):
        start = index * size
        if before[start : start + size] != after[start : start + size]:
            found.append((index % WIDTH, index // WIDTH))
    return found


def render_changes(
    anchor: Anchor, opacity: int = 100, text: str = "Hi", size: int = 24
) -> list[tuple[int, int]]:
    image = black_image()
    watermark = make_text_watermark(text, size, "#ffffff", opacity)
    marked = PillowWatermarkRenderer().render(
        image, watermark, Position(anchor, MARGIN)
    )
    return changed_pixels(image.pixels, marked.pixels)


def test_opacity_100_white_text_changes_pixels_only_in_the_corner() -> None:
    changed = render_changes(Anchor.TOP_LEFT)
    assert changed
    assert all(
        MARGIN <= x < WIDTH // 3 and MARGIN <= y < HEIGHT // 3 for x, y in changed
    )


def test_opacity_100_gives_fully_white_pixels_inside_the_text() -> None:
    image = black_image()
    marked = PillowWatermarkRenderer().render(
        image,
        make_text_watermark("MMMM", 40, "#ffffff", 100),
        Position(Anchor.TOP_LEFT, MARGIN),
    )
    white = bytes([255, 255, 255, 255])
    pixels = [marked.pixels[i : i + 4] for i in range(0, len(marked.pixels), 4)]
    assert white in pixels


def test_opacity_0_leaves_the_image_identical() -> None:
    image = black_image()
    marked = PillowWatermarkRenderer().render(
        image, make_text_watermark("Hi", 24, "#ffffff", 0), Position(Anchor.CENTER, 0)
    )
    assert marked.pixels == image.pixels


def test_half_opacity_is_dimmer_than_full_opacity() -> None:
    image = black_image()
    position = Position(Anchor.TOP_LEFT, MARGIN)
    full = PillowWatermarkRenderer().render(
        image, make_text_watermark("MMMM", 40, "#ffffff", 100), position
    )
    half = PillowWatermarkRenderer().render(
        image, make_text_watermark("MMMM", 40, "#ffffff", 50), position
    )
    assert max(half.pixels[0::4]) == pytest.approx(128, abs=1)
    assert max(full.pixels[0::4]) == 255


@pytest.mark.parametrize(
    ("anchor", "column", "line"),
    [
        (Anchor.TOP_LEFT, 0, 0),
        (Anchor.TOP_CENTER, 1, 0),
        (Anchor.TOP_RIGHT, 2, 0),
        (Anchor.MIDDLE_LEFT, 0, 1),
        (Anchor.CENTER, 1, 1),
        (Anchor.MIDDLE_RIGHT, 2, 1),
        (Anchor.BOTTOM_LEFT, 0, 2),
        (Anchor.BOTTOM_CENTER, 1, 2),
        (Anchor.BOTTOM_RIGHT, 2, 2),
    ],
)
def test_each_anchor_puts_the_text_in_its_third_of_the_picture(
    anchor: Anchor, column: int, line: int
) -> None:
    changed = render_changes(anchor)
    assert changed
    third_w, third_h = WIDTH / 3, HEIGHT / 3
    for x, y in changed:
        assert column * third_w <= x < (column + 1) * third_w
        assert line * third_h <= y < (line + 1) * third_h


def test_corner_text_keeps_the_margin_from_the_edges() -> None:
    changed = render_changes(Anchor.BOTTOM_RIGHT)
    assert max(x for x, _ in changed) <= WIDTH - 1 - MARGIN + 1
    assert max(y for _, y in changed) <= HEIGHT - 1 - MARGIN + 1


def test_text_wider_than_the_picture_stays_inside_without_error() -> None:
    changed = render_changes(Anchor.BOTTOM_RIGHT, text="Very long text " * 10, size=40)
    assert changed
    assert all(0 <= x < WIDTH and 0 <= y < HEIGHT for x, y in changed)


def test_render_never_modifies_the_input_image() -> None:
    image = black_image()
    before = bytes(image.pixels)
    marked = PillowWatermarkRenderer().render(
        image, make_text_watermark(), Position(Anchor.CENTER, MARGIN)
    )
    assert image.pixels == before
    assert marked.image is image
    assert marked.pixels is not image.pixels


def test_render_returns_the_watermark_and_position_it_used() -> None:
    watermark = make_text_watermark()
    position = Position(Anchor.CENTER, MARGIN)
    marked = PillowWatermarkRenderer().render(black_image(), watermark, position)
    assert marked.watermark is watermark
    assert marked.position is position
    assert (marked.width, marked.height) == (WIDTH, HEIGHT)


def test_text_colour_is_used() -> None:
    image = black_image()
    marked = PillowWatermarkRenderer().render(
        image,
        TextWatermark(opacity=100, text="MMMM", font_size=40, colour="#ff0000"),
        Position(Anchor.CENTER, 0),
    )
    assert max(marked.pixels[0::4]) == 255
    assert max(marked.pixels[1::4]) == 0
    assert max(marked.pixels[2::4]) == 0


def test_text_on_a_one_pixel_image_does_not_fail() -> None:
    image = Image(Path("one.png"), 1, 1, BLACK)
    marked = PillowWatermarkRenderer().render(
        image, make_text_watermark(), Position(Anchor.CENTER, MARGIN)
    )
    assert (marked.width, marked.height) == (1, 1)


def test_render_refuses_a_watermark_that_is_not_text() -> None:
    class Other(Watermark):
        pass

    with pytest.raises(InvalidWatermarkError):
        PillowWatermarkRenderer().render(
            black_image(), Other(50), Position(Anchor.CENTER, 0)
        )


def test_render_wraps_a_picture_library_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fail(*_args: object, **_kwargs: object) -> None:
        raise OSError("no font support")

    monkeypatch.setattr(ImageFont, "load_default", fail)
    with pytest.raises(InvalidWatermarkError):
        PillowWatermarkRenderer().render(
            black_image(), make_text_watermark(), Position(Anchor.CENTER, 0)
        )
