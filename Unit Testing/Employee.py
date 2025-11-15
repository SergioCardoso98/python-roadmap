class Employee:
    def __init__(self, name: str, age: int, salary: float) -> Employee:
        self.name = name
        self.age = age
        self.salary: float = float(salary)

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def  name(self, name_value: str):
        if not isinstance(name_value, str):
            raise ValueError("Name must be a string")
        if not all(c.isascii() and (c.isalpha() or c.isspace()) for c in name_value):
            raise ValueError("Only ASCII letters and spaces are allowed")
        self._name = name_value
        
    @property
    def age(self)-> int:
        return self._age
    @age.setter
    def  age(self, age_value: int):
        if isinstance(age_value, int):
            self._age = age_value
        else:
            raise ValueError('Only integers allowed')
        
    @property
    def salary(self)-> float:
        return self._salary
    @salary.setter
    def  salary(self, salary_value: int|float):
        try:
            self._salary = float(salary_value)
        except ValueError:
            raise ValueError('Only integers or floats allowed') 
                
    def salary_raise(self, raise_ammount: int|float):
        try:
            self.salary = self.salary + raise_ammount
        except TypeError:  
            raise TypeError('Only integers or floats allowed')
