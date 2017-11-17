# Include a function to ensure the program has valid float values
def can_cast_to_float(x):
    try:
        float(x)
        return True
    except:
        return False
