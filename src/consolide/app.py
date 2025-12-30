"""
Consolide - Application and runtime module
==========================================

This module contains the application loop for Consolide.
"""

import time

from consolide.component import ConsolideComponent
from consolide.exceptions import ConsolideError
from consolide.terminal import Terminal
from consolide.rendering import RenderContext

class ConsolideApp:
    """
    This class contains the main application loop for Consolide.

    Attributes
    ===========
    root : ConsolideComponent
        The root component of the application.
    """
    def __init__(self, root: type[ConsolideComponent]) -> None:
        self.terminal = Terminal()
        self.root = root(self.terminal)
        self.running: bool = False
        self.__dirty: bool = True
        if hasattr(self.root, "terminal"):
            self.root.terminal = self.terminal

    def run(self) -> None:
        """Starts the application loop."""
        self.running = True
        try:
            self.terminal.clear()
            while self.running:
                self.update()
                if self.__dirty:
                    self.terminal.clear()
                    self.render()
                    self.__dirty = False                    
                # NOTE with this we can prevent the CPU hogging
                time.sleep(0.01)
        except KeyboardInterrupt:
            self.stop()
        except Exception as exc:
            raise ConsolideError(
                "Unhandled exception from the application"
            ) from exc
        finally:
            self.destroy()
    
    def stop(self) -> None:
        """Stops the application loop."""
        self.running = False

    def mark_dirty(self) -> None:
        """Marks the application state as needing to be redrawn."""
        self.__dirty = True
    
    def render(self) -> None:
        """Renders the application state."""
        width, height = self.terminal.size()
        ctx = RenderContext(width, height)
        output = self.root.render(ctx)
        if not isinstance(output, str):
            raise ConsolideError(
                f"{self.root.__class__.__name__}.render() must return str"
            )
        self.terminal.clear()
        self.terminal.write(output)

    def update(self) -> None:
        """Updates the application state."""
        self.root.update()
    
    def destroy(self) -> None:
        """Destroys the application state."""
        self.root.destroy()