"""@file errors.py
@brief Error types the use cases raise.
"""


class ApplicationError(Exception):
    """@brief Base class of every error a use case raises."""


class ImageReadError(ApplicationError):
    """@brief A picture file could not be read."""


class NoImageError(ApplicationError):
    """@brief An operation needs a loaded Image and there is none."""


class NoMarkedImageError(ApplicationError):
    """@brief A save needs a WatermarkedImage and there is none."""


class ImageWriteError(ApplicationError):
    """@brief A picture file could not be written."""
