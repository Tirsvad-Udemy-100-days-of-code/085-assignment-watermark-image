"""@file main_view.py
@brief The main window, drawn after the wireframe of use case UC-001.
"""

import tkinter
from collections.abc import Callable
from pathlib import Path
from tkinter import filedialog

from PIL import ImageTk

from watermark_image import constants
from watermark_image.application.watermark_request import WatermarkRequest
from watermark_image.domain.anchor import Anchor
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
        self._anchor = Anchor.CENTER
        self._place_buttons: dict[Anchor, tkinter.Button] = {}
        self._common_controls: list[tkinter.Widget] = []
        self._text_controls: list[tkinter.Widget] = []
        self._logo_controls: list[tkinter.Widget] = []

        self.window = tkinter.Tk()
        self.window.title(constants.APP_NAME)
        self.window.resizable(False, False)

        toolbar = tkinter.Frame(self.window)
        toolbar.grid(row=0, column=0, columnspan=2, sticky="w", padx=constants.PADDING)
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

        self._build_control_panel()

        self._status_label = tkinter.Label(self.window, anchor="w")
        self._status_label.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="we",
            padx=constants.PADDING,
            pady=constants.PADDING,
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
        self._set_states()
        self._logo_name.set(
            constants.NO_LOGO_TEXT
            if self._view_model.logo_source is None
            else self._view_model.logo_source.name
        )
        self._show_selected_place()

    def _set_states(self) -> None:
        enabled = self._view_model.can_add
        using_logo = self._view_model.use_logo
        groups = (
            (self._common_controls, enabled),
            (self._text_controls, enabled and not using_logo),
            (self._logo_controls, enabled and using_logo),
        )
        for controls, active in groups:
            for control in controls:
                control["state"] = "normal" if active else "disabled"

    def run(self) -> None:
        """@brief Show the window and handle input until it is closed."""
        self.window.mainloop()

    def _build_control_panel(self) -> None:
        panel = tkinter.Frame(self.window)
        panel.grid(row=1, column=1, sticky="n", padx=constants.PADDING)
        row = 0

        tkinter.Label(panel, text=constants.TYPE_LABEL, anchor="w").grid(
            row=row, column=0, columnspan=2, sticky="w"
        )
        row += 1
        self._type = tkinter.StringVar(value=constants.TYPE_TEXT_LABEL)
        types = tkinter.Frame(panel)
        types.grid(row=row, column=0, columnspan=2, sticky="w")
        for caption in (constants.TYPE_TEXT_LABEL, constants.TYPE_LOGO_LABEL):
            radio = tkinter.Radiobutton(
                types, text=caption, variable=self._type, value=caption
            )
            radio.pack(side="left")
            self._common_controls.append(radio)
        self._type.trace_add("write", self._on_type_changed)
        row += 1

        self._text = tkinter.StringVar(value=constants.DEFAULT_TEXT)
        self._add_row(
            panel,
            row,
            constants.TEXT_LABEL,
            tkinter.Entry(panel, textvariable=self._text, width=constants.ENTRY_WIDTH),
            self._text_controls,
        )
        row += 1

        self._size = tkinter.StringVar(value=str(constants.DEFAULT_FONT_SIZE))
        self._add_row(
            panel,
            row,
            constants.SIZE_LABEL,
            tkinter.Spinbox(
                panel,
                from_=constants.MIN_FONT_SIZE,
                to=constants.CONTROL_MAX_FONT_SIZE,
                textvariable=self._size,
                width=constants.ENTRY_WIDTH,
            ),
            self._text_controls,
        )
        row += 1

        self._colour = tkinter.StringVar(value=constants.DEFAULT_TEXT_COLOUR)
        self._add_row(
            panel,
            row,
            constants.COLOUR_LABEL,
            tkinter.Entry(
                panel, textvariable=self._colour, width=constants.ENTRY_WIDTH
            ),
            self._text_controls,
        )
        row += 1

        self._logo_name = tkinter.StringVar(value=constants.NO_LOGO_TEXT)
        logo = tkinter.Frame(panel)
        choose = tkinter.Button(
            logo, text=constants.CHOOSE_LOGO_BUTTON_TEXT, command=self._on_choose_logo
        )
        choose.pack(side="left")
        tkinter.Label(logo, textvariable=self._logo_name).pack(
            side="left", padx=constants.PADDING
        )
        self._logo_controls.append(choose)
        self._add_row(panel, row, constants.LOGO_LABEL, logo, self._logo_controls)
        row += 1

        self._scale = tkinter.Scale(
            panel,
            from_=constants.MIN_LOGO_SCALE,
            to=constants.MAX_LOGO_SCALE,
            orient="horizontal",
            command=self._on_control_changed,
        )
        self._scale.set(constants.DEFAULT_LOGO_SCALE)
        self._add_row(
            panel, row, constants.SCALE_LABEL, self._scale, self._logo_controls
        )
        row += 1

        for variable in (self._text, self._size, self._colour):
            variable.trace_add("write", self._on_control_changed)

        places = tkinter.Frame(panel)
        for index, anchor in enumerate(Anchor):
            button = tkinter.Button(
                places,
                text=constants.PLACE_CAPTIONS[index],
                width=3,
                command=self._place_command(anchor),
            )
            line, column = divmod(index, constants.PLACE_GRID_COLUMNS)
            button.grid(row=line, column=column)
            self._place_buttons[anchor] = button
            self._common_controls.append(button)
        self._add_row(panel, row, constants.PLACE_LABEL, places, self._common_controls)
        row += 1

        self._opacity = tkinter.Scale(
            panel,
            from_=constants.MIN_OPACITY,
            to=constants.MAX_OPACITY,
            orient="horizontal",
            command=self._on_control_changed,
        )
        self._opacity.set(constants.DEFAULT_OPACITY)
        self._add_row(
            panel, row, constants.OPACITY_LABEL, self._opacity, self._common_controls
        )
        row += 1

        self._add_button = tkinter.Button(
            panel, text=constants.ADD_BUTTON_TEXT, command=self._on_add
        )
        self._add_button.grid(row=row, column=0, columnspan=2, pady=constants.PADDING)
        self._common_controls.append(self._add_button)

    def _add_row(
        self,
        panel: tkinter.Frame,
        row: int,
        caption: str,
        widget: tkinter.Widget,
        group: list[tkinter.Widget],
    ) -> None:
        tkinter.Label(panel, text=caption, anchor="w").grid(
            row=row, column=0, sticky="w"
        )
        widget.grid(row=row, column=1, sticky="w", pady=2)
        if not isinstance(widget, tkinter.Frame):
            group.append(widget)

    def _place_command(self, anchor: Anchor) -> Callable[[], None]:
        return lambda: self._on_place(anchor)

    def _show_selected_place(self) -> None:
        default = self.window.cget("bg")
        for anchor, button in self._place_buttons.items():
            selected = anchor is self._anchor
            button.configure(
                bg=constants.PLACE_SELECTED_BACKGROUND if selected else default,
                relief="sunken" if selected else "raised",
            )

    def _read_request(self) -> WatermarkRequest:
        logo_source = (
            self._view_model.logo_source if self._view_model.use_logo else None
        )
        return WatermarkRequest(
            logo_source=logo_source,
            logo_scale_percent=int(self._scale.get()),
            text=self._text.get(),
            font_size=self._to_int(self._size.get()),
            colour=self._colour.get(),
            anchor=self._anchor,
            opacity=int(self._opacity.get()),
        )

    def _to_int(self, value: str) -> int:
        # A size that is not a number becomes 0, which the domain refuses with
        # its own message; the view holds no rule of its own.
        try:
            return int(value)
        except ValueError:
            return 0

    def _on_place(self, anchor: Anchor) -> None:
        self._anchor = anchor
        self._show_selected_place()
        self._on_control_changed()

    def _on_add(self) -> None:
        self._view_model.add_watermark(self._read_request())
        self.refresh()

    def _on_type_changed(self, *_ignored: str) -> None:
        self._view_model.use_logo = self._type.get() == constants.TYPE_LOGO_LABEL
        self.refresh()
        self._on_control_changed()

    def _on_choose_logo(self) -> None:
        extensions = " ".join(f"*{ext}" for ext in constants.SUPPORTED_READ_EXTENSIONS)
        chosen = filedialog.askopenfilename(
            title=constants.LOGO_DIALOG_TITLE,
            filetypes=[(constants.IMAGE_FILES_LABEL, extensions)],
        )
        if chosen:
            self._view_model.choose_logo(Path(chosen))
            self._on_control_changed()
            self.refresh()

    def _on_control_changed(self, *_ignored: str) -> None:
        if self._view_model.has_watermark:
            self._on_add()

    def _on_upload(self) -> None:
        extensions = " ".join(f"*{ext}" for ext in constants.SUPPORTED_READ_EXTENSIONS)
        chosen = filedialog.askopenfilename(
            title=constants.OPEN_DIALOG_TITLE,
            filetypes=[(constants.IMAGE_FILES_LABEL, extensions)],
        )
        if chosen:
            self._view_model.upload_image(Path(chosen))
            self.refresh()
