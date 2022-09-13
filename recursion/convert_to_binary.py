def convert_to_binary(n):
    assert type(n) == int, 'The number must be integer number.'
    if n == 0:
        return 0
    return n % 2 + 10 * convert_to_binary(n // 2)


print(convert_to_binary(13.2))
