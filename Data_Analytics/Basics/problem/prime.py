num = int(input("enter the number:"))


if num <=1:
    print("Not prime number")
else:
    for i in range(2,num):
        if num % i == 0:
            print(f"This is not prime number {num}")
            break
        else:
            print(f"This is prime number {num}")
            break