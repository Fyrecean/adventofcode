with open("05/in") as f:
    input = f.readlines()
seats = [["O" for r in range(8)] for x in range(128)]
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
    seats[row][col] = "X"
found = 0
for i, s in enumerate(seats):
    for k in range(len(s)):
        if s[k] == 'O':
            me = True
            if k == 0:
                me = me and s[k + 1] == 'X'
            elif k == 7:
                me = me and s[k - 1] == 'X'
            else:
                me = me and s[k - 1] == 'X' and s[k + 1] == 'X'
            if me:
                found = i * 8 + k
    if found > 0:
        break

print(found)