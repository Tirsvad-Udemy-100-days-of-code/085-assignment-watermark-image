"""@file capture_smoke.py
@brief Opens an empty window on the virtual display and saves a screenshot of it.
"""

import os
import pathlib
import tkinter

from PIL import ImageGrab


def main() -> None:
    """@brief Draw a small window and write its screenshot to SCREENSHOT_DIR."""
    folder = pathlib.Path(os.environ.get("SCREENSHOT_DIR", "docs/screenshots"))
    folder.mkdir(parents=True, exist_ok=True)

    root = tkinter.Tk()
    root.title("Watermark Image")
    root.geometry("640x400+0+0")
    tkinter.Label(root, text="Docker harness works", font=("DejaVu Sans", 24)).pack(
        expand=True
    )
    root.update_idletasks()
    root.update()

    left, top = root.winfo_rootx(), root.winfo_rooty()
    width, height = root.winfo_width(), root.winfo_height()
    screen = ImageGrab.grab(xdisplay=os.environ["DISPLAY"])
    screen.crop((left, top, left + width, top + height)).save(
        folder / "harness-smoke.png"
    )
    root.destroy()


if __name__ == "__main__":
    main()
