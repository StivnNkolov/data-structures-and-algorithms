def factorial(n):
    assert n > 0 and type(n) == int, 'The number must be positive integer only!'
    if n == 1:
        return 1
    return n * factorial(n - 1)


result = factorial(2.4)
print(result)
