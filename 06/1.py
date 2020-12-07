with open("06/in") as f:
    input = f.readlines()
questions = {
        "a": False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, 
        "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, 
        "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, 
        "v": False, "w": False, "x": False, "y": False, "z": False
    }

sum = 0
for i in input:
    if i == "\n":
        for i in questions:
            questions[i] = False
    else:
        for j in i:
            if j != "\n" and questions[j] == False:
                questions[j] = True
                sum += 1
    
print(sum)