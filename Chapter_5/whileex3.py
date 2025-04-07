
#qs3 - print the elements of the following list using a loop: 
# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<len(nums):
#     print(nums[i])
#     i +=1

nums = [1,4,9,16,25,36,49,64,81,100]

i = 1

while i<len(nums):
   if (nums[i]%2 == 0):
      print("Even number:", nums[i])
   elif(nums[i] % 2 != 0):
      print("Odd number:", nums[i])
      i +=1