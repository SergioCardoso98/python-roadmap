import re  # Import the regular expressions module

# Sample string containing an email-like pattern
test_string = 'abilio-fonseca@github.com'

# Use re.search to find the first substring in test_string that matches the pattern:
# Pattern breakdown:
# [\w.-]+    => Match one or more (+) characters that are either:
#               - word characters (letters, digits, underscore),
#               - dot ('.'),
#               - or dash ('-')
# @          => Match the '@' symbol literally
# [\w.-]+    => Match one or more (+) characters as above (the domain part)
match = re.search(r'[\w.-]+@[\w.-]+', test_string)

# If a match is found, print the matched substring
if match:
    print(match.group())
