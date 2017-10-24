# Programming Exercise 3-1
#
# Program to display the name of a week day from its number.
# This program prompts a user for the number (1 to 7)
# and uses it to choose the name of a weekday
# to display on the screen.

# Variables to hold the day of the week and the name of the day.
# Be sure to initialize the day of the week to an int and the name as a string.
day_of_week = 0
name_of_day = ""

# Get the number for the day of the week.
# be sure to format the input as an int
day_of_week = input("Enter the day number:: ")
day_of_week = int(day_of_week)

# Determine the value to assign to the day of the week.
# use a set of if ... elif ... etc. statements to test the day of the week value.
if day_of_week == 1:
    name_of_day = "Monday"
elif day_of_week == 2:
    name_of_day = "Tuesday"
elif day_of_week == 3:
    name_of_day = "Wednesday"
elif day_of_week == 4:
    name_of_day = "Thursday"
elif day_of_week == 5:
    name_of_day = "Friday"
elif day_of_week == 6:
    name_of_day = "Saturday"
elif day_of_week == 7:
    name_of_day = "Sunday"
else:
    name_of_day = "ERROR"

if name_of_day == "ERROR":
    print("That wasn't a valid day of the week eh")
else:
    print("You have chosen",name_of_day)




# use the final else to display an error message if the number is out of range.


# display the name of the day on the screen.




