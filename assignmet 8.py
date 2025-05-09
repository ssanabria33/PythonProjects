"""
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.
=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.

"""
# input section below
# Ask the user to enter marks for three subjects
print("Please enter marks for three subjects (between 0 and 100).")

# input for Subject 1
subject1 = input("Enter marks for subject1: ")
if not subject1.isdigit() or not (0<= int(subject1) <=100):
    print("Invalid input for Subject 1. Please enter a number between 0 and 100.")
exit()

# input for Subject 2
subject2 = input("Enter marks for subject2: ")
if not subject2.isdigit() or not (0<= int(subject2) <=100):
    print("Invalid input for Subject 2. Please enter a number between 0 and 100.")
exit()

# input for Subject 3
subject3 = input("Enter marks for Subject3: ")
if not subject3.isdigit() or not (0<= int(subject3) <=100):
    print("Invalid input for Subject 3. Please enter a number between 0 and 100.")
exit()

# Convert inputs to integers
mark1 = int(subject1)
mark2 = int(subject2)
mark3 = int(subject3)

# Calculate average
average = (mark1 + mark2 + mark3) / 3

# Determine grade
if marks >= 90:
    print("A")
elif 80 <= marks <= 89:
    print("B")
elif 70 <= marks <= 79:
    print("C")
elif 60 <= marks <= 69:
    print("D")
elif marks < 60:
    print("F")

# Output the grade
print("Average marks:", round(average, 2))
print("Grade:", grade)