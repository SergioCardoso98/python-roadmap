# -------------------------------
# ITERABLES
# -------------------------------
# An iterable is any object you can loop over (like list, tuple, string, etc.)
# An object is iterable if it implements the __iter__() method.
# So __iter__() is just a special method that tells Python: “Here’s how to start looping over me.”
# It returns an iterator — an object that has a __next__() method and remembers where it is during looping.

nums = [1, 2, 3, 4, 5]

print("Iterating over 'nums' (a list):")
for num in nums:
    print(f"- {num}")

print("\nChecking methods on the list object:")
print(dir(nums))  # Lists are iterable — they have an __iter__ method

print("\n[INFO] In the background, the 'for' loop calls __iter__() on the object. And only then it uses the __next__()")

print("\n" + "#" * 30 + "\n")

# -------------------------------
# ITERATORS
# -------------------------------
# An iterator is an object with:
#   - __iter__() method → returns itself
#   - __next__() method → returns the next item and tracks the current state

print("Trying to use next() directly on 'nums':")
# 'nums' is iterable, but not an iterator — it has __iter__, but not __next__

try:
    print(next(nums))  # This will raise a TypeError
except Exception as e:
    print(f"[ERROR] Cannot call next() on list directly: {e}")

print("\n" + "#" * 30 + "\n")

# -------------------------------
# CONVERTING ITERABLE TO ITERATOR
# -------------------------------
print("Converting 'nums' to an iterator using nums_iter = nums.__iter__():")
nums_iter = nums.__iter__() # iter(nums) -> just a fancier way, under the hood does the __iner__() call
print(f"Methods of iterator object: {dir(nums_iter)}")

print("\nUsing next() to manually iterate:")
try:
    print(f"First item: {next(nums_iter)}")
    print(f"Second item: {next(nums_iter)}")
    print(f"Third item: {next(nums_iter)}")
    print(f"Fourth item: {next(nums_iter)}")
    print(f"Fifth item: {next(nums_iter)}")
    print(f"Sixth item: {next(nums_iter)}")
except StopIteration as e:
    print(f"[INFO] Reached end of iterator. Exception given: {e}")

print("\n[INFO] Once exhausted, an iterator cannot be reused — you must create a new one.")

print("\n" + "#" * 30 + "\n")

print("\nMaking a for loop using While loop")
try:
    print("Converting 'nums' again to an iterator using nums_iter2 = iter(nums):")
    nums_iter2 = iter(nums)
    counter = 1
    while True:
        print(f'{counter}º item: {next(nums_iter2)}')
except StopIteration as e:
    print(f"[INFO] Reached end of iterator2. Exception given: {e}")