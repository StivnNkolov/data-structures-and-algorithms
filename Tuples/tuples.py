"""
A tuple is immutable sequence of Python objects.
Tuples are also comparable and hashable.
When we declare a tuple we cannot change it. That is the main difference between Tuples and Lists.
Hashable - object is hashable if it has a value that remains the same during its lifetime.
The elements of Tuple are located in the memory contiguously.

We generally use tuple for heterogeneous (different) data types and lists for homogeneous (similar) data types.
Iterating through a tuple is faster than list.
Tuples that contains immutable elements can be used as a key for a dictionary.
If we have data that doesn't change, we use tuple to guarantee that it remain write-protected.

"""

# Creating tuple
t = 1, 2, 3, 4, 5  # TC=O(1) SC=O(n)
t1 = (1, 2, 3, 4, 5)
t_with_one_element = (1,)  # Without the comma it will be considered string not tuple.
t2 = tuple('abcd')
print(type(t))
print(type(t1))
print(t2)

# Access tuple elements
print(t[1])
print(t[-1])
print(t[:2])
# t[1] = 'a'  # Not going to work.

# Traversing a tuple. TC=O(n) SC=O(1)
for el in t:
    print(el)

for index in range(len(t)):
    print(t[index])

# Search for element in tuple.
print(1 in t)  # TC=O(n) linear search.
print(t.index(2))  # If we try with value that is not in tuple it will throw value error. TC=0(n)


def search_in_tuple(input_tuple, searched_value):  # TC=O(n) SC=O(1)
    for index in range(0, len(input_tuple)):
        if input_tuple[index] == searched_value:
            return f'Element {searched_value} is found on index {index}.'
    return f'Element {searched_value} is not found.'


print(search_in_tuple(t, 10))

# Tuple operations/functions
test_tuple1 = (1, 2, 3, 4, 5)
test_tuple2 = (1, 2, 3, 4, 5)

print(test_tuple1 + test_tuple2)  # Return both tuples merged in one.
print(test_tuple1 * 4)
print(test_tuple1.count(1))  # return the count of element in tuple.
print(test_tuple1.index(1))  # return the index of the element in the tuple if exists.
print(len(test_tuple1))
print(max(test_tuple1))
print(min(test_tuple1))
tuple_from_list = tuple([1, 2, 3])  # converting list to tuple.

"""
Function that can be used for both list and tuple:
len(), max(), min(), sum(), any(), all(), sorted()

"""
