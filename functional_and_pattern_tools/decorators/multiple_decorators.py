#When you have multiple decorators applied to a single function in Python, they are applied from the bottom up (closest decorator to the function is applied first), 
#but when the function runs, the outermost decorator is the one that effectively wraps the others.

#def tldr():
#   print('Begin')
#       start_time = time.time()
#           print('main_func running')
#           time.sleep(1)
#       print(f'duration: {time.time() - start_time}')
#   print('End')

#main_func = decorator_announce(decorator_execution_time(main_func))

import time
def decorator_announce(func):
    def wrapper():
        print('Begin')
        func()
        print('End')
    return wrapper


def decorator_execution_time(func):
    def wrapper():
        start_time = time.time()
        func()
        print(f'duration: {time.time() - start_time}')
    return wrapper

@decorator_announce
@decorator_execution_time 
def main_func(): # main_func = decorator_announce(decorator_execution_time(main_func))
    print('main_func running')
    time.sleep(1)
main_func()


