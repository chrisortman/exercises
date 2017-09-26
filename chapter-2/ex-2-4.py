# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.
item1 = 0.0
item2 = 0.0
item3 = 0.0
item4 = 0.0
item5 = 0.0

subtotal = 0.0
sales_tax = 0.0
total = 0.0

# Constant for the sales tax rate.
TAX_RATE = 0.06

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.
def get_price(for_item):
    val = input("Please enter the price for the " + for_item + " item: ")
    return float(val)

item1 = get_price("first")
item2 = get_price("second")
item3 = get_price("third")
item4 = get_price("fourth")
item5 = get_price("fifth")

# Calculate the subtotal by adding up the item prices.
subtotal = item1 + item2 + item3 + item4 + item5

# Calculate the sales tax by multiplying the subtotal by the tax rate.
sales_tax = subtotal * TAX_RATE

# Calculate the total by adding the subtotal and tax.
total = subtotal + sales_tax

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 
print("Subotal:", format(subtotal, ">10.2f"))
print("Tax:    ", format(sales_tax, ">10.2f"))
print("Total:  ", format(total, ">10.2f"))



