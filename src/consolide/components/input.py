"""Input component (display-only for now).

This component renders a single-line input field, optionally styled
according to focus state. It does not yet handle keyboard input; the
``value`` can be manipulated by external code.
"""

from __future__ import annotations

from typing import Optional

from consolide.ansi import style as ansi_style
from consolide.component import ConsolideComponent
from consolide.rendering import RenderContext


class Input(ConsolideComponent):
    """Simple single-line input field.

    Parameters
    ----------
    terminal : Terminal
        Target terminal instance.
    value : str
        Current value of the input.
    placeholder : str
        Text shown when value is empty.
    width : Optional[int]
        Fixed width for the input area. If None, uses the context width.
    """

    def __init__(
        self,
        terminal,
        *,
        value: str = "",
        placeholder: str = "",
        width: Optional[int] = None,
        fg: Optional[str] = None,
        placeholder_fg: Optional[str] = None,
        focused_fg: Optional[str] = None,
        focused: bool = False,
    ) -> None:
        super().__init__(terminal)

        self.value = value
        self.placeholder = placeholder
        self.width = width
        self.fg = fg if fg is not None else None

        self.placeholder_fg = placeholder_fg if placeholder_fg is not None else None
        self.focused_fg = focused_fg if focused_fg is not None else None

        self.focused = focused

    def render(self, ctx: RenderContext) -> str:
        if ctx.width <= 0 or ctx.height <= 0:
            return ""

        field_width = min(self.width or ctx.width, ctx.width)

        if self.value:
            raw = self.value
            color = self.focused_fg if self.focused and self.focused_fg else self.fg
        else:
            raw = self.placeholder
            color = self.placeholder_fg

        text = raw[: field_width].ljust(field_width)

        styled = ansi_style(
            text,
            fg=color,
            bold=self.focused,
        )

        lines = [styled]
        for _ in range(ctx.height - 1):
            lines.append(" " * ctx.width)
        return "\n".join(lines[: ctx.height])

    def update(self) -> None:
        pass

    def destroy(self) -> None:
        pass
