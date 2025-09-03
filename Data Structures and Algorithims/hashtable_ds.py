#HASH TABLE = key-value lookup 
    #basically key has value
    #in python its a dictionary - dict

#Hashing function, it take the key, and it gives the index in the "array", so "mango" will be converted to dict[3] for example
dict_ = {
    "1": 1,     # key: string "1", value: int 1
    "2": "2"    # key: string "2", value: string "2"
}

print(dict_["1"])  # Output: 1
print(dict_["2"])  # Output: "2"