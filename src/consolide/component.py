"""
Consolide - Component module
============================

The Component module contains the base class for all components.
"""

from abc import ABC, abstractmethod
from .exceptions import *

class ConsolideComponent(ABC):
    """This class is the base for all components"""

    @abstractmethod
    def render(self) -> str: ...
    
    @abstractmethod
    def update(self) -> None: ...
    
    @abstractmethod
    def destroy(self) -> None: ...