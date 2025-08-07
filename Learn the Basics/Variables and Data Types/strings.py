#Strings are arrays

#Same thing
print("Hello")
print('Hello')

#" and '
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Multi lines
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

print('---------------------------')

#Slicing strings
b = "Hello, World!"
print(b[2:5]) # From 2 till 5 -> llo
b = "Hello, World!"
print(b[:5]) # Slice From the Start -> Hello
b = "Hello, World!"
print(b[2:])# Slice To the End  -> llo, World!
#Navigating indexes
b = "Hello, World!"
print(b[-5:-2])# with "-" -> orl ("World!" -5 = o) ("World!" -2 = d (not included))
b = "Hello, World!"
print(b[8:11])# same result as above
b = "Hello, World!"
print(b[8:-2])# same result as above
b = "Hello, World!"
print(b[8:-200])# empty (not Hello, Wo) just empty print
b = "Hello, World!"
print(b[0:200])# whole phrase

first_part = "Hello"
second_part = "World!"

#Concatenate
print(first_part + " " + second_part)#Hello World!

#We can also split with the .split methos and other things list bellow
#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isascii()	Returns True if all characters in the string are ascii characters
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle() 	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning

#Escape carachers
##\' 	Single Quote 	
#\\ 	Backslash 	
#\n 	New Line 	
#\r 	Carriage Return 	
#\t 	Tab 	
#\b 	Backspace 	
#\f 	Form Feed 	
#\ooo 	Octal value 	
#\xhh 	Hex value