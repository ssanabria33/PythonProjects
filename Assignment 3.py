"""
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).
===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
"""

# input below:
weight_input = input("Enter your weight in kilos: ")
height_input = input("Enter your height in meters: ")

# Convert the input variables to float
weight = float(weight_input)
height = float(height_input)

# processing below:
bmi = weight / (height ** 2)

#output below

print("The bmi is: ", bmi)