"""Small, dependency-free utility functions for a sample CI/CD project."""

from __future__ import annotations

import math
from collections.abc import Iterable
from numbers import Real


def normalize_whitespace(text: str) -> str:
    """Collapse runs of whitespace in *text* to single spaces.

    Leading and trailing whitespace is removed. The function preserves the
    original spelling and punctuation of all non-whitespace characters.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())


def word_count(text: str) -> int:
    """Return the number of whitespace-delimited words in *text*.

    Punctuation is treated as part of a word. Empty or whitespace-only text
    has a word count of zero.

    Raises:
        TypeError: If ``text`` is not a string.
    """
    return len(normalize_whitespace(text).split())


def is_palindrome(
    text: str,
    *,
    ignore_case: bool = True,
    alphanumeric_only: bool = True,
) -> bool:
    """Return whether *text* reads the same forward and backward.

    By default, comparison is case-insensitive and ignores punctuation,
    whitespace, and other non-alphanumeric characters. Set either keyword
    option to ``False`` to include that aspect in the comparison.

    Raises:
        TypeError: If ``text`` is not a string or either option is not bool.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(ignore_case, bool):
        raise TypeError("ignore_case must be a bool")
    if not isinstance(alphanumeric_only, bool):
        raise TypeError("alphanumeric_only must be a bool")

    candidate = text.casefold() if ignore_case else text
    if alphanumeric_only:
        candidate = "".join(character for character in candidate if character.isalnum())
    return candidate == candidate[::-1]


def calculate_average(values: Iterable[Real]) -> float:
    """Return the arithmetic mean of a non-empty iterable of finite numbers.

    The iterable is consumed once, so generators are supported. Booleans are
    rejected even though Python treats them as integers.

    Raises:
        TypeError: If ``values`` is not iterable or contains a non-real value.
        ValueError: If ``values`` is empty or contains a non-finite number.
    """
    try:
        iterator = iter(values)
    except TypeError as exc:
        raise TypeError("values must be an iterable of real numbers") from exc

    total = 0.0
    count = 0
    for value in iterator:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("values must contain only real numbers (not bool)")
        number = float(value)
        if not math.isfinite(number):
            raise ValueError("values must contain only finite numbers")
        total += number
        count += 1

    if count == 0:
        raise ValueError("values must not be empty")
    return total / count
