# Is unique: Implement and algorithm to determine if a list has all unique characters, using python list

my_list = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]
unique_list = [1, 2]


def is_unique(array):
    working_list = []

    if not array:
        return 'Empty input list.'

    for element in array:
        if element in working_list:
            return False
        working_list.append(element)
    return True


print(is_unique(my_list))
print(is_unique(unique_list))
