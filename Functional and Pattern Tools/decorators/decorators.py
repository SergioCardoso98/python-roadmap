#A decorator in Python is a function or class that modifies the behavior of another function or method without changing its source code. 
#Decorators wrap a target function, allowing you to add functionality before or after it runs (like logging, timing, or access control). 
#They are applied using the @decorator_name syntax placed above a function definition. Under the hood, the decorator receives the original function as an argument and returns a new callable that replaces it. 
#Decorators are commonly used for code reuse, cleaner syntax, and separation of concerns in both simple scripts and large applications


#context that will be needed for the explanation above
#The stack is temporary — it's used during the execution of a function call and then discarded.
#The heap is persistent — it's used for objects that may outlive a function call (which functions can).
#Cell object = a small box on the heap holding a reference to a variable that might be shared by multiple inner functions

#def my_func():
    #print("hello")
#Behind the scenes, Python creates a function object in the heap, with:
#The code (__code__)
#The name (__name__)
#Any defaults
#A reference to any closure cells if applicable (__closure__)


#Decorator is basicly is send a function to a function that will return an altered(decorated) function
#function = decorator(function)

from datetime import datetime
import inspect

def decorator_add_executed_at(function): #it will assign the function_sum with a new function (that will execute behaviour + original function_sum logic)
    value_to_later_multiply = 2
        # A value to demonstrate how variables move from the stack (where local variables normally live temporarily during function execution)
        # to the heap (stored inside closure cell objects of the returned function to persist after the outer function finishes)
    def wrapper(): #we need to build new function here and return it to function_sum, other wise decorator_add_executed_at would execute as soon as we decorate it
        print(f"{function.__name__}: started executing at", datetime.now()) # aditional behaviour that i want
        print(f'And the retained the value_to_later_multiply ({value_to_later_multiply} because since it still has a pointor to the memory address hasn\'t been cleaned up by the Pythons Garbage Coletor )')
            # Because the wrapper function references value_to_later_multiply, Python stores it in a closure cell object on the heap.
            # This allows the variable to persist even after the outer function's stack frame is destroyed.
            # The variable isn't copied; instead, the closure holds a reference (pointer) to its memory address.
            # As long as the closure exists, Python's garbage collector will not free that memory.
        result = function()
            # This is also why the wrapper can call the original function — it holds a reference to the original function object.
            # So the wrapped function retains the original logic plus the added behavior.
        return result # returns the function_sum() original logic after the wrapper logic being done
    return wrapper 
        # The decorator returns the wrapper function, which replaces the original function.
        # The new function includes additional behavior before and/or after calling the original function.

@decorator_add_executed_at # function_sum = decorator_add_executed_at(function_sum)
def function_sum():
    x = 1 +1 
    return x

result_to_print = function_sum()
print(f'result: {result_to_print}')
print(f'function_sum()/wrapper() retains the value_to_later_multiply var memory adress:')
if function_sum.__closure__:
    for i, cell in enumerate(function_sum.__closure__):
        print(f"Closure cell {i}:")
        print(f"    Memory address: {id(cell.cell_contents)}")
        print(f"    Type: {type(cell.cell_contents)}")
        print(f"    Value: {cell.cell_contents}")
else:
    print("No closure found")