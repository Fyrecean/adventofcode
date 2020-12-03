with open("3/in") as f:
    input = f.readlines()

x = 0
y = 0
slopex = 3
slopey = 1
hits = 0

while y < len(input):
    if input[y][x] == '#':
        hits += 1
    x += slopex
    x %= len(input[0]) - 1
    y += slopey

print(hits)