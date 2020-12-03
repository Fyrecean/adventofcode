with open("1/in") as input:
    nums = list(map(int, input.readlines()))

for i, n in enumerate(nums):
    for k in nums[i:]:
        if n + k == 2020:
            print(n*k)