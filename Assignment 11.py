"""
Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non-numeric input.
=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1.
"""

# Input below
# Prompt the user to enter a positive number

user_input = input("Enter a positive number: ")

# Check if this is an actual number and convert it
# Loop until you have a positive or valid number

while True:
    if user_input.isdigit():
        number = int(user_input)

        if number > 0: # If its a positive number then break
            break
        else:
            user_input = input("The number must be a positive number! Please try again")
    else:
        user_input = input("Invalid input. Please enter a positive number: ")


print("This is the calculation for the Collatz sequence! ")

while number != 1:
    print(number, end="  --> ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(1)

