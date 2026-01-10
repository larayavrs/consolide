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
    """

    def render(self, ctx: RenderContext) -> str:
        if ctx.width <= 0 or ctx.height <= 0:
            return ""
        line = " " * ctx.width
        return "\n".join(line for _ in range(ctx.height))

    def update(self) -> None:
        pass

    def destroy(self) -> None:
        pass