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
        child_width = usable_width // count

        child_ctxs = [
            RenderContext(child_width, ctx.height)
            for _ in self.children
        ]

        rendered = [
            child.render(child_ctx).splitlines()
            for child, child_ctx in zip(self.children, child_ctxs)
        ]

        lines = []
        for row in range(ctx.height):
            line_parts = []
            for block in rendered:
                line = block[row] if row < len(block) else ""
                line_parts.append(line.ljust(child_width))
            lines.append((" " * self.gap).join(line_parts))
        
        return "\n".join(lines)
    
    def update(self) -> None:
        for child in self.children:
            child.update()

    def destroy(self) -> None:
        for child in self.children:
            child.destroy()