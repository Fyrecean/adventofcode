def xor(a, b):
    return (a or b) and not (a and b)

with open("2/in") as f:
    input = f.readlines()

valid = 0
for line in input:
    #Initialization
    parts = line.split(':')
    password = parts[1][1:]
    rule = parts[0].split(' ')
    char = rule[1]
    nums = rule[0].split('-')
    a = int(nums[0])
    b = int(nums[1])

    #Validation
    if xor(password[a - 1] == char, password[b - 1] == char):
        valid += 1

print(valid)