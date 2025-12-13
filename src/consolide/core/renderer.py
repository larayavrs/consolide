import os
from ._component import Component

class Renderer:
    """Render orchestrator class, allows you to render multiple components as a single view."""

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def render(self, components: list[Component]) -> str:
        """
        Renders a collection of components
        
        Parameters
        ----------
        components : list[Component]
            Collection of components to render
        
        Returns
        -------
        str
            Rendered text combined from all components.
        """
        return "\n\n".join(component.render() for component in components)

    def refresh(self, components: list[Component]) -> None:
        self.clear()
        print(self.render(components))