"""Styled text component for Consolide.

This builds on top of the basic Label behavior but applies ANSI styles
(foreground/background colors, bold, italic, underline).
"""

from __future__ import annotations

from typing import Optional

from consolide.ansi import style as ansi_style
from consolide.rendering import RenderContext
from .label import Label


class Text(Label):
    """Styled text component.

    Parameters
    ----------
    terminal : Terminal
        Target terminal instance.
    text : str
        Text content.
    fg, bg : Optional[str]
        Named colors ("red", "green", etc.) or raw ANSI codes.
    bold, italic, underline : bool
        Style flags.
    """

    def __init__(
        self,
        terminal,
        text: str,
        *,
        fg: Optional[str] = None,
        bg: Optional[str] = None,
        bold: bool = False,
        italic: bool = False,
        underline: bool = False,
        align: Optional[str] = "left",
    ) -> None:
        super().__init__(terminal, text, align=align)
        self.fg = fg
        self.bg = bg
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def render(self, ctx: RenderContext) -> str:
        base = super().render(ctx)
        if not base:
            return ""
        return ansi_style(
            base,
            fg=self.fg,
            bg=self.bg,
            bold=self.bold,
            italic=self.italic,
            underline=self.underline,
        )
