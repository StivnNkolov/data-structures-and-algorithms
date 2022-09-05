def fibonacci(n):
    assert n >= 0 and type(n) == int, 'N must be positive integer number!'
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


result = fibonacci(4)
print(result)
