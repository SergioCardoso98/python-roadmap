# -----------------------------------------------------------
# 🧠 PYTHON COMPREHENSIONS — COMPLETE CHEAT SHEET
# -----------------------------------------------------------
# General syntax pattern:
# [expression for item in iterable if condition]
# {expression for item in iterable if condition}    → set comprehension
# {key: value for item in iterable if condition}    → dict comprehension
#
# The "if" part is optional.
# -----------------------------------------------------------

# Base data for examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# -----------------------------------------------------------
# 1️⃣ BASIC LIST COMPREHENSION
# -----------------------------------------------------------
# Create a new list with doubled values
doubled = [n * 2 for n in numbers]
print("1️⃣ Doubled:", doubled)
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# -----------------------------------------------------------
# 2️⃣ LIST COMPREHENSION WITH CONDITION (IF)
# -----------------------------------------------------------
# Include only even numbers, then double them
even_doubled = [n * 2 for n in numbers if n % 2 == 0]
print("2️⃣ Even numbers doubled:", even_doubled)
# Output: [4, 8, 12, 16, 20]

# -----------------------------------------------------------
# 3️⃣ LIST COMPREHENSION WITH IF...ELSE
# -----------------------------------------------------------
# If even → double, else → triple
processed = [n * 2 if n % 2 == 0 else n * 3 for n in numbers]
print("3️⃣ Even→x2, Odd→x3:", processed)
# Output: [3, 4, 9, 8, 15, 12, 21, 16, 27, 20]

# -----------------------------------------------------------
# 4️⃣ NESTED LIST COMPREHENSION
# -----------------------------------------------------------
# Create all coordinate pairs (x, y)
coords = [(x, y) for x in range(3) for y in range(2)]
print("4️⃣ Coordinates:", coords)
# Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# -----------------------------------------------------------
# 5️⃣ DICTIONARY COMPREHENSION
# -----------------------------------------------------------
# Create a dict mapping number → its square
squares = {n: n**2 for n in numbers}
print("5️⃣ Squares dict:", squares)
# Output: {1:1, 2:4, 3:9, ..., 10:100}

# With condition
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print("5️⃣.5️⃣ Even squares dict:", even_squares)
# Output: {2:4, 4:16, 6:36, 8:64, 10:100}

# -----------------------------------------------------------
# 6️⃣ SET COMPREHENSION
# -----------------------------------------------------------
# Collect unique results (no duplicates)
evens_set = {n for n in numbers if n % 2 == 0}
print("6️⃣ Even set:", evens_set)
# Output: {2, 4, 6, 8, 10}

# -----------------------------------------------------------
# 7️⃣ COMPREHENSION USING A FUNCTION
# -----------------------------------------------------------
def transform(x):
    """Returns the number squared plus one."""
    return x**2 + 1

transformed = [transform(n) for n in numbers]
print("7️⃣ Function applied:", transformed)
# Output: [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]

# -----------------------------------------------------------
# 8️⃣ BAD PRACTICE WARNING ⚠️
# -----------------------------------------------------------
# Don’t use comprehensions just for side effects like printing.
# ❌ This is not recommended:
# [print(n) for n in numbers]
#
# ✅ Instead, use a normal loop:
# for n in numbers:
#     print(n)

# -----------------------------------------------------------
# ✅ Summary of what to study next:
# - list comprehensions with if / else
# - nested comprehensions
# - dict
