
"""
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest
"""

# Prompt the user to enter the principle amount
principal =float(input("Enter the principal amount: "))

# prompt the user to enter the interest rate
rate = float(input("Enter the interest rate (in percentage): "))

# prompt the user to enter the time period
time = float(input(" Enter the time period: "))

# processing is below
simple_interest = (principal * rate * time) / 100

# output

print("the calculated interest rate is: ", simple_interest)