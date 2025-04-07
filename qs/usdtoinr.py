# usd = int(input("enter the usd: "))

# USD = 83.84

# i = 1

# while i<=usd:
#     USD *= i
#     i +=1

# print("The USD convert in INR:",USD)

usd = int(input("enter the usd: "))

USD = 83.84

for val in range(1, usd+1):
    USD *= val
print(USD)