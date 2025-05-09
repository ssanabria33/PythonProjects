"""
Challenge: Use nested loop structures to print
the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.
=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a
pattern of asterisks (*) in the form of a right triangle.
"""

# Input below
# Prompt the user to develop a program that prompts the user to print a pattern of asterisks in the form of a right triangle

# Ask user for number of rows
rows = int(input("Enter the number of rows: "))

# Ask user for the character to use in the pattern
char = input("Enter the character to use for the pattern: ")

# Outer loop controls the number of rows
for i in range(1, rows + 1):
    # Inner loop prints the character 'i' times
    for j in range(i):
        print(char, end='')  # end='' keeps it on the same line
    print()  # moves to the next line after each row
