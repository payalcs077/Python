from DAY7.package1.sanitization_script.sanitization import remove_html_chars, remove_space
from DAY7.package1.sanitization_script.sanitization import remove_char,help_menu

help_menu()

text = "<html>/Hello</html>"
cleaned = remove_html_chars(text)
print(cleaned)

text = "htmlhellohtml"
char = 'hello'
result = remove_char(char, text)
print(result)

text = 'hello world '
output = remove_space(text)
print(output)




