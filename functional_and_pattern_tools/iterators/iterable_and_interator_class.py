# -------------------------------
# CUSTOM ITERATOR CLASS EXAMPLE
# -------------------------------

# This is a custom iterator class that mimics Python's built-in `range()` function.
# It demonstrates how to make your own iterable + iterator in one class.
# 
# KEY FEATURES:
# - Implements __iter__() → returns self (makes it iterable)
# - Implements __next__() → returns next value in sequence and tracks state
# - Raises StopIteration when finished

class MyRange:
    def __init__(self, val, end_val):
        # val: starting value of the sequence
        # end_val: stopping value (non-inclusive, like range())
        self.value = val
        self.end = end_val

    def __iter__(self):
        # Makes this object an iterable
        # Returning self means this object is also its own iterator
        return self

    def __next__(self):
        # Called on each iteration (e.g., by next() or a for loop)
        if self.value >= self.end:
            # When we reach the end of the sequence, stop iteration
            raise StopIteration
        current = self.value
        self.value += 1  # Move to the next value
        return current

# -------------------------------
# USING THE CUSTOM ITERATOR
# -------------------------------

# Creating an instance of MyRange from 1 to 9 (end is non-inclusive)
sequence = MyRange(1, 10)

# Iterating using a for loop (under the hood uses __iter__ and __next__)
for n in sequence:
    print(n)

# OUTPUT:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# [INFO]
# After the loop, the iterator is exhausted.
# To iterate again, create a new MyRange instance.
