# We can assign like this
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Also like this 
x = y = z = "Orange"
print(x)
print(y)
print(z)

#And like this
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
print('--------------------------------------')
#Text types
str_ = "Hello World"
print(f'{str_} is a {type(str_)}')

#Numeric types
int_ = 19
print(f'{int_} is a {type(int_)}')
float_ = 19.0
print(f'{float_} is a {type(float_)}')
complex_ = 19j
print(f'{complex_} is a {type(complex_)}')

#Sequence types
list_ = ["Math", "English", "Physics", "Chemistry"]
print(f'{list_} is a {type(list_)}')
tuple_ = ("Math", "English", "Physics", "Chemistry")
print(f'{tuple_} is a {type(tuple_)}')
range_ = range(4)
print(f'{range_} is a {type(range_)}')

#Mapping tyoe
dict_ = {"name" : "John", "age" : 36}
print(f'{dict_} is a {type(dict_)}')

#Set Types
set_ = {"apple", "banana", "cherry"}
print(f'{set_} is a {type(set_)}')
frozenset_ = frozenset({"apple", "banana", "cherry"})
print(f'{frozenset_} is a {type(frozenset_)}')

#Boolean Type
boolean_ = True
print(f'{boolean_} is a {type(boolean_)}')
boolean2_ = False
print(f'{boolean2_} is a {type(boolean2_)}')

#Binary Types
bytes_ = b"Hello"
print(f'{bytes_} is a {type(bytes_)}')
bytearray_ = bytearray(5)
print(f'{bytearray_} is a {type(bytearray_)}')
memoryview_ = memoryview(bytes(5))
print(f'{memoryview_} is a {type(memoryview_)}')

#None Type
none_ = None
print(f'{none_} is a {type(none_)}')
