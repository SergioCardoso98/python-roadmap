from Cookie import CookieBox

# Create a CookieBox for Oreo with 4 cookies and nutrition score 'F'
oreo_box = CookieBox('Oreo', 4, 'F')

# Create a CookieBox for Tuc with 20 cookies and nutrition score 'D'
tuc_box = CookieBox('Tuc', 20, 'D')

# Eat 5 cookies from the Tuc box
tuc_box.eat_cookies(5)

# Print the current state of the Tuc box
# This triggers the __str__() dunder method internally,
# which defines how the object is represented as a string for users
print(tuc_box)  # Output: Box of Tucs with 15 left

# Print the current state of the Oreo box
# Also triggers the __str__() method
print(oreo_box)  # Output: Box of Oreos with 4 left

# Using the + operator between two CookieBox objects
# This calls the __add__() dunder method, which defines the behavior of the + operator for CookieBox instances
print(tuc_box + oreo_box)  # Output: Tuc Oreo

# Print the official representation of the Tuc box object
# This calls the __repr__() dunder method, which provides a detailed, developer-oriented string useful for debugging
print(repr(tuc_box))

# Print the official representation of the Oreo box object
print(repr(oreo_box))


# -------------------------------------------------------------------
# DUNDER METHODS EXPLAINED IN DETAIL:
#
# Dunder methods, short for "double underscore methods," are special methods in Python classes.
# They have names surrounded by double underscores, like __init__, __str__, __repr__, __add__, etc.
#
# These methods allow your objects to interact with built-in Python operations and functions,
# letting you customize how your class behaves in different contexts.
#
# Examples in this code:
#
# 1) __init__(self, ...):
#    - The constructor method that runs when you create a new object.
#    - Sets up initial attributes.
#
# 2) __str__(self):
#    - Defines the "informal" string representation of the object.
#    - Called by print() and str() functions.
#    - Meant to be user-friendly and readable.
#
# 3) __repr__(self):
#    - Defines the "official" string representation of the object.
#    - Used in debugging and by the repr() function.
#    - Should ideally provide enough detail to recreate the object.
#
# 4) __add__(self, other):
#    - Defines the behavior of the + operator when used between two objects of your class.
#    - Can be customized however you want; here, it returns a combined string of brands.
#
# Why use dunder methods?
# - They make your objects integrate naturally with Python syntax.
# - Allow your objects to work with built-in functions and operators.
# - Improve readability and usability of your custom classes.
#
# When you do something like:
#   print(tuc_box)
# Python internally calls:
#   tuc_box.__str__()
#
# When you do:
#   tuc_box + oreo_box
# Python internally calls:
#   tuc_box.__add__(oreo_box)
#
# When you call:
#   repr(tuc_box)
# Python internally calls:
#   tuc_box.__repr__()
#
# Understanding and implementing dunder methods is a key part of mastering Python OOP!
# -------------------------------------------------------------------
