# Programming Exercise 5-2
#
# Program to calculate final purchase details.
# This program takes a purchase amount from a user,
# then calculates state tax, county tax and total tax,
# 	and passes them to a function to be totaled
# and displayed



# Global constants for the state and county tax rates
STATE_TAX = 0.6
COUNTY_TAX = 0.6



# define the main function
def main():
    # Define local float variables for purchase, state tax and county tax
    # Get the purchase amount from the user
    purchase = 0.0
    state_tax = 0.0
    county_tax = 0.0
    
    purchase = float(input("Enter purchase amount:")) 
    # Calculate the state tax using the global constant for state tax rate
    state_tax = purchase * STATE_TAX
    # Calculate the county tax using the global constant for county tax rate
    county_tax = purchase * COUNTY_TAX

    # Call the sale details function, passing the purchase, state tax and county tax
    sales_details(purchase, county_tax, state_tax)


# define a function to display purchase details
# this function accepts purchase, stateTax, and countyTax as arguments,
# calculates the total tax and sale total,
# then displays the purchase details
def sales_details(purchase, county_tax, state_tax):
    # Define local float variables for total tax and sale total
    total_tax = 0.0
    sale_total = 0.0
	# Calculate the total tax
    total_tax = state_tax + county_tax	
	# Calculate the total sale
    sale_total = total_tax + purchase
    # Display the purchase details, including purchase, state tax, county tax,
    #	total tax, and sale total, each on a line.  Format floats to 2 decimal places.
    print("Sale Total: ", format(sale_total, '.2f'))


# Call the main function to start the program.
main()
