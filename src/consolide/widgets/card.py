from consolide.core._component import Component
from consolide.terminal.size import terminal_size
from consolide.utilities.measure import visible_length

class Card(Component):
    """Card component visualization"""

    def __init__(self, title: str, lines: list[str], _max_width: int = 60):
        self.title = title
        self.lines = lines
        cols, _ = terminal_size()
        self.width = min(cols - 4, _max_width)
    
    def render(self):
        content = self.width - 2

        def line(txt: str) -> str:
            pad = content - visible_length(txt)
            return f"│{txt}{' ' * pad}│"

        top = f"┌{'─' * content}┐"
        sep = f"├{'─' * content}┤"
        bottom = f"└{'─' * content}┘"
        body = [line(t) for t in self.lines]

        return "\n".join([top, line(self.title.center(content)), sep, *body, bottom])
