# Global variables for this example (you could pass them dynamically too)
role = 'admin'      # This represents the user's role
language = 'pt'     # This represents the preferred language

def decorator_params_wrapper(role):
    #This outer function is called immediately when the decorator is applied.
    #It receives 'role' as a parameter and returns the actual decorator.
    def check_permissions_decorator(func):
        #This is the actual decorator.
        #It receives the original function and returns a new wrapped version of it.
        def wrapper(*args, **kwargs):
            #This is the wrapper that replaces the original function.
            #It adds behavior (permission check based on role) before calling the original function.
            if role == 'admin':
                # If allowed, pass True to the original function
                response = func(True, *args, **kwargs)
            else:
                # If not allowed, pass False to the original function
                response = func(False, *args, **kwargs)
            return response  # Return whatever the original function returns
        return wrapper  # Return the wrapped function
    return check_permissions_decorator  # Return the actual decorator


# When Python sees @decorator_params_wrapper(role), it immediately does:
# 1. decorator_params_wrapper('admin') → returns check_permissions_decorator
# 2. check_permissions_decorator(access_admin_dashboard) → returns wrapper
# So, access_admin_dashboard is now actually the 'wrapper' function.
# access_admin_dashboard = decorator_params_wrapper(role)(access_admin_dashboard)
#                                                         <---- this (access_admin_dashboard), runs the result of decorator_params_wrapper(role) which in this case is a func, if it was string for example it would crash
#                                                               TypeError: 'str' object is not callable
@decorator_params_wrapper(role)
def access_admin_dashboard(allowed, lang):
    if allowed:
        # If the user is allowed, return the appropriate message based on language
        if lang == 'pt':
            return 'Página do painel de administração'
        else:
            return 'Admin dashboard page'
    else:
        # If not allowed, return a 403 forbidden message
        return '403'

# - The 'allowed' argument is injected automatically by the decorator
res = access_admin_dashboard(language)

# Print the result
print(res)
