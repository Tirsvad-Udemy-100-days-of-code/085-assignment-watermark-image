"""@file errors.py
@brief Error types the rules of the domain raise.
"""


class DomainError(Exception):
    """@brief Base class of every error the domain raises."""


class InvalidWatermarkError(DomainError):
    """@brief A watermark or its position holds a value the rules refuse."""
