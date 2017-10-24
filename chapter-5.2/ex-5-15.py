# Programming Exercise 5-15
#
# Program to find the average of five scores and output the scores and average with letter grade equivalents.
# This program prompts a user for five numerical scores,
# calculates their average, and assigns letter grades to each,
# and outputs the list and average as a table on the screen.

# define the main function
def main():
    # define local variables for average and five scores
    avg = 0.0

    # Get five scores from the user
    score1 = prompt_for_score()
    score2 = prompt_for_score()
    score3 = prompt_for_score()
    score4 = prompt_for_score()
    score5 = prompt_for_score()


    # find the average by passing the scores to a function that returns the average
    avg = calculate_avg(score1,score2,score3,score4,score5)

    # display grade and average information in tabular form
    # as score, numeric grade, letter grade, separated by tabs
    print_header()
    print_row(1, score1, determine_grade(score1))
    print_row(2, score2, determine_grade(score2))
    print_row(3, score3, determine_grade(score3))
    print_row(4, score4, determine_grade(score4))
    print_row(5, score5, determine_grade(score5))
    # display a line of underscores under this header
    print_footer(avg, determine_grade(avg))
    # print data for all five scores, using the score,
    # with the result of a function to determine letter grade

    # display a line of underscores under this table of data

    # display the average and the letter grade for the average


def prompt_for_score():
    return float(input("Please enter score: "))

def calculate_avg(a,b,c,d,e):
    return (a+b+c+d+e)/5.0

def print_header():
    print("score\t\tnumeric grade\t\tletter grade")
    print("--------------------------------------")

def print_row(num,score,letter_grade):
    print("score ",num,":\t", score,"\t\t",letter_grade)

def print_footer(average_score,letter_grade):
    print("--------------------------------------")
    print("Average score:\t", average_score, "\t\t", letter_grade)

# Define a function to return the average of 5 grades.
# This function accepts five values as parameters,
# computes the average,
# and returns the average.

    # define a local float variable to hold the average
    
    # calculate the average
    
    # return the average



# Define a function to return a numeric grade from a number.
# This function accepts a grade as a parameter,
# Uses logical tests to assign it a letter grade,
# and returns the letter grade.
def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

main()

