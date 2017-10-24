import random

def main():
	
    MIN = 0
    MAX = 10
    
    addend_one = 0
    addend_two = 0
    user_answer = 0
    correct_answer = 0
    
    addend_one, addend_two = generate_random_ints(MIN,MAX)
    correct_answer = calculate_correct_answer(addend_one, addend_two)
    
    display_addition_problem(addend_one,addend_two)    
    user_answer = prompt_for_answer()
    evaluate_answer(
        correct_answer=correct_answer,
        user_answer=user_answer
    )

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("You did it!!")
    else:
        print("Too bad :(")
        
def generate_random_int(min_value,max_value):
    return 5
def generate_random_ints(min_value,max_value):
    x = random.randint(min_value,max_value)
    y = random.randint(min_value,max_value)
    return x,y
def calculate_correct_answer(x,y):
    return x + y
    
def display_addition_problem(addend_one,addend_two):
    line1 = format(addend_one, '5')
    
    line2_left = "+"
    line2_right = format(addend_two, '4')
    line2 = line2_left + line2_right
    
    print(line1)
    print(line2)

def prompt_for_answer():
    user_entry = int(input("Enter your answer: "))
    return user_entry

main()
