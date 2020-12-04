
fields = {
        "byr": False,
        "iyr": False,
        "eyr": False,
        "hgt": False,
        "hcl": False,
        "ecl": False,
        "pid": False,
        "cid": True
    }

with open("04/in") as f:
    input = f.readlines()

consolodated = [""]
j = 0
for i in input:
    if not i == '\n':
        consolodated[j] += i.replace('\n', ' ')
    else:
        j += 1
        consolodated.append("")

valid = 0

for i in consolodated:
    attributes = i.split(' ')
    for j in attributes:
        field = j.split(":", 1)[0]
        fields[field] = True
    correct = True
    for k in fields:
        correct = fields[k] and correct
    if correct:
        valid += 1
    for k in fields:
        if k != "cid":
            fields[k] = False

print(valid)