#A lambda in Python is just a quick way to write a tiny function without using def. It’s often used when you only need the function once. 
#The syntax is lambda x: x + 1, which creates a function that adds 1 to whatever you give it. It works the same as a regular function but is written in one line.

add_one = lambda x: x + 1
print(add_one(5))  # Output: 6

#more usefull one would be

words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words, key=lambda word: len(word))
# Result: ['apple', 'banana', 'cherry']

