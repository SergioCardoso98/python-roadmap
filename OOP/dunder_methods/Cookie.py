# Cookie.py

class CookieBox:
    def __init__(self, brand: str, n_cookies: int, nutricion_score: str):
        # Constructor method to initialize a CookieBox object
        # brand: the brand of the cookies (e.g., Oreo)
        # n_cookies: number of cookies initially in the box
        # nutricion_score: nutrition score of the cookies (e.g., 'F', 'D')
        self.brand = brand
        self.number_of_cookies = n_cookies
        self.nutricion_score = nutricion_score
    
    def eat_cookies(self, n_cookies: int):
        # Method to simulate eating cookies from the box
        # Reduces number_of_cookies by n_cookies
        # If n_cookies is negative, sets number_of_cookies to zero (guard clause)
        self.number_of_cookies -= n_cookies
        if n_cookies < 0: 
            self.number_of_cookies = 0

    def __str__(self) -> str:
        # dunder (double underscore) method __str__ defines
        # the string representation of the object when printed or str() is called
        # Usually user-friendly description
        return f'Box of {self.brand}s with {self.number_of_cookies} left'

    def __repr__(self) -> str:
        # dunder method __repr__ defines the official string representation,
        # mainly used for debugging and development
        # Should be unambiguous and ideally valid Python code to recreate the object
        return (f'CookieBox(brand:{self.brand}, number_of_cookies: {self.number_of_cookies}, '
                f'nutricion_score{self.nutricion_score})')
    
    def __add__(self, other: 'CookieBox'):
        # dunder method __add__ defines the behavior of the + operator
        # when used between two CookieBox objects
        # Here, returns a string combining the brands of the two boxes
        # Note: This is just a demonstration; you could also implement merging boxes, etc.
        return f'{self.brand} {other.brand}'
