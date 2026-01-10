"""
Consolide - Align layout
========================

Provides horizontal and vertical alignment for a single child component
within the available render area.
"""

from typing import Literal

from consolide.rendering import RenderContext
from consolide.component import ConsolideComponent, SingleChildComponent

HorizontalAlign = Literal["left", "center", "right"]
VerticalAlign = Literal["top", "middle", "bottom"]

class Align(SingleChildComponent):
    """
    Aligns a single child component within the available rendering area.

    This layout does not alter the child's content. Instead, it calculates
    the appropriate cursor offset before rendering the child, based on the
    desired horizontal and vertical alignment.

    Characteristics:
    - The child component is aligned within the available rendering area.
    - The child's content is not modified.

    Parameters
    ----------
    terminal : Terminal
        The terminal instance used for rendering.
    child : ConsolideComponent
        The component to align.
    horizontal : HorizontalAlign
        Horizontal alignment strategy. Default is "left".
    vertical : VerticalAlign
        Vertical alignment strategy. Default is "top".
    """

    def __init__(
        self, 
        terminal,
        child: ConsolideComponent,
        *,
        horizontal: HorizontalAlign = "left",
        vertical: VerticalAlign = "top",
    ) -> None:
        super().__init__(terminal, child)
        self.horizontal = horizontal
        self.vertical = vertical

    def render(self, ctx: RenderContext) -> str:
        """
        Render the child component aligned within the given render context.

        This implementation renders the child first and then repositions its
        buffer inside the available area, based purely on string dimensions.
        """
        if ctx.width <= 0 or ctx.height <= 0:
            return ""

        raw = self.child.render(RenderContext(ctx.width, ctx.height))
        if not raw:
            return ""

        child_lines = raw.splitlines()
        child_height = min(len(child_lines), ctx.height)
        child_width = min(max((len(line) for line in child_lines), default=0), ctx.width)

        # Horizontal alignment
        if self.horizontal == "center":
            offset_x = max((ctx.width - child_width) // 2, 0)
        elif self.horizontal == "right":
            offset_x = max(ctx.width - child_width, 0)
        else:
            offset_x = 0

        # Vertical alignment
        if self.vertical == "middle":
            offset_y = max((ctx.height - child_height) // 2, 0)
        elif self.vertical == "bottom":
            offset_y = max(ctx.height - child_height, 0)
        else:
            offset_y = 0

        blank_line = " " * ctx.width
        lines: list[str] = []

        # Top padding
        for _ in range(offset_y):
            lines.append(blank_line)

        # Content rows
        for row in range(child_height):
            line = child_lines[row][:child_width].ljust(child_width)
            padded = (
                " " * offset_x
                + line
                + " " * max(ctx.width - offset_x - child_width, 0)
            )
            lines.append(padded[:ctx.width])

        # Bottom padding
        while len(lines) < ctx.height:
            lines.append(blank_line)

        return "\n".join(lines[:ctx.height])

    def update(self) -> None:
        """Propagates update calls to the child component."""
        self._update_child()

    def destroy(self) -> None:
        """Propagates destroy calls to the child component."""
        self._destroy_child()
