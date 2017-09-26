# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats
tract_size_feet = 0.0
number_of_acres = 0.0

# Constant for the number of square feet in an acre.
SQ_FEET_TO_ACRE = 43560

# Get the square feet in the tract from the user.
# you will need to convert this input to a float
tract_size_feet = input("Enter size of tract in square feet: ")
tract_size_feet = float(tract_size_feet)

# Calculate the number of acres.
number_of_acres = tract_size_feet / SQ_FEET_TO_ACRE

# Print the number of acres.
# remember to format the acres to two decimal places
print("There are ",format(number_of_acres,".2f")," acres", sep="")




