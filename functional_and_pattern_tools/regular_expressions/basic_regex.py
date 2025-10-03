import re

# Sample string to test regex patterns on
test_string = (
    "Hello, old World! 12345 \n"
    "Tabs\tand spaces    \r\n"
    "Special chars: .^$*+?{}[]\\|() "
    "Unicode: café, naïve, résumé, 🐍🚀"
)

print('String that will be searched:\n')
print(f'{test_string}\n')

# Explanation of raw strings (r""):
# Normally, in Python strings, backslashes '\' introduce escape sequences.
# For example, "\n" means a newline character.
# Using a raw string like r"\n" tells Python to treat backslashes literally,
# which is especially useful in regex where '\' is very common.

# --- BASIC REGEX PATTERNS ---

print('Basic Patterns:')

# \w matches any "word" character: letters (a-z, A-Z), digits (0-9), or underscore (_).
match = re.search(r'\w', test_string)
print(f'    re.search(r"\\w", test_string) = {match.group()}')
# Finds the first word character in the string.

# \W matches any non-word character (anything except letters, digits, or underscore).
match = re.search(r'chars: \W\W\W', test_string)
print(f'    re.search(r"chars: \\W\\W\\W", test_string) = {match.group()}')
# Matches 'chars: ' followed by three non-word characters (in this case ": .^").

# . (dot) matches any character except newline '\n'.
match = re.search(r'.', test_string)
print(f'    re.search(r".", test_string) = {match.group()}')
# Matches the very first character in the string (which is 'H').

# \b matches a word boundary (the position between a word and a non-word character).
match = re.search(r'\bold\b', test_string)
print(f'    re.search(r"\\bold\\b", test_string) = {match.group()}')
# Matches the exact word "old" with word boundaries on both sides.

# \s matches any whitespace character (space, tab, newline, return, form feed).
match = re.search(r'Tabs\s', test_string)
print(f'    re.search(r"Tabs\\s", test_string) = {match.group()}')
# Matches "Tabs" followed by a whitespace (in this case, a tab).

# \S matches any non-whitespace character.
match = re.search(r'\Sllo', test_string)
print(f'    re.search(r"\\Sllo", test_string) = {match.group()}')
# Matches any non-whitespace character followed by "llo".
# Finds "Hello" because 'H' is non-whitespace.

# Matching a tab character literally:
match = re.search(r'Tabs\t', test_string)
print(f'    re.search(r"Tabs\\t", test_string) = {match.group()}')

# Matching a newline character literally:
match = re.search(r'45 \n', test_string)
print(f'    re.search(r"45 \\n", test_string) = {match.group()}')

# Matching a carriage return '\r' literally:
match = re.search(r'spaces    \r', test_string)
print(f'    re.search(r"spaces    \\r", test_string) = {match.group()}')

# \d matches any decimal digit (0-9).
match = re.search(r'World! \d', test_string)
print(f'    re.search(r"World! \\d", test_string) = {match.group()}')

# ^ matches the start of the string.
match = re.search(r'^Hello', test_string)
print(f'    re.search(r"^Hello", test_string) = {match.group()}')

# $ matches the end of the string.
match = re.search(r'🐍🚀$', test_string)
print(f'    re.search(r"🐍🚀$", test_string) = {match.group()}')
