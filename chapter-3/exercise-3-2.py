# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
length_a = 0.0
width_a = 0.0
area_a = 0.0

length_b = 0.0
width_b = 0.0
area_b = 0.0
# initialize these as floats


# Get length A from the user and convert it to a float
length_a = float(input("Enter length for rectangle A:"))

# Get width A from the user and convert it to a float
width_a = float(input("Enter width for rectangle A:"))


# Get length B from the user and convert it to a float
length_b = float(input("Enter length for rectangle B:"))


# Get width B from the user and convert it to a float
width_b = float(input("Enter width for rectangle B:"))


# Calculate area A
area_a = length_a * width_a

# Calculate area B
area_b = length_b * width_b


# Print each area, formatting the values to 2 decimal places
print("Area A: ", format(area_a, '.2f'))
print("Area B: ", format(area_b, '.2f'))

if area_a > area_b:
    print("A is greater")
elif area_b > area_a:
    print("B is greater")
else:
    print("A and B are equal")
# if area A is greater, print "A is greater" message.

# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

