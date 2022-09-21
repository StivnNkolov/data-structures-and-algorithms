def find_biggest_number(input_array, array_len):
    if array_len == 1:
        return input_array[0]
    return max(input_array[array_len - 1], find_biggest_number(input_array, array_len - 1))


print(find_biggest_number([1, 5, 2, 15], 4))
