"""Tests of the SaveImage use case."""

from pathlib import Path

import pytest

from tests.unit.fakes import FakeImageWriter, make_marked
from watermark_image.application.confirmation import Confirmation
from watermark_image.application.errors import ImageWriteError, NoMarkedImageError
from watermark_image.application.save_image import SaveImage
from watermark_image.application.workspace import Workspace
from watermark_image.domain.errors import OverwriteOriginalError


def make_use_case(
    writer: FakeImageWriter, with_marked: bool = True
) -> tuple[SaveImage, Workspace]:
    workspace = Workspace()
    if with_marked:
        marked = make_marked("photo.png")
        workspace.replace_image(marked.image)
        workspace.replace_marked(marked)
    return SaveImage(writer, workspace), workspace


def test_execute_writes_the_marked_image_once_and_confirms() -> None:
    writer = FakeImageWriter()
    use_case, workspace = make_use_case(writer)
    target = Path("out.png")
    result = use_case.execute(target)
    assert result == Confirmation(target)
    assert writer.calls == [(workspace.current_marked(), target)]


def test_execute_refuses_when_there_is_no_marked_image() -> None:
    writer = FakeImageWriter()
    use_case, _ = make_use_case(writer, with_marked=False)
    with pytest.raises(NoMarkedImageError):
        use_case.execute(Path("out.png"))
    assert writer.calls == []


@pytest.mark.parametrize("spelling", ["photo.png", "./photo.png", "sub/../photo.png"])
def test_execute_refuses_the_original_in_any_spelling(spelling: str) -> None:
    writer = FakeImageWriter()
    use_case, _ = make_use_case(writer)
    with pytest.raises(OverwriteOriginalError):
        use_case.execute(Path(spelling))
    assert writer.calls == []


def test_execute_keeps_the_state_when_the_writer_fails() -> None:
    writer = FakeImageWriter(error=ImageWriteError("no"))
    use_case, workspace = make_use_case(writer)
    image = workspace.current_image()
    marked = workspace.current_marked()
    with pytest.raises(ImageWriteError):
        use_case.execute(Path("out.png"))
    assert workspace.current_image() is image
    assert workspace.current_marked() is marked
