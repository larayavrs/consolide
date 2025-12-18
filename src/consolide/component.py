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
    def render(self):
        raise ConsolideNotImplemented("render method not implemented")
    
    @abstractmethod
    def update(self):
        raise ConsolideNotImplemented("update method not implemented")
    
    @abstractmethod
    def destroy(self):
        raise ConsolideNotImplemented("destroy method not implemented")