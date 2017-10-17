# -*- coding: UTF-8 -*-

# Programming Exercise 5-11
#
# Program to quiz a user with a random addition problem.
# This program uses a random function to generate addends for an addition problem,
#   calls a function to display the problem, passing the operands as arguments,
#   calls a second function to prompt the user for an answer to the problem,
# it calculates the correct answer,
# then passes the user answer and correct answer to a third function to evaluate the results,
#   and display whether the user was correct or not.



# to generate random numbers, import random module
import random


# define the main function
def main():
        # Define constant values for min addend and max addend
    MAX_ADDEND = 100
    MIN_ADDEND = 0

    # Define local int variables for addend 1, addend 2, user answer and correct answer
    addend_one = 0
    addend_two = 0
    user_answer = 0
    correct_answer = 0

    # Generate random integers for addend 1 and addend 2, with values from min to max
    # constants defined above
    addend_one, addend_two = generate_addends(min_value=MIN_ADDEND, max_value=MAX_ADDEND)

    # Call the function to display addition problem passing addend 1 and addend 2
    display_problem(addend_one, addend_two)
    # Assign the user answer to the result of calling the function to prompt for answer
    user_answer = prompt_for_answer()
    # Calculate correct answer
    correct_answer = calculate_correct_answer(addend_one, addend_two)
    # Call the function to evaluate answer, passing correct answer and user answer
    evaluate_answer(user = user_answer, correct = correct_answer)

def generate_addends(min_value, max_value):
    x = random.randint(min_value, max_value)
    y = random.randint(min_value, max_value)
    return x,y

# Define a function to display addition problem
# This function accepts two integer parameters, the addends,
# performs no calculations,
# but displays them, one above the other, aligned.
def display_problem(x, y):
    # print the first number in a field 5 characters wide
    print(format(x, "5d"))
    print("+", end="")
    print(format(y, "4d"))

        # print a + sign, followed by the second number in a field 4 characters wide


# Define a function to prompt a user for an answer and return it
# This function take no parameters,
# It prompts the user for an answer and casts it to an int,
# then returns the integer value
def prompt_for_answer():
    return int(input("Enter your answer: "))

def calculate_correct_answer(x, y):
    return x + y

# Define a function to evaluate the user's answer and display the evaluation
# This function takes correct answer and user answer as parameters
# if compares them to see if they match
# and displays a success or failure message to the user
def evaluate_answer(user, correct):
    if user == correct:
        print("ZOMG!!!! You got it 😃")
    else:
        print("Oh, that's too bad 🙁")
        # if correct answer equals user answer, display success message

        # else display failure message



# Call the main function to start the program
main()




