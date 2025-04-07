#write a program to check the prime number

#Prime Number - A prime number is whole number that cannot evenly divided by any other number except for 1 and itself.


Num = int(input("enter the num: "))

flag = False
if Num == 1:
    print(f"{Num} is not prime number ")
elif Num > 1:
    for i in range(2, Num):
        if(Num % i == 0):
            flag = True
            break 

if flag:
    print(f"{Num}, is not a prime number")
else:
    print(f"{Num}, is a prime number")
            
        

