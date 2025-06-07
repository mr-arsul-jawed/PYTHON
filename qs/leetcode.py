def two_num(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] + num[j] == target:
                return [i, j]


nums = [2, 7, 11, 15]
target = 9
result = two_num(nums, target)
print(two_num(nums, target)) 

if result:
    print(f"The indices of the two numbers that add up to {target} are {result}.")
    print(f"The numbers are {nums[result[0]]} and {nums[result[1]]}.")
else:
    print(f"No two numbers add up to {target}.")







