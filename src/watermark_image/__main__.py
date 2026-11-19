"""@file __main__.py
@brief Entry point: `python -m watermark_image` starts the application.
"""

from watermark_image.infrastructure.composition import CompositionRoot
from watermark_image.presentation.main_view import MainView


def main() -> None:
    """@brief Build the view model and show the main window."""
    MainView(CompositionRoot().build_view_model()).run()


if __name__ == "__main__":
    main()
