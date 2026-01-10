"""
Consolide - Column component
===========================

This module contains the column, a component that groups multiple components vertically.
"""

from __future__ import annotations
from typing import Iterable

from consolide.component import ConsolideComponent, MultiChildComponent
from consolide.rendering import RenderContext

class Column(MultiChildComponent):
    """
    Column is a layout component that arranges its children vertically,
    distributing the available height among them.

    Each child receives:
        - The full available width from the parent RenderContext.
        - A calculated height based on the total available height and the
      number of children.
    
    Optional vertical spacing (gap) can be added between children.

    Column does NOT draw borders, backgrounds, or visual decorations.
    It is purely a layout component responsible for spatial distribution.

    This component is typically used as a root layout or to structure
    sections of a terminal UI vertically.

    Parameters
    ----------
    terminal : Terminal
        Reference to the terminal instance used by the application.
    children : Iterable[ConsolideComponent]):
        A list or iterable of child components to render vertically.
    gap : int
        Number of empty lines inserted between each child. Defaults to 0.
    """

    def __init__(
        self, terminal, children: Iterable[ConsolideComponent] | None = None, gap: int = 0
    ) -> None:
        super().__init__(terminal, children)
        self.gap = gap

    def render(self, ctx: RenderContext) -> str:
        """
        Render the Column and its children within the given RenderContext.

        The available height is divided among children after accounting
        for gaps. Each child is rendered independently using its own
        RenderContext.

        Parameters
        ----------
        ctx : RenderContext
            The RenderContext containing the available width and height.

        Returns
        -------
        str
            The rendered output of the Column and its children.
        """
        if not self.children or ctx.height <= 0:
            return ""

        count = len(self.children)
        total_gap = self.gap * (count - 1)

        if total_gap >= ctx.height:
            return ""

        usable_height = ctx.height - total_gap

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

        # Allocate heights proportionally.
        remaining_height = usable_height
        remaining_weight = total_weight
        child_heights: list[int] = []

        for w in weights:
            if remaining_weight <= 0 or remaining_height <= 0:
                part = 0
            else:
                part = remaining_height * w // remaining_weight
            child_heights.append(part)
            remaining_height -= part
            remaining_weight -= w

        rendered_blocks = []
        for child, height in zip(self.children, child_heights):
            child_ctx = RenderContext(ctx.width, max(height, 0))
            output = child.render(child_ctx)
            rendered_blocks.append(output.splitlines())

        lines = []
        for block in rendered_blocks:
            lines.extend(block)
            lines.extend([" " * ctx.width] * self.gap)

        return "\n".join(lines[:ctx.height])

    def update(self) -> None:
        """
        Update lifecycle hook.

        Propagates the update call to all child components.
        """
        for child in self.children:
            child.update()

    def destroy(self) -> None:
        """
        Destroy lifecycle hook.

        Propagates the destroy call to all child components,
        allowing them to clean up resources if needed.
        """
        for child in self.children:
            child.destroy()