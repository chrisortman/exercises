# Programming Exercise 7-2
#
# Program to display a list of random integers.
# This program takes no input,
# it loops through a list of integers and exchanges them for random integers,
# then displays the list on a single line.



# to use the random functions, import the random module
import random


# Define the main function
def main():
    # Initialize a list of integers.
    numbers = []

    # loop through the list
    for i in range(7):
        numbers.append(random.randint(0,9))
         # assigning a random integer to each member of the list

    # loop through the list
    for i in range(7):
        print(numbers[i], end="")
        if i < 6:
            print(', ', end='')
main()

        # display the current value

        
        # add a comma and space, unless this is the last value



# Call the main function.


