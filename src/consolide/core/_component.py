from abc import ABC, abstractmethod

class Component(ABC):
    """
    Base class for every renderizable components in Consolide

    Notes
    -----
    - Never prints directly to the console.
    - `render()` must be idempotent
    """

    @abstractmethod
    def render(self) -> str:
        """
        Renders the component
        
        Returns
        -------
        str
            Rendered component as a string
        """
        raise NotImplementedError

    def display(self) -> None:
        """Prints the component as stdout"""
        print(self.render())
