# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats
purchase_amount = 0.0
state_tax = 0.0
county_tax = 0.0
total_tax = 0.0
total_sale = 0.0

# Constants for the state and county tax rates
COUNTY_TAX_RATE = 0.06
STATE_TAX_RATE = 0.07

# Get the amount of purchase from the user, casting it to a float.
purchase_amount = input("Enter the total purchase amount: ")
purchase_amount = float(purchase_amount)

# Calculate the state sales tax.
state_tax = purchase_amount * STATE_TAX_RATE

# Calculate the county sales tax.
county_tax = purchase_amount * COUNTY_TAX_RATE

# Sum the total tax.
total_tax = state_tax + county_tax

# Calculate the total of the sale.
total_sale = purchase_amount + total_tax

# Print detailed information about the sale, formatting all values to two decimal places.
line = "{:<15} {:>10.2f}"
print(line.format("Purchase:",purchase_amount))
print(line.format("State Tax:",state_tax))
print(line.format("County Tax:",county_tax))
print(line.format("Total Tax:",total_tax))
print(line.format("Total:",total_sale))




