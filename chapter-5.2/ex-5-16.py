# Programming Exercise 5-16
#
# Program to compare the proportion of odd and even random integers.
# This program accepts no input.
# It uses a loop and the random library to generate 100 random integers,
# counts the number of odd and even results,
# and displays the total of each.



# To use the random integer function, import the random library
import random


# define the main function
def main():
    # define local int variable for number, odd and even totals
    number = 0
    odds = 0
    evens = 0

    # define a constant to hold how many numbers to compare (100)
    MAX_NUM = 100

    # loop through the range of numbers to compare
    for x in range(MAX_NUM):
        # get a random integer from the random library function
        number = random.randint(1,500)
        # if the check for even function returns true, increment even counter
        if is_even(number):
            evens += 1
        else:
            odds += 1
        # else increment odd counter.

    # display the results on the screen
    
    print("Odds: ", odds)
    print("Events ", evens)


# Define a function to check for even numbers
# This function accepts one integer parameter,
# uses the mod operater to see if can be evenly divided by two,
# and return true if it can, false it cannot
def is_even(num):
    # if dividing the number by two yields no remainder, return true
    return num % 2 == 0
    # else return false



# Call the main function to begin the program
main()

