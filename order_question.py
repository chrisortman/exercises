UPPER_LIMIT = 100 

def check_numbers(x,y,z):
    a = (x * y) / z
    b = x * (y / z)
    a = round(a, 3)
    b = round(b, 3)
    if abs(a - b) >= .001:
        print("Different values")
        print("First: ",a)
        print("Second: ", b)
        
def print_numbers(x,y,z):
    print("Check: ", x,y,z)
    
# I'm done with this stuff for now    
for x in range(UPPER_LIMIT):
    for y in range(UPPER_LIMIT):
        for z in range(1,UPPER_LIMIT):
           check_numbers(x,y,z)