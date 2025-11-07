# -----------------------------------------------------------
# ⚙️ PYTHON GENERATOR EXPRESSIONS — COMPLETE CHEAT SHEET
# -----------------------------------------------------------
# General syntax pattern:
# (expression for item in iterable if condition)
#
# Very similar to list comprehensions — BUT uses () instead of [].
# → Creates a generator object that produces items *lazily* (one by one)
#   instead of creating a full list in memory.
#
# The "if" part is optional.
# -----------------------------------------------------------

# Base data for examples
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# -----------------------------------------------------------
# 1️⃣ BASIC GENERATOR EXPRESSION
# -----------------------------------------------------------
# Create a generator that doubles each number
doubled_gen = (n * 2 for n in numbers)
print("1️⃣ Generator object:", doubled_gen)
# Output: <generator object <genexpr> at ...>

# To see the values, iterate over it:
print("1️⃣ Doubled values:", list(doubled_gen))
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# ⚠️ Once converted to a list (or fully iterated), it's EXHAUSTED.
# Running list(doubled_gen) again would return [] (empty list).

# -----------------------------------------------------------
# 2️⃣ GENERATOR WITH CONDITION (IF)
# -----------------------------------------------------------
# Only include even numbers, then double them
even_doubled_gen = (n * 2 for n in numbers if n % 2 == 0)
print("2️⃣ Even doubled:", list(even_doubled_gen))
# Output: [4, 8, 12, 16, 20]

# -----------------------------------------------------------
# 3️⃣ GENERATOR WITH IF...ELSE
# -----------------------------------------------------------
# If even → double, else → triple
processed_gen = (n * 2 if n % 2 == 0 else n * 3 for n in numbers)
print("3️⃣ Even→x2, Odd→x3:", list(processed_gen))
# Output: [3, 4, 9, 8, 15, 12, 21, 16, 27, 20]

# -----------------------------------------------------------
# 4️⃣ USING next() TO FETCH ITEMS ONE BY ONE
# -----------------------------------------------------------
# Generators produce items lazily — one at a time.
lazy_gen = (n ** 2 for n in numbers)

print("4️⃣ First item:", next(lazy_gen))  # 1
print("   Second item:", next(lazy_gen)) # 4
# You can keep calling next() until it’s exhausted (StopIteration raised)

# -----------------------------------------------------------
# 5️⃣ MEMORY EFFICIENCY DEMO
# -----------------------------------------------------------
import sys

nums_list = [n * 2 for n in range(1000000)]   # Big list
nums_gen  = (n * 2 for n in range(1000000))   # Generator

print("5️⃣ List size (bytes):", sys.getsizeof(nums_list))
print("5️⃣ Generator size (bytes):", sys.getsizeof(nums_gen))
# Output example:
# List size: ~8,000,000 bytes
# Generator size: ~100 bytes ⚡

# -----------------------------------------------------------
# 6️⃣ USING GENERATORS IN A LOOP
# -----------------------------------------------------------
# Perfect for streaming or large data processing
for val in (n for n in numbers if n % 3 == 0):
    print("6️⃣ Multiple of 3:", val)
# Output:
# 3️⃣ Multiple of 3: 3
# 6️⃣ Multiple of 3: 6
# 9️⃣ Multiple of 3: 9

# -----------------------------------------------------------
# 7️⃣ USING GENERATOR WITH FUNCTIONS (e.g., sum, max, min)
# -----------------------------------------------------------
# Many built-in functions can consume generators directly
total = sum(n for n in numbers if n % 2 == 0)
print("7️⃣ Sum of even numbers:", total)
# Output: 30

# -----------------------------------------------------------
# 8️⃣ NESTED GENERATOR EXPRESSIONS
# -----------------------------------------------------------
# Create coordinate pairs (x, y)
coords_gen = ((x, y) for x in range(3) for y in range(2))
print("8️⃣ Coordinates:", list(coords_gen))
# Output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

# -----------------------------------------------------------
# 9️⃣ BAD PRACTICE WARNING ⚠️
# -----------------------------------------------------------
# ❌ Don’t use generators for side effects like printing:
# (print(n) for n in numbers)
#
# ✅ Use a normal for-loop instead:
# for n in numbers:
#     print(n)

# -----------------------------------------------------------
# ✅ Summary of what to remember:
# - Generator expressions use () instead of []
# - They produce items lazily (one at a time)
# - More memory-efficient for large data
# - Can be used directly in loops or functions like sum(), max(), etc.
# - Once used, they’re exhausted and can’t be reused
# -----------------------------------------------------------
