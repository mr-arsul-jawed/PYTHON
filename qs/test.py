'''r = range(-25,10)
#print(type(r))
print(r)
for i in r:
 print(i,end=" ")'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
 print("* "*n)'''

'''n=int(input("Enter the number of rows: "))
for i in range(1,n+1): 
    for j in range(1,n+1): 
        print(n+1-j,end=" ")
    print()'''

'''for i in range(2):
 for j in range(2):
   print('i = {} j = {}'.format(i,j))'''

# n=int(input("Enter the number of rows: "))
# for i in range(0,n+1):
#  for j in range(0,i+1):
#   print("*",end=" ")
#  print()

# num1 = int(input("enter the number: "))
# num2= int(input("enter the number: "))
# new_num = num1+num2
# print("values",new_num)

# print("data type",type(new_num))

# x= 5
# y=10

# print("the value of x is {} and y value is {}".format(x,y))

n= int(input("enter the values:"))
for i in range (n):
    for j in range (i+1):
     print("*",end="")
    print()

