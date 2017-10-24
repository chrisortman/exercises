# Programming Exercise 5-13
#
# Program to display a table of times and falling distances for a specific range in seconds.
# This program accepts no input,
# but uses a loop to pass a range of times in seconds to a function
#       that returns the falling distance for that amount of time,
# and displays the results as a table.



# define the main function
def main():
    # define a local float variable to hold distance
    distance = 0.0

    # Set up results chart, printing time and falling distance separated by a tab
    # include a separator line made with a row of underscores
    print_header()
    
    # loop through a range of time values (in seconds)
    for t in range(10):
        # pass the time to a falling distance function and assign result to distance
        distance = falling_distance(t)
        print_row(time=t, distance=distance)
                # print the time and distance formatted to two places, separated by a tab

def print_header():
    print("Time\tDistance")
    print("--------------")


# Define a function to calculate the falling distance for a time in seconds
# The function accepts a time in seconds as a parameter,
# computes the distance,
# and returns the distance it has fallen in that time
def falling_distance(time):
    return time * 9.8 * 9.8

def print_row(time, distance):
    print("{:.2f}\t{:>7.2f}".format(time,distance))


# Call the main function to start the program
if __name__ == "__main__":
    main()




