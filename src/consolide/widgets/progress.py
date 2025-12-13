from consolide.terminal.size import terminal_size
from consolide.core._component import Component

class ProgressBar(Component):

    def __init__(self, total: int, label: str = "") -> None:
        self.total = total
        self.label = label
        self.__current = 0

    def tick(self, step: int = 1) -> None:
        self.__current = min(
            self.total, self.__current + step
        )
    
    def render(self) -> str:
        cols, _ = terminal_size()
        bar_width = min(40, cols - 20)
        percent = int((self.__current / self.total) * 100)
        filled = int(bar_width * percent / 100)
        bar = "█" * filled + " " * (bar_width - filled)
        return f"{self.label} [{bar}] {percent}%"