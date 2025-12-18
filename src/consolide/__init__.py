"""
consolide
=========

Consolide is a library for building interactive command line interfaces in
Python.
"""

import os

from .exceptions import *

# NOTE: By now Consolide is only compatible on Windows
if os.name != "nt":
    raise ConsolideUncompatibleSystem("Consolide is only compatible on Windows")

# TODO: add more things here in a future?