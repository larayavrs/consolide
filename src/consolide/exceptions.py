"""
Consolide - Exceptions module
==============================

In this module we define all the exceptions used in Consolide.
"""

class ConsolideException(Exception):
    """Base exception for Consolide."""
    pass

class ConsolideUncompatibleSystem(ConsolideException):
    """Exception raised when the operating system is not compatible with Consolide."""
    pass

class ConsolideUncompatibleTerminal(ConsolideException):
    """Exception raised when the terminal is not compatible with Consolide."""
    pass

class ConsolideError(ConsolideException):
    """Base exception for Consolide errors."""
    pass

class ConsolideDeprecated(ConsolideError):
    """Exception raised when a deprecated feature is used."""
    pass

class ConsolideNotImplemented(ConsolideError):
    """Exception raised when a feature is not implemented."""
    pass