"""
Consolide - Row component
=========================

This module contains the row, a component that groups multiple components horizontally.
"""

from typing import Iterable

from consolide.component import ConsolideComponent, MultiChildComponent
from consolide.rendering import RenderContext

class Row(MultiChildComponent):
    """
    A component that groups multiple components horizontally.

    Attributes
    ----------
    terminal : Terminal
        The terminal to render the row to
    children : Iterable[ConsolideComponent]
        The children of the row
    gap : int
        The gap between the children
    """
    def __init__(self, terminal, children: Iterable[ConsolideComponent] | None = None, gap: int = 1):
        super().__init__(terminal, children)
        self.gap = gap

    def render(self, ctx: RenderContext) -> str:
        if not self.children:
            return ""

        count = len(self.children)
        total_gap = self.gap * (count - 1)
        if total_gap >= ctx.width:
            return ""
        
        usable_width = ctx.width - total_gap

        # Compute per-child weights (defaulting to 1 when not present).
        weights: list[int] = []
        for child in self.children:
            w = getattr(child, "weight", 1)
            try:
                w_int = int(w)
            except (TypeError, ValueError):
                w_int = 1
            if w_int <= 0:
                w_int = 1
            weights.append(w_int)

        total_weight = sum(weights) or count

        # Allocate widths proportionally, taking care with rounding.
        remaining_width = usable_width
        remaining_weight = total_weight
        child_widths: list[int] = []

        for w in weights:
            if remaining_weight <= 0 or remaining_width <= 0:
                part = 0
            else:
                part = remaining_width * w // remaining_weight
            child_widths.append(part)
            remaining_width -= part
            remaining_weight -= w

        child_ctxs = [
            RenderContext(max(width, 0), ctx.height)
            for width in child_widths
        ]

        rendered = [
            (child.render(child_ctx).splitlines(), child_ctx.width)
            for child, child_ctx in zip(self.children, child_ctxs)
        ]

        lines = []
        for row in range(ctx.height):
            line_parts = []
            for block, width in rendered:
                if width <= 0:
                    line_parts.append("")
                    continue
                line = block[row] if row < len(block) else ""
                line_parts.append(line.ljust(width))
            lines.append((" " * self.gap).join(line_parts))
        
        return "\n".join(lines)
    
    def update(self) -> None:
        for child in self.children:
            child.update()

    def destroy(self) -> None:
        for child in self.children:
            child.destroy()