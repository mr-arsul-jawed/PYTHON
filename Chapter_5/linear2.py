#EXAMPLE: Linear search using for loop

num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 16

i = 0

for val in num:
    if(val == x):
     print("Founding idx....",num.index(val))
     print("Founding val",val)
     i += 1