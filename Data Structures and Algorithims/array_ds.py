#fixed size
#only 1 data type

#why fixed size?
#it needs to know how much memory it needs to prevently alocate for itself


#only 1 data type
#to know where to read from the memory
#bool = 1 byte
#int = 2 bytes 
#for example

#in python all array nodes are sequencial in the memory - one next to the other

#Dynamic array
#unfixed syze 
# Dynamic array when we push a new value to the "array" under the hood will search for open space in the memory and allocates it, diferent languages might 
# do it diferent of each other, but that why its slower, more things the computer needs to do

#unfixed type
# JS will for example if [int, string, int] int = 2 bytes; string = 3bytes it will do "boxing" of the size, Meaning will alocate the ammount for all
#  entries in the array equal to the bigger, so it would alocate 9bytes (int=3, string=3, int=3), event though technically only need 7bytes 

import array
import sys

fixed_array = array.array('h', [10, 20, 30, 40]) # define the values and its data type
print("Fixed-size array (array module):", fixed_array)
print("Array typecode:", fixed_array.typecode)
print("Array length:", len(fixed_array))

for i, val in enumerate(fixed_array):
    obj_id = id(val)
    size = sys.getsizeof(val)  # size of the Python int object in bytes
    print(f"Element {i} = {val}, Id (memory address) = {hex(obj_id)}, Size of Python object = {size} bytes (0x{size:x})")

