"""
Consolide - Component module
============================

The Component module contains the base classes for all components.
"""

from abc import ABC, abstractmethod
from typing import Iterable, List, Optional

from consolide.terminal import Terminal
from consolide.rendering import RenderContext

from consolide.exceptions import ConsolideNotImplemented

class ConsolideComponent(ABC):
    """Base class for all Consolide components."""

    def __init__(self, terminal: Terminal) -> None:
        self.terminal = terminal

    @abstractmethod
    def render(self, ctx: RenderContext) -> str:
        """Render this component into a string buffer for the given context."""
        raise ConsolideNotImplemented
    
    @abstractmethod
    def update(self) -> None:
        """Update this component's internal state."""
        raise ConsolideNotImplemented
    
    @abstractmethod
    def destroy(self) -> None:
        """Release any resources held by this component."""
        raise ConsolideNotImplemented


class MultiChildComponent(ConsolideComponent):
    """Base class for components that manage a list of children.

    This is used by layout components like :class:`Row`, :class:`Column`,
    and :class:`Container` to share the same children management API.
    """

    def __init__(
        self,
        terminal: Terminal,
        children: Iterable[ConsolideComponent] | None = None,
    ) -> None:
        super().__init__(terminal)
        self.children: List[ConsolideComponent] = list(children or [])

    def add(self, component: ConsolideComponent) -> None:
        """Append a child component to this container."""
        self.children.append(component)

    def extend(self, components: Iterable[ConsolideComponent]) -> None:
        """Extend this container with multiple child components."""
        self.children.extend(components)

    def remove(self, component: ConsolideComponent) -> None:
        """Remove a child component from this container."""
        self.children.remove(component)

    def clear(self) -> None:
        """Remove all children from this container."""
        self.children.clear()


class SingleChildComponent(ConsolideComponent):
    """Base class for components that wrap a single child component.

    Used by layout wrappers such as :class:`Box`, :class:`Padding`,
    :class:`Align`, and convenience layouts like :class:`Center`.
    """

    def __init__(
        self,
        terminal: Terminal,
        child: Optional[ConsolideComponent] = None,
    ) -> None:
        super().__init__(terminal)
        self.child: Optional[ConsolideComponent] = child

    def set_child(self, child: ConsolideComponent) -> None:
        """Replace the wrapped child component."""
        self.child = child

    def _update_child(self) -> None:
        if self.child is not None:
            self.child.update()

    def _destroy_child(self) -> None:
        if self.child is not None:
            self.child.destroy()
