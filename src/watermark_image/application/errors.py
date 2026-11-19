"""@file errors.py
@brief Error types the use cases raise.
"""


class ApplicationError(Exception):
    """@brief Base class of every error a use case raises."""


class ImageReadError(ApplicationError):
    """@brief A picture file could not be read."""
