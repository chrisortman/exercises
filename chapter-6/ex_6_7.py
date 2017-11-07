def main():
    valid_number = False
    while not valid_number:
        user_input = ""
        user_input = input("Please enter a number:")
        try:
            f = open("afile.txt")
            float(user_input)
        except ValueError:
            print(user_input, "is not a valid number")
        else:
            valid_number = True
        finally:
            f.close()
        
    print("Thank you, your number is", user_input)
    
    
    
    
main()