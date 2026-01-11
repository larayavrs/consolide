"""Subtitle component with a softer style than Title.
"""

from __future__ import annotations


from .text import Text


class Subtitle(Text):
    """Secondary heading text.

    Defaults to magenta and not uppercased.
    """

    def __init__(self, terminal, text: str) -> None:
        super().__init__(terminal, text, bold=False)

