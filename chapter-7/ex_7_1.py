# Programming Exercise 7-1
#
# Program to Total a week's sales (seven inputs).
# This program prompts a user for a sales amount for each day of the week,
# totals them up, then displays the total formatted as currency.



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
        need_value = True
        prompt_message = "Enter sales for {}:".format(days_of_week[i])
        while need_value:
            # get the daily sales for the current day by name
            day_total = input(prompt_message)
            # use a function to validate the input can be cast to a float
            if can_cast_to_float(day_total):
                # add the daily sales to the total
                daily_sales[i] = float(day_total)
                need_value = False
            else:
                print("That's not a number")


    # Display total sales; use a $ and format the value to two decimal places
    print("Total Sales: ${:.2f}".format(sum(daily_sales)))


# Include a function to ensure the program has valid float values
def can_cast_to_float(x):
    try:
        float(x)
        return True
    except:
        return False



# Call the main function to start the program
main()
