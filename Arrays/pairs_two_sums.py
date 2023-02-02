nums = [2, 7, 11, 15]  # target = 9
nums_2 = [3, 3, 2, 4]  # target = 6
nums_3 = [3, 3]  # target = 6


def find_pairs(array, target):
    for index in range(len(array) - 1):
        current_element = array[index]
        next_element = array[index + 1]

        if current_element + next_element == target:
            return index, index + 1
    return 'There is no such pairs in the array'


print(find_pairs(nums_2, 6))
