# from sanitization_script.sanitization import help_menu

# print(help_menu())

import pyfiglet

text = "HELLO"
ascii_art = pyfiglet.figlet_format(text)

print(ascii_art)

ascii_art = pyfiglet.figlet_format("PYTHON", font="slant")
print(ascii_art)
