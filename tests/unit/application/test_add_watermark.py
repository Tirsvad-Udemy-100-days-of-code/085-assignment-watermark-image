"""Tests of the AddWatermark use case."""

from pathlib import Path

import pytest

from tests.unit.fakes import (
    FakeImageReader,
    FakeWatermarkRenderer,
    make_image,
    make_logo_request,
    make_request,
)
from watermark_image import constants
from watermark_image.application.add_watermark import AddWatermark
from watermark_image.application.errors import ImageReadError, NoImageError
from watermark_image.application.workspace import Workspace
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.errors import InvalidWatermarkError
from watermark_image.domain.logo_watermark import LogoWatermark
from watermark_image.domain.text_watermark import TextWatermark

LOGO = make_image("logo.png", 3, 2)


def make_use_case(
    with_image: bool = True, reader: FakeImageReader | None = None
) -> tuple[AddWatermark, Workspace, FakeWatermarkRenderer]:
    workspace = Workspace()
    if with_image:
        workspace.replace_image(make_image(width=4, height=2))
    renderer = FakeWatermarkRenderer()
    reader = reader or FakeImageReader(LOGO)
    return AddWatermark(reader, renderer, workspace), workspace, renderer


def test_execute_raises_when_no_image_is_loaded() -> None:
    use_case, workspace, renderer = make_use_case(with_image=False)
    with pytest.raises(NoImageError, match="Upload an image first"):
        use_case.execute(make_request())
    assert renderer.calls == []
    assert workspace.current_marked() is None


@pytest.mark.parametrize(
    "request_values",
    [
        {"text": ""},
        {"text": "  "},
        {"font_size": 0},
        {"colour": "red"},
        {"opacity": -1},
        {"opacity": 101},
    ],
)
def test_execute_refuses_invalid_values_and_changes_nothing(
    request_values: dict[str, object],
) -> None:
    use_case, workspace, renderer = make_use_case()
    first = use_case.execute(make_request())
    marked = workspace.current_marked()
    with pytest.raises(InvalidWatermarkError):
        use_case.execute(make_request(**request_values))  # type: ignore[arg-type]
    assert workspace.current_marked() is marked
    assert len(renderer.calls) == 1
    assert first.width == 4


def test_execute_renders_a_text_watermark_at_the_chosen_anchor() -> None:
    use_case, workspace, renderer = make_use_case()
    use_case.execute(make_request("Hi", 20, "#112233", Anchor.TOP_RIGHT, 70))
    image, watermark, position = renderer.calls[0]
    assert image is workspace.current_image()
    assert watermark == TextWatermark(
        opacity=70, text="Hi", font_size=20, colour="#112233"
    )
    assert (position.anchor, position.margin) == (
        Anchor.TOP_RIGHT,
        constants.DEFAULT_MARGIN,
    )


def test_execute_keeps_the_original_image_untouched() -> None:
    use_case, workspace, _ = make_use_case()
    original = workspace.current_image()
    assert original is not None
    pixels_before = original.pixels
    use_case.execute(make_request())
    assert workspace.current_image() is original
    assert original.pixels == pixels_before


def test_execute_replaces_the_marked_image_and_returns_its_view() -> None:
    use_case, workspace, _ = make_use_case()
    use_case.execute(make_request())
    first = workspace.current_marked()
    view = use_case.execute(make_request(opacity=10))
    second = workspace.current_marked()
    assert second is not None
    assert second is not first
    assert (view.width, view.height, view.pixels) == (4, 2, second.pixels)


def test_execute_reads_the_logo_and_renders_a_logo_watermark() -> None:
    reader = FakeImageReader(LOGO)
    use_case, workspace, renderer = make_use_case(reader=reader)
    use_case.execute(make_logo_request("emblem.png", 40, Anchor.BOTTOM_LEFT, 80))
    assert reader.read_sources == [Path("emblem.png")]
    image, watermark, position = renderer.calls[0]
    assert image is workspace.current_image()
    assert watermark == LogoWatermark(opacity=80, logo=LOGO, scale_percent=40)
    assert position.anchor is Anchor.BOTTOM_LEFT


def test_execute_does_not_read_a_logo_for_a_text_request() -> None:
    reader = FakeImageReader(LOGO)
    use_case, _, _ = make_use_case(reader=reader)
    use_case.execute(make_request())
    assert reader.read_sources == []


def test_execute_with_an_unreadable_logo_changes_nothing() -> None:
    reader = FakeImageReader(error=ImageReadError("Not a readable image"))
    use_case, workspace, renderer = make_use_case(reader=reader)
    original = workspace.current_image()
    assert original is not None
    pixels_before = original.pixels
    with pytest.raises(ImageReadError, match="Not a readable image"):
        use_case.execute(make_logo_request())
    assert workspace.current_marked() is None
    assert workspace.current_image() is original
    assert original.pixels == pixels_before
    assert renderer.calls == []


@pytest.mark.parametrize("scale", [0, 101])
def test_execute_refuses_a_logo_scale_outside_the_limits(scale: int) -> None:
    use_case, workspace, renderer = make_use_case()
    with pytest.raises(InvalidWatermarkError):
        use_case.execute(make_logo_request(logo_scale_percent=scale))
    assert workspace.current_marked() is None
    assert renderer.calls == []


def test_execute_keeps_the_original_image_untouched_for_a_logo() -> None:
    use_case, workspace, _ = make_use_case()
    original = workspace.current_image()
    assert original is not None
    pixels_before = original.pixels
    view = use_case.execute(make_logo_request())
    assert workspace.current_image() is original
    assert original.pixels == pixels_before
    assert view.pixels != pixels_before
