import re

# Sample string to test regex patterns on
test_string = ('Abilio..Fonseca@@@@@ctw.bmwgroup.com')

print('String that will be searched:\n')
print(f'{test_string}\n')

# --- REPETITION REGEX PATTERNS ---

print('Repetition Patterns:')

#+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
#* -- 0 or more occurrences of the pattern to its left
#? -- match 0 or 1 occurrences of the pattern to its left

match = re.search(r'\w+\w', test_string)
print(f'    re.search(r"\\w+\\w", test_string) = {match.group()}')

match = re.search(r'\w+\w\W?\W?\w*', test_string)
print(f'    re.search(r"\\w+\\w\\W?\\W?\\w*", test_string) = {match.group()}')

match = re.search(r'\w+\w\W?\W?\w*\W*', test_string)
print(f'    re.search(r"\\w+\\w\\W?\\W?\\w*\\W*", test_string) = {match.group()}')

match = re.search(r'\w+\w\W?\W?\w*\W*.*', test_string)
print(f'    re.search(r"\\w+\\w\\W?\\W?\\w*\\W*.*", test_string) = {match.group()}')

match = re.search(r'.@+.', test_string)
print(f'    re.search(r".@+.", test_string) = {match.group()}')