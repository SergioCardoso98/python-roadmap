class FunctionsExecutionCounter:
    def __init__(self, func):
        # Store the original function inside the instance
        self.func = func  
        # Initialize a counter to track number of calls
        self.num_calls = 0

    # This makes the instance callable like a function
    # CURRENTLY: Accepts any arguments (*args, **kwargs)
    def __call__(self, *args, **kwargs):
        # Increment the call counter every time the function is called
        self.num_calls += 1
        print(f'This was printed {self.num_calls} times')
        # Call the original function with whatever arguments were passed
        return self.func(*args, **kwargs)  


@FunctionsExecutionCounter
def say_hi():
    print(f'Hi!')


# Call the decorated function multiple times
say_hi()
say_hi()
say_hi()


# -----------------------------------------------------------------
# Explanation of memory and function call behavior:
#
# When Python runs the @FunctionsExecutionCounter decorator on say_hi:
# - It creates an instance of FunctionsExecutionCounter with say_hi passed to __init__.
# - The say_hi name now refers to that instance, not the original function.
# - When say_hi() is called, it actually calls the instance's __call__ method. -> say_hi.__call__
# - __call__ increments num_calls and calls the original say_hi function stored in self.func.
#
# The instance keeps track of state (num_calls) between calls because it's stored in memory.
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# How to remove *args and **kwargs to make the decorator stricter:
#
# Instead of accepting any arguments, define __call__ with explicit parameters
# matching the wrapped function's signature.
#
# For example, if say_hi accepts one parameter 'name':
#
#     def __call__(self, name):
#         self.num_calls += 1
#         print(f'This was printed {self.num_calls} times')
#         return self.func(name)
#
# This makes the decorator less flexible but more strict about arguments.
# -----------------------------------------------------------------
