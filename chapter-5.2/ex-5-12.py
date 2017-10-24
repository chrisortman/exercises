# Programming Exercise 5-12
#
# Program to find the greater of two integers.
# This program accepts two integers,
# passes them to a function that compares them,
# and displays which one is greater.



# define the main function
def main():
    # Define local variables to hold two integers
    first_integer = 0
    second_integer = 0

    # prompt the user for the first integer
    first_integer = int(input("Enter first int: ")) 
    
    
    # prompt the user for the second integer
    second_integer = int(input("Enter second int: ")) 

    # print the RETURN VALUE from calling a function to find the greater of two integers
    # the two integers are passed as arguments
    this_one = greater(first_integer, second_integer)
    print(this_one) 
    
# Define a function to compare integer values.
# This function accepts two integer parameters,
# compares them,
# and returns the value of the greater.
def greater(first,second):
	# if the first integer is greater, return the first integer
    if first > second:
        print("Integer 1 is larger than 2")
        return first
    else:
        print("Integer 2 is larger than 1")
        return second
        
	# else, return the second integer



# Call the main function to start the program
main()