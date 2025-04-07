#write a number to print all prime number

num = int(input("enter the num: "))

if num == 1:
    print("it is not prime ")
if num > 1:
    for val in range(2,num+1):
        if num % val == 0:
            print("no ")
    else:
        print("yes")