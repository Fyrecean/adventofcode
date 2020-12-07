with open("06/in") as f:
    input = f.readlines()
    input.append("\n")
questions = [
        "a", "b", "c", "d", "e", "f", "g", 
        "h", "i", "j", "k", "l", "m", "n", 
        "o", "p", "q", "r", "s", "t", "u", 
        "v", "w", "x", "y", "z"
    ]
sum = 0
person = []
for i in input:
    if i != "\n":
        person.append(i)
    else:
        for k in questions:
            yes = True
            for j in person:
                yes = yes and k in j
            if yes:
                sum += 1
        person = []
print(sum)