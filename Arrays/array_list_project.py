# # First task.
# def get_temperatures():
#     # TC O(n)
#     temperatures = []
#     number_of_days = int(input('How many day"s temperature? '))
#
#     for day in range(number_of_days):
#         current_day_temp = float(input(f"Day {day + 1}'s high temp: "))
#         temperatures.append(current_day_temp)
#
#     return temperatures
#
#
# def get_average_temp(temp_list):
#     # TC O(n)
#     average_temp = sum(temp_list) / len(temp_list)
#     print(f'Average = {average_temp}')
#     return average_temp
#
#
# def calculate_number_of_days_above_avg(temp_list, avg_tmp):
#     # TC O(n)
#     number_of_days_above_avg = len([el for el in temp_list if el > avg_tmp])
#     print(f'{number_of_days_above_avg} day(s) above average')
#
#
# temps = get_temperatures()
# avg_temp = get_average_temp(temps)
# calculate_number_of_days_above_avg(temps, avg_temp)


# # Task 2: Middle Function
# # Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
#
# def middle(lst):
#     return lst[1:len(my_list) - 1]
#
#
# my_list = [1, 2, 3, 4]
# print(middle(my_list))

# # Task 3: 2D Lists
# # Given 2D list calculate the sum of diagonal elements.
#
# my_list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
#
# def sum_diagonal(a):
#     diagonal_sum = 0
#     for row in range(len(a)):
#         diagonal_sum += a[row][row]
#     return diagonal_sum
#
#
# sum_diagonal(my_list_2D)

# # Task 4: Best Score
# # Given a list, write a function to get first, second best scores from the list.
# # List may contain duplicates.
#
# def first_second(given_list):
#     given_list.sort(reverse=True)
#     return given_list[0], given_list[1]
#
#
# my_list = [84, 85, 86, 87, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
# print(first_second(my_list))

# Task 5: Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100.
def missing_number(my_list, total_count):
    if my_list[-1] != total_count:
        return total_count
    elif my_list[0] != 1:
        return 1
    elif len(my_list) == total_count:
        return 'No missing number'

    for index in range(0, total_count):
        curr_number = my_list[index]
        next_number = my_list[index + 1]

        if curr_number + 1 != next_number:
            return curr_number + 1


print(missing_number([2, 3, 4, 5, 6], 6))  # 5


def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)


print(missingNumber([2, 3, 4, 5, 6], 6))

# Task 6: Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100.
