"""
Consolide - Terminal module
===========================

Low-level terminal abstraction development in Consolide.
"""

import os
import shutil
import sys

from consolide.exceptions import ConsolideUncompatibleTerminal

class TerminalManager:
    """This class handles terminal operations in a safe and unified way"""

    def __init__(self) -> None:
        if not sys.stdout.isatty():
            raise ConsolideUncompatibleTerminal(
                "The terminal is not compatible with Consolide. Standard output is not a TTY"
            )
    
    def _enable_ansi(self) -> None:
        """Enables ANSI escape sequences on Windows terminals"""
        if os.name == "nt":
            os.system("")
    
    def clear(self) -> None:
        """Clears the terminal screen"""
        sys.stdout.write("\x1b[2J\x1b[H")
        sys.stdout.flush()
    
    def move_cursor(self, row: int, col: int) -> None:
        """
        Moves the cursos to the given position

        Parameters
        ----------
        row : int
            The row to move the cursor to
        col : int
            The column to move the cursor to
        """
        sys.stdout.write(f"\x1b[{row};{col}H")
        sys.stdout.flush()

    def write(self, text: str) -> None:
        """
        Writes text to the terminal

        Parameters
        ----------
        text : str
            The text to write
        """
        sys.stdout.write(text)
        sys.stdout.flush()
    
    def writeln(self, text: str = "") -> None:
        """
        Writes text to the terminal and moves the cursor to the next line

        Parameters
        ----------
        text : str
            The text to write
        """
        sys.stdout.write(text + "\n")
        sys.stdout.flush()
    
    def size(self) -> tuple[int, int]:
        """
        Returns the size of the terminal

        Returns
        -------
        tuple[int, int]
            A tuple containing the width and height of the terminal
        """
        size = shutil.get_terminal_size()
        return size.columns, size.lines