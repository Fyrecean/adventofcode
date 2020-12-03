from functools import reduce

with open("3/in") as f:
    input = f.readlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
hits = [0] * len(slopes)
for i, (slopex, slopey) in enumerate(slopes):
    x = 0
    y = 0
    while y < len(input):
        if input[y][x] == '#':
            hits[i] += 1
        x += slopex
        x %= len(input[0]) - 1
        y += slopey

print(reduce((lambda x, y : x * y), hits))