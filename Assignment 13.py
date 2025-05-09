"""
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

"""
# Input below
# Prompt the user to enter a string
text = input("Enter a word or phrase: ")

# Convert it to lowercase
text = text.lower()

# Set up palindrome
is_palindrome = True

# Use loop to compare characters from both ends
for i in range(len(text) // 2):
    if text[i] != text [-(i + 1)]:
        is_palindrome = False
        break

# Print the result
    if is_palindrome:
        print("Yes")
    else:
        print ("No")
