from array import *

'''
Create array
 1 Assign it to a variable
 2 Define the types of elements that it will store    
 3 Define the size (the maximum number of elements)
'''
print('Create array:')
int_array = array('i', [1, 2, 3, 4, 5, 6])  # In this case O(1) constant
double_array = array('d', [1.2, 4.6, 4.8])  # In this case O(1) constant
print(int_array)
# If we create empty list and assign values one by one the complexity is O(n)

# '''
# Insert in array
#  If array is full we have to make new array and add the new items O(n)
# '''
# print('Insert in array:')
# intArray.insert(6, 0)  # Insert at the end of array O(1)
# intArray.insert(0, 0)  # Insert at the start of array O(n)
# doubleArray.insert(3, 1.1)  # Insert at random position of array O(n)
# print(intArray)
# print(doubleArray)

# '''
# Array traversal
# '''
# print('Array traversal:')
#
#
# # Time complexity: O(n)
# # Space complexity: O(1)
# def traverse_array(input_arr):
#     for el in int_array:
#         print(el)
#
#
# traverse_array(int_array)

# '''
# Access array element
# '''
# print('Access array element:')
# print(int_array[0])  # Time complexity: O(1)
# print(int_array[-6])  # Time complexity: O(1)
#
#
# # Time complexity: O(1)
# # Space complexity: O(1)
# def access_element(input_array, index):
#     input_array_length = len(input_array)
#     if index not in range(-input_array_length, input_array_length):
#         print('List index out of range')
#     else:
#         print(input_array[index])
#
#
# access_element(int_array, 5)

'''
Find array element
'''
print('Find array element:')


# Time complexity: O(n)
# Space complexity: O(1)
def search_in_array(input_array, searched_element):
    for el in input_array:
        if el == searched_element:
            return True  # Time complexity: O(1)
        return 'There is no such element in the array.'


# Time complexity: O(n*2)
# Space complexity: O(1)
def search_in_array2(input_array, searched_element):
    for el in input_array:
        if el == searched_element:
            return f'Index position of element: {input_array.index(el)}'  # Time complexity: O(n)
        return 'There is no such element in the array.'


print(search_in_array(int_array, 20))


'''

'''
