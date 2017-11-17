# Programming Exercise 7-3
#
# Program to compute simple statistics for one year of monthly rainfall.
# This program prompts the user for 12 monthly rainfall values,
# calculates the total and average, finds the high and low values,
# and displays the results on the screen.

from validations import prompt_for_float


# define the main function
def main():

    # define local float variables for total, average, high and low rainfall
    total = 0.0
    average = 0.0
    high = 0.0
    low = 0.0

    # define local string values for high month, low month and rainfall input
    high_month = ""
    low_month = ""

    # define a list of floats to hold 12 monthly rainfall amounts
    monthly_rainfall = [0.0 for i in range(12)]
    # define a list for month names initialized with names for all 12 months.
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]


    # loop through the monthly rainfall list
    for i in range(12):
        # prompt the user for rainfall input, using the month name in the prompt
        prompt_text = "Please enter rainfall for {}:".format(month_names[i])
        monthly_rainfall[i] = prompt_for_float(prompt_text, "That's not a number")

    # Calculate the total of monthly rainfall
    total_rainfall = sum(monthly_rainfall)
    # Calculate the average monthly rainfall
    avg_rainfall = total_rainfall / len(monthly_rainfall)
    # find the high (max) rainfall
    high_rainfall = max(monthly_rainfall)
    # use the index of the high rainfall to find the month name for high rainfall
    high_month = month_names[monthly_rainfall.index(high_rainfall)]
    # find the low (min) rainfall
    low_rainfall = min(monthly_rainfall)
    # use the index of the low rainfall to find the month name for low rainfall
    low_month = month_names[monthly_rainfall.index(low_rainfall)]
    # Display results appropriately, formatting float values to two decimal places
    print("Total Rainfall: {:.2f}".format(total_rainfall))
    print("Average Rainfall: {:.2f}".format(avg_rainfall))
    print("High Month: {}".format(high_month))
    print("Low Month: {}".format(low_month))


# function to validate float input


main()

