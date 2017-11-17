# Include a function to ensure the program has valid float values
def try_cast_to_float(x):
    try:
        maybe = float(x)
        return True, maybe
    except:
        return False,None

def can_cast_to_float(x):
    return try_cast_to_float(x)[0]

def prompt_for_float(prompt_text, invalid_message):
    need_value = True
    while need_value:
        # get the daily sales for the current day by name
        potential_value = input(prompt_text)
        # use a function to validate the input can be cast to a float
        valid,f_value = try_cast_to_float(potential_value)
        if valid:
            # add the daily sales to the total
            need_value = False
            return f_value
        else:
            print(invalid_message)
