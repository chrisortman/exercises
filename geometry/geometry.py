#main
    #prompt
    #handle_choice
    #display
import circle
import rectangle

AREA_OF_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_RECTANGLE_CHOICE = 3
PERIMETER_RECTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():

    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input("Enter your choice: "))
        output = handle_choice(choice)
        print(output)
        

def display_menu():
    print(" MENU")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")
 
def handle_area_of_circle():
    radius = float(input("Enter the circle's radius: "))
    return "The area is " + str(circle.area(radius))
def handle_circumference_of_circle():
    radius = float(input("Enter the circle's radius: "))
    return "The circumference is " + str(circle.circumference(radius))
    
def area_of_rectangle():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The area is" + str(rectangle.area(width,length))
def perimeter_of_rectangle():
    width = float(input("Enter the rectangle's width: "))
    length = float(input("Enter the rectangle's length: "))
    return "The perimeter is " + str(rectangle.perimeter(width,length))
    
def handle_choice(choice):
    if choice == AREA_OF_CIRCLE_CHOICE:
        return handle_area_of_circle()
    elif choice == CIRCUMFERENCE_CHOICE:
        return handle_circumference_of_circle()
    elif choice == AREA_RECTANGLE_CHOICE:
        return area_of_rectangle()
    elif choice == PERIMETER_RECTANGLE_CHOICE:
        return perimeter_of_rectangle()
    elif choice == QUIT_CHOICE:
        return "Exiting the program..."
    else:
        return "Error: Invalid selection."

main()


