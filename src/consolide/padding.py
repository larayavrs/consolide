"""
Consolide - Padding layout
==========================

This module contains the padding layout component.
"""

from consolide.component import ConsolideComponent, SingleChildComponent
from consolide.rendering import RenderContext


class Padding(SingleChildComponent):
    """
    Padding is a layout wrapper that adds empty space around a single child
    component.

    It reduces the available rendering area passed to the child, while
    preserving the overall size of the parent RenderContext.

    Padding does NOT draw borders or decorations. It simply inserts blank
    space (spaces) around the content.

    Parameters
    ----------
    terminal : Terminal
        Reference to the terminal instance used by the application.
    child : ConsolideComponent
        The child component to wrap with padding.
    padding : int
        The number of empty lines to insert around the child.

    Characteristics:
    - Padding is uniform on all sides.
    - Outer dimensions remain unchanged.
    - Inner content is clipped if it exceeds available space.
    - Useful for improving visual spacing and readability.

    This component is often used together with Box, Column, or Row to
    improve layout aesthetics.
    """
    
    def __init__(self, terminal, child: ConsolideComponent, padding: int = 1):
        super().__init__(terminal, child)
        self.padding = padding

    def render(self, ctx: RenderContext) -> str:
        """
        Render the padded component.

        The child receives a reduced RenderContext that accounts for the
        padding on all sides.

        Parameters
        ----------
        ctx : RenderContext
            The RenderContext containing the available width and height.

        Returns
        -------
        str
            The rendered output of the padded component.
        """
        inner_width = ctx.width - self.padding * 2
        inner_height = ctx.height - self.padding * 2

        if inner_width <= 0 or inner_height <= 0:
            return " " * ctx.width * ctx.height

        child_ctx = RenderContext(inner_width, inner_height)
        content = self.child.render(child_ctx).splitlines()

        lines = []

        for _ in range(self.padding):
            lines.append(" " * ctx.width)

        for i in range(inner_height):
            line = content[i] if i < len(content) else ""
            padded = (
                " " * self.padding +
                line.ljust(inner_width) +
                " " * self.padding
            )
            lines.append(padded[:ctx.width])

        for _ in range(self.padding):
            lines.append(" " * ctx.width)

        return "\n".join(lines[:ctx.height])
    
    def update(self) -> None:
        """Update lifecycle hook.

        Delegates update calls to the wrapped child component.
        """
        self._update_child()

    def destroy(self) -> None:
        """Destroy lifecycle hook.

        Delegates destruction to the wrapped child component.
        """
        self._destroy_child()
