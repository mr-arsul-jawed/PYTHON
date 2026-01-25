# #fact using recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     return n*fact(n-1)

# reseult = fact(5)
# print(reseult)

#fibonacci sequence using recursion

def fibonacci(n):
    if(n==0 or n==1):
        return 1
    else:
      return  fibonacci(n - 1) + fibonacci(n - 2)
    

print(fibonacci(5))