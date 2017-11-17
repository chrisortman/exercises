# Programming Exercise 7-1
#
# Program to Total a week's sales (seven inputs).
# This program prompts a user for a sales amount for each day of the week,
# totals them up, then displays the total formatted as currency.
from validations import prompt_for_float


# Define the main function
def main():
    # Define local float variable for rtotal sales


    # Initialize lists for daily sales and days of the week (7 elements each)
    daily_sales = [0.0 for i in range(7)]
    days_of_week = ["Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"]

    # loop 7 times
    for i in range(7):
        prompt_message = "Enter sales for {}:".format(days_of_week[i])
        daily_sales[i] = prompt_for_float(prompt_message, "That's not a number")

    # Display total sales; use a $ and format the value to two decimal places
    print("Total Sales: ${:.2f}".format(sum(daily_sales)))





# Call the main function to start the program
main()
