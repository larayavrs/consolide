from consolide.core._component import Component

class Input(Component):
    """Input component for getting user input."""
    
    def __init__(self, prompt: str) -> None:
        self.prompt = prompt
        self.value: str | None = None
    
    def ask(self) -> str:
        """Asks the user for input outside of the render"""
        self.value = input(self.prompt)
        return self.value

    def render(self) -> str:
        """
        Renders the input component with the current value

        Returns
        -------
        str
            Rendered input component with the current value
        """
        if self.value is None:
            return ""
        return f"{self.prompt} {self.value}"