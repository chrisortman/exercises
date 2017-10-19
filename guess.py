magic_number = 37


# INPUTS
# guess

# OUTPUTS
# message

# ask user for guess

# check if guess is right
guess_is_wrong = True
while guess_is_wrong:
    guess = input("Guess a number between 0 and 100")
    guess = int(guess)
    if guess == magic_number:
        guess_is_wrong = False
        print("You did it!")
    else:
        guess_is_wrong = True
        print("Sorry")
        
 
 

