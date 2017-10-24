# Programming Exercise 6-2
#
# Program to read up to five lines of a file and display them.
# This program prompts the user for a file name,
# attempts to open and read five lines of the file,
# then displays those lines and finally closes the file.



# define a main function
def main():
    # Declare local variables, line and filename as strings and counter as int
    line = '' 
    filename = ''
    counter = 0
    # Prompt the user for a file name
    filename = input("Please enter a filename: ")
    # Open the specified file for reading
    selected_file = open(filename,'r')

    # Read the first line of the file and increment the line counter to 1
    # this is needed to prepare conditions for the while loop to follow
    line = selected_file.readline()
    counter += 1
    # Use a while loop to read until counter is 5 or reading produces no data
    while counter <= 5 and line != '':
	# remove carriage returns before display, as print() supplies its own
        print(line.rstrip())
        line = selected_file.readline()
        counter += 1
        # Update counter when line is read


    # Close file
    selected_file.close()

# Call the main function to begin the program
main()

