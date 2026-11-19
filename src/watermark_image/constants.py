"""@file constants.py
@brief Every constant of the application, defined once.
"""

from typing import Final

## @brief Name shown in the window title.
APP_NAME: Final[str] = "Watermark Image"

## @brief File extensions the application can open, lower case with a dot.
SUPPORTED_READ_EXTENSIONS: Final[tuple[str, ...]] = (
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".webp",
)

## @brief File extensions the application can save, lower case with a dot.
SUPPORTED_WRITE_EXTENSIONS: Final[tuple[str, ...]] = (".jpg", ".jpeg", ".png")

## @brief Smallest opacity of a watermark, in percent (fully transparent).
MIN_OPACITY: Final[int] = 0

## @brief Largest opacity of a watermark, in percent (fully opaque).
MAX_OPACITY: Final[int] = 100

## @brief Opacity a new watermark starts with, in percent.
DEFAULT_OPACITY: Final[int] = 50

## @brief Smallest font size of a text watermark, in points.
MIN_FONT_SIZE: Final[int] = 1

## @brief Font size a new text watermark starts with, in points.
DEFAULT_FONT_SIZE: Final[int] = 48

## @brief Colour a new text watermark starts with, as a hex string.
DEFAULT_TEXT_COLOUR: Final[str] = "#ffffff"

## @brief Smallest scale of a logo watermark, in percent of the image width.
MIN_LOGO_SCALE: Final[int] = 1

## @brief Largest scale of a logo watermark, in percent of the image width.
MAX_LOGO_SCALE: Final[int] = 100

## @brief Scale a new logo watermark starts with, in percent of the image width.
DEFAULT_LOGO_SCALE: Final[int] = 25

## @brief Distance between a watermark and the image edge, in pixels.
DEFAULT_MARGIN: Final[int] = 16

## @brief Largest size of the preview area, as width and height in pixels.
PREVIEW_MAX_SIZE: Final[tuple[int, int]] = (640, 480)

## @brief Quality of a saved JPEG file, from 1 to 100.
JPEG_QUALITY: Final[int] = 92

## @brief Pixel format used for every picture held in memory (Pillow mode name).
PIXEL_MODE: Final[str] = "RGBA"

## @brief Bytes one pixel takes in the PIXEL_MODE format (red, green, blue, alpha).
BYTES_PER_PIXEL: Final[int] = 4

## @brief Status line text before any picture is loaded.
STATUS_EMPTY: Final[str] = "Upload an image to begin"

## @brief Status line text after a picture is loaded; `{name}` is the file name.
STATUS_LOADED: Final[str] = "Loaded {name}"

## @brief Reason shown when a file cannot be read as a picture.
ERROR_NOT_READABLE: Final[str] = "Not a readable image"

## @brief Text in front of the message in the status line of the window.
STATUS_LABEL_PREFIX: Final[str] = "Status: "

## @brief Caption of the button that uploads a picture.
UPLOAD_BUTTON_TEXT: Final[str] = "Upload image"

## @brief Caption of the button that saves the watermarked picture.
SAVE_BUTTON_TEXT: Final[str] = "Save image"

## @brief Title of the dialog that asks for the picture file.
OPEN_DIALOG_TITLE: Final[str] = "Upload image"

## @brief Name of the file type group in the open dialog.
IMAGE_FILES_LABEL: Final[str] = "Image files"

## @brief Space between the widgets of the window, in pixels.
PADDING: Final[int] = 8

## @brief Background colour of the preview area, as a hex string.
PREVIEW_BACKGROUND: Final[str] = "#e8e8e8"
