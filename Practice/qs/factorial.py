num = int(input("Enter a number: "))
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers."
    else:
        return n * factorial(n-1)
    

result = factorial(num)
print(f"The factorial of {num} is: {result}")
    



    



