"""ANSI color and style helpers for Consolide.

This module centralizes ANSI escape sequence handling so components can
apply colors and text styles in a consistent way.
"""

from __future__ import annotations

from typing import Iterable, List, Optional

_FG_CODES = {
    "black": 30,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "white": 37,
}

_BG_CODES = {
    "black": 40,
    "red": 41,
    "green": 42,
    "yellow": 43,
    "blue": 44,
    "magenta": 45,
    "cyan": 46,
    "white": 47,
}


def style(
    text: str,
    *,
    fg: Optional[str] = None,
    bg: Optional[str] = None,
    bold: bool = False,
    italic: bool = False,
    underline: bool = False,
) -> str:
    """Wrap ``text`` in ANSI escape codes for the given style.

    Parameters
    ----------
    text:
        The text to style.
    fg, bg:
        Either a named color ("red", "green", etc.) or a raw ANSI code
        string like "31" / "41". ``None`` means no change.
    bold, italic, underline:
        When True, the corresponding text attribute is enabled.
    """

    codes: List[str] = []

    if fg is not None:
        if fg in _FG_CODES:
            codes.append(str(_FG_CODES[fg]))
        else:
            codes.append(str(fg))

    if bg is not None:
        if bg in _BG_CODES:
            codes.append(str(_BG_CODES[bg]))
        else:
            codes.append(str(bg))

    if bold:
        codes.append("1")
    if italic:
        codes.append("3")
    if underline:
        codes.append("4")

    if not codes:
        # ensure we do not accidentally leave stray styles active: explicitly
        # terminate any previous attributes at the end of the text.
        return f"{text}\x1b[0m"

    prefix = "\x1b[" + ";".join(codes) + "m"
    suffix = "\x1b[0m"
    return f"{prefix}{text}{suffix}"
