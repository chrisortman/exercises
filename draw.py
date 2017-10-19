output = ""
cols = 5
rows = 6

for row in range(0,rows):
    for col in range(0,cols):
        output = output + "*"
    #print("*",end='')
    output = output + "\n"
    
print(output)
