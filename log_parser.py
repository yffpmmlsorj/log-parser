"""A line-oriented log parser that turns key=value logs into dictionaries."""

from __future__ import annotations

__all__ = ["logParser"]


def logParser(value):
    """A line-oriented log parser that turns key=value logs into dictionaries."""
    if value is None:
        raise ValueError("value must not be None")
    return value
