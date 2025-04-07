def find_two_sum(nums, target):
   
    for i in range(len(nums)):
      
        for j in range(i + 1, len(nums)):
         
            if nums[i] + nums[j] == target:
           
                return i, j
   
    return None


nums = [2, 3, 4, 5, 6, 7]
target = 8
result = find_two_sum(nums, target)

if result:
    print(f"The indices of the two numbers that add up to {target} are {result}.")
    print(f"The numbers are {nums[result[0]]} and {nums[result[1]]}.")
else:
    print(f"No two numbers add up to {target}.")
