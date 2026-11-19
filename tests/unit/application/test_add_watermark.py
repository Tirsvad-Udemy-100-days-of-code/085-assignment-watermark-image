"""Tests of the AddWatermark use case."""

import pytest

from tests.unit.fakes import FakeWatermarkRenderer, make_image, make_request
from watermark_image import constants
from watermark_image.application.add_watermark import AddWatermark
from watermark_image.application.errors import NoImageError
from watermark_image.application.workspace import Workspace
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.errors import InvalidWatermarkError
from watermark_image.domain.text_watermark import TextWatermark


def make_use_case(
    with_image: bool = True,
) -> tuple[AddWatermark, Workspace, FakeWatermarkRenderer]:
    workspace = Workspace()
    if with_image:
        workspace.replace_image(make_image(width=4, height=2))
    renderer = FakeWatermarkRenderer()
    return AddWatermark(renderer, workspace), workspace, renderer


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
