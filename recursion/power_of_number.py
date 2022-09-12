def power_of_number(base, exponent):
    assert exponent >= 1, 'Y must be integer number bigger than 1'
    if exponent == 1:
        return base
    return base * power_of_number(base, exponent - 1)


print(power_of_number(3, 0))
