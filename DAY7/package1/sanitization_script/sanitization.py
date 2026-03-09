def help_menu():
    """
    This module has three functions
    Removes HTML related characters: < > /
    from the given string.
    """
    print(help_menu.__doc__)

# def remove_html_chars(text):
def remove_html_chars(text : str)-> str:
    remove_chars = "<>/"
    for ch in remove_chars:
        text = text.replace(ch, "")
    return text

def remove_char(cha_rem, text):
   return  text.replace(cha_rem,"")

def remove_space(text):
   return text.replace(" ", ",")

