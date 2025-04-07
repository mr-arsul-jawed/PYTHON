num = int(input("enter the number:"))
if num <= 1:
    print("it is not prime number")
else:
 for i in range(2,num):
    if num % i == 0:
        print("Not prime")
        break
    else:
       print("Prime")
       break
