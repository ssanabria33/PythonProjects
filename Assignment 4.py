"""
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
"""

# input below

x1 = float(input("Enter x1 coordinates: "))
y1 = float(input("Enter y1 coordinates: "))
x2 = float(input("Enter x2 coordinates: "))
y2 = float(input("Enter y2 coordinates: "))

# processing below:
# calculate the power of sections first

dx_squared = (x2 - x1) ** 2
dy_squared = (y2 - y1) ** 2

# add the squared sections together
distance_squared = dx_squared + dy_squared

# apply the sqrt for the distance squared
distance = distance_squared ** 0.5

# output
print (f"The distance between two points is: {distance}")
print("The distance between two points is: ", distance)