import re

_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")

def visible_length(text: str) -> int:
    """
    This calculate the large of visibility of text without ANSI sequences

    Parameters
    ----------
    text : str
        Text to measure

    Returns
    -------
    int
        Length of the visible text
    """
    return len(_ANSI_RE.sub("", text))