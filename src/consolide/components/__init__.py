"""Public UI components (widgets) exposed by Consolide.

This package groups leaf-level components (non-layout), such as labels.
"""

from .label import Label
from .text import Text
from .title import Title
from .subtitle import Subtitle
from .input import Input

__all__ = [
    "Label",
    "Text",
    "Title",
    "Subtitle",
    "Input",
]
