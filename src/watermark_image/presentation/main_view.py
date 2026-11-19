"""@file main_view.py
@brief The main window, drawn after the wireframe of use case UC-001.
"""

import tkinter
from pathlib import Path
from tkinter import filedialog

from PIL import ImageTk

from watermark_image import constants
from watermark_image.presentation.main_view_model import MainViewModel
from watermark_image.presentation.preview_image import PreviewImage


class MainView:
    """@brief Draws the window and forwards input to the view model."""

    def __init__(self, view_model: MainViewModel) -> None:
        """@brief Build the window; it is shown by `run`.

        @param view_model The view model the window shows.
        """
        self._view_model = view_model
        self._preview_image = PreviewImage()
        self._photo: ImageTk.PhotoImage | None = None

        self.window = tkinter.Tk()
        self.window.title(constants.APP_NAME)
        self.window.resizable(False, False)

        toolbar = tkinter.Frame(self.window)
        toolbar.grid(row=0, column=0, sticky="w", padx=constants.PADDING)
        self._upload_button = tkinter.Button(
            toolbar, text=constants.UPLOAD_BUTTON_TEXT, command=self._on_upload
        )
        self._upload_button.pack(side="left", pady=constants.PADDING)
        self._save_button = tkinter.Button(
            toolbar, text=constants.SAVE_BUTTON_TEXT, state="disabled"
        )
        self._save_button.pack(side="left", padx=constants.PADDING)

        width, height = constants.PREVIEW_MAX_SIZE
        area = tkinter.Frame(
            self.window, width=width, height=height, bg=constants.PREVIEW_BACKGROUND
        )
        area.grid(row=1, column=0, padx=constants.PADDING)
        area.pack_propagate(False)
        self._preview_label = tkinter.Label(area, bg=constants.PREVIEW_BACKGROUND)
        self._preview_label.pack(expand=True)

        self._status_label = tkinter.Label(self.window, anchor="w")
        self._status_label.grid(
            row=2, column=0, sticky="we", padx=constants.PADDING, pady=constants.PADDING
        )
        self.refresh()

    def refresh(self) -> None:
        """@brief Show the current state of the view model."""
        preview = self._view_model.preview
        if preview is None:
            self._photo = None
            self._preview_label.configure(image="")
        else:
            self._photo = self._preview_image.to_photo_image(preview)
            self._preview_label.configure(image=self._photo)
        if self._view_model.can_save:
            self._save_button.configure(state="normal")
        else:
            self._save_button.configure(state="disabled")
        self._status_label.configure(
            text=constants.STATUS_LABEL_PREFIX + self._view_model.status
        )

    def run(self) -> None:
        """@brief Show the window and handle input until it is closed."""
        self.window.mainloop()

    def _on_upload(self) -> None:
        extensions = " ".join(f"*{ext}" for ext in constants.SUPPORTED_READ_EXTENSIONS)
        chosen = filedialog.askopenfilename(
            title=constants.OPEN_DIALOG_TITLE,
            filetypes=[(constants.IMAGE_FILES_LABEL, extensions)],
        )
        if chosen:
            self._view_model.upload_image(Path(chosen))
            self.refresh()
