from typing import List
from consolide.core._component import Component

class Row(Component):
    
    def __init__(self, components: list[Component], gap: int = 3) -> None:
        self.components = components
        self.gap = " " * gap

    def render(self) -> str:
        blocks: list[list[str]] = [
            component.render().splitlines()
            for component in self.components
        ]
        heights = [len(block) for block in blocks]
        max_height = max(heights, default=0)

        if max_height == 0:
            return ""

        for block in blocks:
            while len(block) < max_height:
                block.append("")

        lines: list[str] = []
        for row in range(max_height):
            lines.append(self.gap.join(block[row] for block in blocks))

        return "\n".join(lines)

class Column(Component):
    """
    Organize components in a horizontal column
    """
    
    def __init__(self, components: List[Component]) -> None:
        self.components = components
    
    def render(self) -> str:
        """
        Renders the components in a single column
        """
        return "\n\n".join(component.render() for component in self.components)

class Spacer(Component):
    """
    Invisible component which adds space
    """

    def __init__(self, height: int = 1) -> None:
        self.height = height
    
    def render(self) -> str:
        return "\n" * self.height