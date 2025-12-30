"""
Consolide - Label widget
=======================

Provides a basic text label component.
"""

from typing import Optional

from consolide.component import ConsolideComponent
from consolide.rendering import RenderContext

class Label(ConsolideComponent):
    """
    Basic text display component
    
    Attributes
    ----------
    terminal : Terminal
        The terminal to render the label to
    text : str
        The text to display
    align : Optional[str]
        The alignment of the text (either "left" or "right"), defaults to "left"
    """
    def __init__(self, terminal, text: str, *, align: Optional[str] = "left") -> None:
        super().__init__(terminal)
        self.text = text
        self.align = align
    
    def render(self, ctx: RenderContext) -> None:
        lines = self.text.splitlines()
        clipped = lines[:ctx.height]
        return "\n".join(line[:ctx.width] for line in clipped)
    
    def update(self) -> None:
        pass

    def destroy(self) -> None:
        pass