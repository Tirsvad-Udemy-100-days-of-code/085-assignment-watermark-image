"""Tests of the Workspace."""

from tests.unit.fakes import FakeWatermarkRenderer, make_image, make_text_watermark
from watermark_image.application.workspace import Workspace
from watermark_image.domain.anchor import Anchor
from watermark_image.domain.position import Position
from watermark_image.domain.watermarked_image import WatermarkedImage


def test_workspace_starts_without_an_image() -> None:
    assert Workspace().current_image() is None


def test_replace_image_makes_it_current() -> None:
    workspace = Workspace()
    image = make_image()
    workspace.replace_image(image)
    assert workspace.current_image() is image


def test_replace_image_drops_the_earlier_image() -> None:
    workspace = Workspace()
    workspace.replace_image(make_image("a.png"))
    second = make_image("b.png")
    workspace.replace_image(second)
    assert workspace.current_image() is second


def make_marked_for(workspace: Workspace) -> WatermarkedImage:
    image = workspace.current_image()
    assert image is not None
    return FakeWatermarkRenderer().render(
        image, make_text_watermark(), Position(Anchor.CENTER, 0)
    )


def test_workspace_starts_without_a_marked_image() -> None:
    assert Workspace().current_marked() is None


def test_replace_marked_makes_it_current() -> None:
    workspace = Workspace()
    workspace.replace_image(make_image())
    marked = make_marked_for(workspace)
    workspace.replace_marked(marked)
    assert workspace.current_marked() is marked


def test_replace_image_drops_the_marked_image() -> None:
    workspace = Workspace()
    workspace.replace_image(make_image())
    workspace.replace_marked(make_marked_for(workspace))
    workspace.replace_image(make_image("b.png"))
    assert workspace.current_marked() is None
