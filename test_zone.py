def test_function(func):
    print('tested the fucntion')
    func()
    return test_function


def main_function():
    print('Im the main function')

main_function = test_function(main_function)

main_function()

def decorator(func):
    def wrapper():
        print('Tested the function as a decorator')
        func()
    return wrapper

def main_execution():
    print('Im the main executor')

main_execution = decorator(main_execution)

main_execution()
