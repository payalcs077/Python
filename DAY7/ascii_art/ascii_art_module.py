# ascii_art_module.py

import pyfiglet


def ascii_art(text, font):
    """
    Generates ASCII art for the given text and font.
    
    Parameters:
    text (str): Text to convert into ASCII art
    font (str): Font style for ASCII art
    
    Returns:
    str: ASCII art string
    """
    return pyfiglet.figlet_format(text, font=font)



