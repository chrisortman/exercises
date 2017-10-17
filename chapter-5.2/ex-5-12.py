# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function
def main():
    # Define local variables to hold two integers


    # prompt the user for the first integer
    num1 = prompt_user_for("first")
    
    # prompt the user for the second integer
    num2 = prompt_user_for("second")


    # print the return value from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    bigger_num = find_greater(num1,num2)
    display_bigger_num(bigger_num)

def prompt_user_for(something):
    return int(input("Enter " + something + " number: "))

# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def find_greater(x,y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return x

def display_bigger_num(num):
    print("The bigger number is: ",num)

# Call the main function to start the program
main()




