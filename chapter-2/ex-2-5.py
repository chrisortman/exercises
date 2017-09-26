# Programming Exercise 2-5
#
# Program to calculate distances traveled over time at a speed.
# This program uses no input.
# It will calculate the distance traveled for 6, 10 and 15 hours at a constant speed,
# then display all the results on the screen.

# Variables to hold the three distances.
# be sure to initialize these as floats.
distance_six_hours = 0.0
distance_ten_hours = 0.0
distance_fifteen_hours = 0.0

# Constant for the speed.
SPEED = 55

# Calculate the distance the car will travel in
# 6, 10, and 15 hours.
distance_six_hours = 6 * SPEED
distance_ten_hours = 10 * SPEED
distance_fifteen_hours = 15 * SPEED


# Print the results for all calculations.
print("After 6 hours you will have traveled", distance_six_hours, "miles")
print("After 10 hours you will have traveled", distance_ten_hours, "miles")
print("After 15 hours you will have traveled", distance_fifteen_hours, "miles")




