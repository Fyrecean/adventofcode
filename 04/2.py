from functools import reduce
with open("04/bad") as f:
    input = f.readlines()

passports = [""]
j = 0
for i in input:
    if not i == '\n':
        passports[j] += i.replace('\n', ' ', -1)
    else:
        passports[j] = passports[j][:-1]
        j += 1
        passports.append("")
count = 0
for i in passports:
    attributes = i.split(' ')
    possibleAttribs = [False] * 7
    valid = True
    for a in attributes:
        type = a[:3]
        val = a[4:]
        if type == 'byr':
            val = int(val)
            valid = valid and val >= 1920 and val <= 2002
            possibleAttribs[0] = True
        elif type == 'iyr':
            val = int(val)
            valid = valid and val >= 2010 and val <= 2020
            possibleAttribs[1] = True
        elif type == 'eyr':
            val = int(val)
            valid = valid and val >= 2020 and val <= 2030
            possibleAttribs[2] = True
        elif type == 'hgt':
            try:
                unit = val[-2:]
                val = int(val[:-2])
                if unit == 'cm':
                    valid = valid and val >= 150 and val <= 193
                elif unit == 'in':
                    valid = valid and val >= 59 and val <= 76
            except:
                valid = False
            possibleAttribs[3] = True
        elif type == 'hcl':
            try:
                int(val[1:], 16)
            except:
                valid = False
            valid = valid and val[0] == '#' and len(val) == 7
            possibleAttribs[4] = True
        elif type == 'ecl':
            valid = valid and val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            possibleAttribs[5] = True
        elif type == 'pid':
            try:
                int(val)
            except:
                valid = False
            valid = valid and len(val) == 9 
            possibleAttribs[6] = True
        elif type == 'cid':
            continue
        if not valid:
            break
    if valid and reduce((lambda x, y : x and y), possibleAttribs):
        count += 1

print(count)