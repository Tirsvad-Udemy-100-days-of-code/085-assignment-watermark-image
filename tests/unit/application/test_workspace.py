"""Tests of the Workspace."""

from tests.unit.fakes import make_image
from watermark_image.application.workspace import Workspace


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
