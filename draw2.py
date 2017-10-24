output = ""
cols = 5
rows = 6

for row in range(1,rows):
    for col in range(0,cols):
        output = output + "*"
    output = output + "\n"
    
print(output)
