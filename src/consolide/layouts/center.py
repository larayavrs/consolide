"""
Consolide - Center layout
=========================

Convenience layout that centers a single child both horizontally and
vertically within the available area.
"""

from consolide.component import ConsolideComponent, SingleChildComponent
from consolide.rendering import RenderContext
from consolide.layouts.align import Align


class Center(SingleChildComponent):
    """Center a single child component within the available area.

    This is a thin wrapper around :class:`Align` configured with
    ``horizontal="center"`` and ``vertical="middle"``.
    """

    def __init__(self, terminal, child: ConsolideComponent) -> None:
        super().__init__(terminal, child)

    def render(self, ctx: RenderContext) -> str:
        if self.child is None:
            return ""
        # delegate the actual centering math to Align.
        aligned = Align(
            self.terminal,
            self.child,
            horizontal="center",
            vertical="middle",
        )
        return aligned.render(ctx)

    def update(self) -> None:
        self._update_child()

    def destroy(self) -> None:
        self._destroy_child()