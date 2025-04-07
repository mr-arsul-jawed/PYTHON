# def fact(n):
#   fact = 1
#   for i in range(1, n+1):
#     fact *= i
#     print("previous num:",i, "current num:",fact)

# fact(5)

def feb(n):

    return n*feb(n-1)


sum = feb(6)
print(sum)
