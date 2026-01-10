from dataclasses import dataclass

@dataclass(frozen=True)
class RenderContext:
    """Rendering constraints for a component.

    ``width`` and ``height`` describe the rectangular area (in characters)
    that the component may draw into.
    """

    width: int
    height: int

    @property
    def size(self) -> tuple[int, int]:
        """Return ``(width, height)`` for convenience when both are needed."""
        return self.width, self.height
