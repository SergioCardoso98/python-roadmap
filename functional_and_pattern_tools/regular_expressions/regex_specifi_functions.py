import re

# groups
test_string = 'abilio-fonseca@github.com'
match = re.search(r'[\w.-]@[\w.-]+',test_string)

print(match.group())