class Dog:
    def __init__(self, name, race):
        self.name = name
        self.race = race

    def print_self(self):
        print(f'Dog object at {self}')
        print(f'With the Dir: \n    {dir(self)}')