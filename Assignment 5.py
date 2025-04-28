"""
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
"""

# prompt the user to enter a time duration in hours
hours= float(input("Enter time duration in hours (non-negative number): "))

# check if the input is non negative
if hours < 0:
    raise ValueError ("Time duration must be a non-negative number.")

# processing: Convert hours to minutes and seconds
minutes = hours * 60
seconds = minutes * 60

# output display the converted time duration in minutes and seconds
print(f"{hours} hours is equal to {int(minutes)} minutes and {int(seconds)} seconds.")