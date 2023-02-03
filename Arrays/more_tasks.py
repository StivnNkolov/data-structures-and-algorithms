# my_list = [1, 2, 3, 4]
#
#
# def middle(input_array):
#     return input_array[1:len(input_array) - 1]
#
#
# print(middle(my_list))
import math

# input_matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
#
# def sum_diagonal(matrix):
#     result = 0
#     for index in range(len(matrix)):
#         result += matrix[index][index]
#     return result
#
#
# print(sum_diagonal(input_matrix))

# my_list = [84, 85, 90, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
#
#
# def find_first_second_best_scores(input_array):
#     array_copy = input_array[:]
#     array_copy.sort(reverse=True)
#     first = array_copy[0]
#     second = 0
#
#     for element in array_copy:
#         if element == first:
#             continue
#         second = element
#         break
#
#     return first, second
#
#
# print(find_first_second_best_scores(my_list))

# array = [1, 2, 3, 4, 6]
# n = 6
#
#
# def missing_number(input_array, input_array_len):
#     total = input_array_len * (input_array_len + 1) / 2
#     summm = sum(input_array)
#     return total - summm
#
#
# print(missing_number(array, n))

# input_array = [1, 1, 2, 2, 3, 4, 5]
#
#
# def remove_duplicate_numbers(array):
#     return list(set(array))
#
#
# print(remove_duplicate_numbers(input_array))

# Write a function to find all pairs of an integer array whose sum is equal to a given number.
input_array = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7


def pair_sum(array, input_target):
    pairs_array = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                pairs_array.append(f'{array[i]}+{array[j]}')
    return pairs_array


print(pair_sum(input_array, target))
