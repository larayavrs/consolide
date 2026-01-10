"""
Consolide - Container widget
============================

A container that groups multiple components.
"""

from typing import Iterable, List

from consolide.component import ConsolideComponent, MultiChildComponent
from consolide.rendering import RenderContext

class Container(MultiChildComponent):
    """
    A component that renders its children sequentially.

    Attributes
    ----------
    children : Iterable[ConsolideComponent]
        The children of the container component
    """
    
    def __init__(
        self,
        terminal,
        children: Iterable[ConsolideComponent] | None = None
    ) -> None:
        super().__init__(terminal, children)
    
    def add(self, component: ConsolideComponent) -> None:
        """
        Adds a child component to the container.

        Parameters
        ----------
        component : ConsolideComponent
            The component to add
        """
        self.children.append(component)
    
    def render(self, ctx: RenderContext) -> str:
        rendered = []
        remaining = ctx.height
        for child in self.children:
            if remaining <= 0:
                break
            child_ctx = RenderContext(ctx.width, remaining)
            output = child.render(child_ctx)
            lines = output.splitlines()
            remaining -= len(lines)
            rendered.append(output)
        return "\n".join(rendered)
    
    def update(self) -> None:
        for child in self.children:
            child.update()
    
    def destroy(self) -> None:
        for child in self.children:
            child.destroy()