# Programming Exercise 5-14
#
# Program to compute kinetic energy from mass and velocity.
# This program accepts values for mass and velocity from the user in kilograms and meters per second,
# passes them to a function that returns kinetic energy in joules calculated from those values,
# and displays the result.


# define the main function
def main():
    # define local float variables for mass, velocity and kinetic energy
    mass = 0.0
    velocity = 0.0
    kinetic_energy = 0.0

    mass, velocity = prompt_for_inputs()

    # Get kinetic energy in joules from the kinetic energy function
    kinetic_energy = calculate_kinetic_energy(mass, velocity)

    # Display kinetic energy in joules, formatted to 2 decimal places.
    display_kinetic_energy(kinetic_energy)

def prompt_for_inputs():
    m = float(input("Enter mass in kg:"))
    v = float(input("Enter velocity in meters/s:"))
    return m,v
# Define a function to calculate kinetic energy in joules.
# The function accepts two parameters, mass in kilograms and velocity in meters/second,
# uses a formula to calculate the joules of kinetic energy,
# and returns the result
def calculate_kinetic_energy(mass, velocity):
    return (mass * velocity * velocity) / 2

def display_kinetic_energy(ke):
    print ('Kinetic Energy is:', format(ke, '.2f'), 'joules')
# Call the main function to start the program
main()


