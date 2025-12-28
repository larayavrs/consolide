"""
Consolide - Component module
============================

The Component module contains the base class for all components.
"""

from abc import ABC, abstractmethod
from consolide.terminal import Terminal

class ConsolideComponent(ABC):
    """This class is the base for all components"""

    def __init__(self, terminal: Terminal) -> None:
        self.terminal = terminal

    @abstractmethod
    def render(self) -> None:
        pass
    
    @abstractmethod
    def update(self) -> None:
        pass
    
    @abstractmethod
    def destroy(self) -> None:
        pass