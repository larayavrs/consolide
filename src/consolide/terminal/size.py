import shutil
from typing import Tuple

def terminal_size() -> Tuple[int, int]:
    """
    Gets the current terminal size
    
    Returns
    -------
    Tuple[int, int]
        Columns and rows of the terminal
    """
    size = shutil.get_terminal_size(
        fallback=(80, 24)
    )
    return size.columns, size.lines


def terminal_width() -> int:
    """
    Gets the current terminal width
    
    Returns
    -------
    int
        Width of the terminal
    """
    return terminal_size()[0]