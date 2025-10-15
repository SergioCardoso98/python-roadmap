# A class in Python is a blueprint for creating objects (instances). 
# It defines a set of attributes and methods that the created objects will have

from Dog import Dog

print(dir(Dog))

golden_re = Dog("Roberto", "Golden Retreiver")
golden_re.print_self()