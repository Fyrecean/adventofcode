with open("1/in") as input:
    nums = list(map(int, input.readlines()))

for i, n in enumerate(nums):
    for j, m in enumerate(nums[i:]):
        for p in nums[j:]:
            if n + m + p == 2020:
                print(n*m*p)