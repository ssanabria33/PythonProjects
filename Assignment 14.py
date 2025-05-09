"""
Challenge: Handle negative exponents efficiently.
====================================
Description: Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.
"""
 # Input below

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result = result * base
    return result
print(power(2,3))
print(power(5,0))

def power(base, exponent):
    result = 1
    if exponent >= 0:
        for _ in range(exponent):
            result = result * base
    else:
        for _ in range(-exponent):
            result = result * base
        result = 1 / result
    return result






