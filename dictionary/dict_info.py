"""
Dictionary is collection which is unordered, changeable and indexed.
Key:Value
"""
# Creating dictionary.
my_dict = {1: 'one', 2: 'two'}
my_dict_2 = dict()

# Access dict items
one = my_dict[1]  # O(1)
two = my_dict[2]
one_int = 1
smt = my_dict[one_int]

"""
Dictionaries in memory:
Python dictionaries are implemented using hash tables. It is an array whose indexes are obtained using a hash 
function on the keys.
A hash table is a way of doing key-value lookups. You store the values in an array, and then use a hash function to find
the index of the array cell that corresponds to your key-value pair. A hash function maps a key to a hash value and then
and index of the array.
There are three main elements in hash tables - the keys, the array and the hash function.
If the hash function returns the same index for different keys, it will create something like linked list in the memory.
"""

# Update/add and element to the dictionary. O(1)/Amortized O(n)
my_dict[3] = 'three'
my_dict[1] = 'uno'

# Traverse dictionary O(n)

# Traverse the keys
for key in my_dict:
    print(key)

for key in my_dict.keys():
    print(key)

# Traverse the values
for value in my_dict.values():
    print(value)

# Traverse key/value pairs
for key, value in my_dict.items():
    print(key, value)

# Delete element from dictionary. O(1)/Amortized O(n)
# POP = remove the value and returns it.
three = my_dict.pop(3)
# popitem() = remove and return the key and the value that you removes. Random.
# clear() = delete all pairs.
# del keyword = delete any pair from the dictionary. Calling __del__ on the obj.


# Dictionary methods
methods_dict = {
    'name': 'Edy',
    'age': 26,
    'address': 'London',
    'education': 'master'
}

# clear() = delete all pairs / return none.
# copy() = return shallow copy of the dict. Don't change the original dict.

new_dict = methods_dict.fromkeys(methods_dict.keys(), 0)

