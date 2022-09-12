def sum_of_all_digits(n):
    assert n >= 0 and type(n) == int, "Number must be both positive and integer number"
    if n == 0:
        return n
    return n % 10 + sum_of_all_digits(n // 10)


print(sum_of_all_digits(-1))
