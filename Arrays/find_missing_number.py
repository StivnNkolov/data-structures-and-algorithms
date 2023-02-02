arr = []
for number in range(2, 101):
    arr.append(number)

a = [1, 2, 3, 5, 6, 7]


# n = len(a)
#
# total = (n + 1) * (n + 2) / 2
# summ = sum(a)
# print(total - summ)

def find_missing(array):
    sum_1 = (len(array) + 1) * (len(array) + 2) / 2
    sum_2 = sum(array)
    print(sum_1 - sum_2)


find_missing(a)
