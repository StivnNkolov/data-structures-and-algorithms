import numpy as np

# How to find maximum product of two integers in the array where all elements are positive.
my_array = np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])


# O(n^2)
def find_maximum_product(array):
    current_product = 0
    # first_number_index = 0
    # second_number_index = 0
    first_number = 0
    second_number = 0

    for index in range(len(array)):
        for index2 in range(index, len(array)):
            if index == index2:
                continue
            temp_product = array[index] * array[index2]
            if temp_product > current_product:
                current_product = temp_product
                # first_number_index = index
                # second_number_index = index2
                first_number = array[index]
                second_number = array[index2]
    return f'Biggest product is {current_product} from numbers on index {first_number}, {second_number}'


print(find_maximum_product(my_array))
