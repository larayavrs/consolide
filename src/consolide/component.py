"""
Consolide - Component module
============================

The Component module contains the base class for all components.
"""

from abc import ABC, abstractmethod

from consolide.terminal import Terminal
from consolide.rendering import RenderContext

from consolide.exceptions import ConsolideNotImplemented

class ConsolideComponent(ABC):
    """This class is the base for all components"""

    def __init__(self, terminal: Terminal) -> None:
        self.terminal = terminal

    @abstractmethod
    def render(self, ctx: RenderContext) -> str:
        raise ConsolideNotImplemented
    
    @abstractmethod
    def update(self) -> None:
        raise ConsolideNotImplemented
    
    @abstractmethod
    def destroy(self) -> None:
        raise ConsolideNotImplemented