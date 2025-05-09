"""
Challenge: Optimize the function to handle large input numbers efficiently.
=====================================================
Description: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False otherwise
"""

# Input below

import math

def is_prime(number):
    # check if the number is at least 1
    if number <= 1:
        print("Not Prime")
        return

    # anything that's number 2 or 3 then its a prime
    if number <= 3:
        print("Prime")
        return

    # Eliminate even numbers and multiply of 3
    if number % 2 == 0 or number % 3 == 0:
        print("Not prime")
        return

    limit = math.isqrt(number)
    i = 5

    # Loop to check divisibility up to the sqrt of the number
    while i <= limit:
        if number % i == 0 or number % (i + 2) == 0:
            print("Not prime")
            return

    i += 6
    print ("Prime")

is_prime(100)

