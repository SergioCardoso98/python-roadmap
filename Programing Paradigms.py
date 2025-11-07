# -------------------------------
# Imperative Programming
# -------------------------------
# This paradigm focuses on giving the computer a sequence of instructions
# that change the program's state step by step.
# Python supports this style with variables, loops, and control structures.

# Example of imperative programming:
x = 0  # Define a variable
for i in range(5):  # Loop to repeat actions
    x += i  # Update the variable step by step
print("Imperative result:", x)  # Output: 10


# -------------------------------
# Object-Oriented Programming (OOP)
# -------------------------------
# This paradigm is based on objects (data + behavior).
# Python supports OOP using classes, inheritance, and polymorphism.

# Example of OOP:
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Inheritance from Animal
    def speak(self):  # Polymorphism (override method)
        return "Woof!"

dog = Dog()
print("OOP result:", dog.speak())  # Output: Woof!


# -------------------------------
# Functional Programming
# -------------------------------
# This paradigm treats functions as first-class citizens,
# emphasizes pure functions, and avoids changing data (immutability).
# Python supports this using lambda functions, higher-order functions, etc.

# Example of functional programming:
nums = [1, 2, 3, 4, 5]

# Use map() and lambda (no explicit loops or mutable state)
squared = list(map(lambda n: n ** 2, nums))
print("Functional result:", squared)  # Output: [1, 4, 9, 16, 25]


# -------------------------------
# Aspect-Oriented Programming (AOP)
# -------------------------------
# This paradigm separates cross-cutting concerns (like logging or security)
# from the main program logic.
# Python doesn’t natively support AOP, but it can be done using decorators or libraries.

# Example using a decorator to simulate AOP:
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    return f"Hello, {name}!"

print("AOP result:", greet("Alice"))  # Output includes log + greeting
