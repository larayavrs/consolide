"""Title component with a prominent style.

This is a convenience wrapper around Text with stronger defaults.
"""

from __future__ import annotations


from .text import Text


class Title(Text):
    """Prominent title text.

    By default, uses uppercase text, cyan color and bold style.
    """

    def __init__(self, terminal, text: str) -> None:

        super().__init__(terminal, text.upper(), bold=True)

