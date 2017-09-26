# Programming Exercise 2-2
#
# Program to compute expected profit from sales.
# This program will prompt a user for a sales projection
# and use it to calculate expected profit from a predefined profit margin
# then display the result.

# Variables to hold the sales total and the profit
# initialize them as float values
sales_total = 0.0
profit = float(0)

# Get the amount of projected sales.
# be sure to convert the input to a float
projected_sales = input("Enter projected sales amount: ")
projected_sales = float(projected_sales)

# Calculate the projected profit using a 23% profit margin.

profit_margin = .23
projected_profit = projected_sales * profit_margin


# Print the projected profit.
# be sure to format the output to two decimal places
print("Your projected profit is $", format(projected_profit, ".2f"), sep="")




