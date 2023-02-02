import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
target = 7


# print(target in my_array)

def find_number(array, searched_num):
    for el in array:
        if el == searched_num:
            return True
    return False


print(find_number(my_array, 33))
