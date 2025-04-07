#qs - Search for a number x in this tuple using loop:
# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 16
# i = 0

# while i<len(nums):
#     if(nums[i] == x):
#         print("found idx",i)
#         break
    
#     else:
#         print("finding...")
    
#     i +=1


num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 16
i = 0

# while i < len(num):
#     if num[i] == x:
#         print("found idx", i)
#         break
#     print("finding...")
#     i += 1
# else:
#     print("Element not found")

while i<len(num):
    if (num[i] == x):
        print("find..",i)
        break
    else:
        print("elemnt not found")
        i +=1

