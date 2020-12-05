with open("05/in") as f:
    input = f.readlines()

highest = 0
for line in input:
    min = 0
    max = 128
    for i in range(6):
        if line[i] == 'F':
            max -= (max-min)//2
        else:
            min += (max-min)//2
    if line[6] == 'F':
        row = min
    else:
        row = max - 1
    min = 0
    max = 8
    for i in range(7,10):
        if line[i] == 'L':
            max -= (max-min)//2
        else:
            min += (max-min)//2
    if line[9] == 'L':
        col = min
    else:
        col = max - 1
    
    id = row*8+col
    if id > highest:
        highest = id

print(highest)