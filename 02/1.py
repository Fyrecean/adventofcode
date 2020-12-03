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
    min = int(nums[0])
    max = int(nums[1])

    #Validation
    occurrences = 0
    for i in password:
        if i == char:
            occurrences += 1
    if occurrences >= min and occurrences <= max:
        valid += 1

print(valid)