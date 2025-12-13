RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
UNDERLINE = "\033[4m"

def apply(text: str, *styles: str) -> str:
    """
    Applies ANSI styles to the text

    Parameters
    ----------
    text : str
        Text to apply styles to
    *styles : str
        ANSI sequences to apply to the text
    
    Returns
    -------
    str
        Text with styles applied
    """
    return f"{''.join(styles)}{text}{RESET}"