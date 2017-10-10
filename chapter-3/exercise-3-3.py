# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.
age = 0
category = ""

# Get the person's age.
# remember to convert the input to an int.
age = int(input("Enter your age in years plz:"))

# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.
if age >= 25:
    category = "Adult"
elif age >= 13:
    category = "Teenager"
elif age >= 3:
    category = "Child"
else:
    category = "Infant"





# display a message with the age category.
print("You are a(n)", category)


