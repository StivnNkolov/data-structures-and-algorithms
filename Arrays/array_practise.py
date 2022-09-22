from array import *

# 1. Create an array and traverse.
print('Step 1:')
test_array = array('i', [1, 2, 3, 4, 5])  # TC O(1)
for el in test_array:  # TC O(n)
    print(el)

# 2. Access individual elements through indexes
print('Step 2:')  # TC O(1)
print('element with index 0:', test_array[0])
print('using negative indexes (index -1):', test_array[-1])

# 3. Append any value to the array using append() method
# print('Step 3:') # TC O(1)
# print('Initial array:', test_array)
# test_array.append(0)
# print('Array after append:', test_array)

# 4. Insert value in an array using insert() method
# print('Step 4:') # TC O(n)
# print('Initial array:', test_array)
# test_array.insert(0, 100)
# print('Array after insert:', test_array)

# # 5. Extend python array using extend() method
# # If we try to extend with array containing different data types than the initial we get TypeError.
# print('Step 5:')  # TC O(n)
# print('Initial array:', test_array)
# array_to_add = array('i', [6, 7, 8])
# test_array.extend(array_to_add)
# print('Array after extend:', test_array)

# # 6. Add items from list into array using fromlist() method
# print('Step 6:') TC O(n)
# python_list = [10, 100, 1000]
# print('Initial array:', test_array)
# test_array.fromlist(python_list)
# print('Array after extend from list:', test_array)

# # 7. Remove any array element using remove() method
# print('Step 7:') TC O(n)
# print('Initial array:', test_array)
# test_array.remove(1)
# print('Array after removing element:', test_array)
# # If we pass value that is not in the arr we get ValueError.
# If we have more than one same value remove() will remove only the first occurrence.

# # 8. Remove last array element using pop() method
# print('Step 8:') TC O(1)
# print('Initial array:', test_array)
# test_array.pop()
# print('Array after pop():', test_array)
# # Pop return the removed value.

# 9. Fetch any element through its index using index() method
print('Step 9:') # TC O(n)
print(test_array.index(1))

# 10. Reverse a python array using reverse() method
print('Step 10:') # TC O(n)
print(test_array.reverse())

# 11. Get array buffer information through buffer_info() method
print('Step 11:')  # TC O(1)
print(test_array.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print('Step 12:')  # TC O(n)
print(test_array.count(1))

# 13. Convert array to string using tostring() method
print('Step 13:')
print(test_array.tostring())

# 14. Convert array to a python list with same elements using tolist() method
print('Step 14:')  # TC O(n)
converted_array = test_array.tolist()
print(converted_array)
"""
# 15. Slice Elements from an array

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[start:stop:step] # start through not past stop, by step

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
"""
