class FunctionsExecutionCounter:
    def __init__(self, func):
        self.func = func  # Store the original function

    def __call__(self, *args, **kwargs):
        print("Before")
        return self.func(*args, **kwargs)  # Call the original function



@FunctionsExecutionCounter
def say_hi(user_name,times):
    print(f'I said hi to {user_name} {times} time(s)')


say_hi('Abílio')
