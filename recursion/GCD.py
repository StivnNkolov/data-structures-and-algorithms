def gcd(x, y):
    assert type(x) == int and type(y) == int, 'Both x and y must be positive integers.'
    if x < 0:
        x = -1 * x
    if y < 0:
        y = -1 * y

    if y == 0:
        return x
    return gcd(y, x % y)


print(gcd(48, 18))
