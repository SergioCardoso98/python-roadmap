#A decorator in Python is a function or class that modifies the behavior of another function or method without changing its source code. 
#Decorators wrap a target function, allowing you to add functionality before or after it runs (like logging, timing, or access control). 
#They are applied using the @decorator_name syntax placed above a function definition. Under the hood, the decorator receives the original function as an argument and returns a new callable that replaces it. 
#Decorators are commonly used for code reuse, cleaner syntax, and separation of concerns in both simple scripts and large applications
import datetime
import random
import time

now = datetime.datetime.now()

def log(func):
    def wrapper():
        func()
        print(f'{func} was executed at {now}')
    return wrapper

def execution_time(func):
    def wrapper():
        exec_start = now
        func()
        print(f'{func} took {now - exec_start} to execute')
    return wrapper

def print_func_info(func):
    def wrapper():
        print(f"Function name: {func.__name__}")
        print(f"Docstring: {func.__doc__}")
        print(f"Defaults: {func.__defaults__}")
        print(f"Code object: {func.__code__}")
        print(f"Attributes (__dict__): {func.__dict__}")
        func()
    return wrapper

@log
@execution_time
@print_func_info
def execute():
    delay = random.uniform(1, 5)
    time.sleep(delay)
    print(f'I splept for {delay} seconds')

execute()