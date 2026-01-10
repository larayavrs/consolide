"""
Consolide - Spacer layout
=========================

A layout component that simply occupies space without rendering content.
Useful as a semantic separator in `Row` and `Column` layouts.
"""

from consolide.component import ConsolideComponent
from consolide.rendering import RenderContext


class Spacer(ConsolideComponent):
    """A layout component that renders an empty region.

    The component does not draw any visible characters, but when used inside
    other layouts it still participates in width/height distribution.

    The ``weight`` attribute is used by row/column layouts to decide how
    much of the available space this spacer should consume relative to
    other children.
    """

    def __init__(self, terminal, *, weight: int = 1) -> None:
        super().__init__(terminal)
        # Ensure a sane, positive integer weight.
        try:
            value = int(weight)
        except (TypeError, ValueError):
            value = 1
        self.weight: int = max(1, value)

    def render(self, ctx: RenderContext) -> str:
        if ctx.width <= 0 or ctx.height <= 0:
            return ""
        line = " " * ctx.width
        return "\n".join(line for _ in range(ctx.height))

    def update(self) -> None:
        pass

    def destroy(self) -> None:
        pass
