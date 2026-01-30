def fux():{
    print("Hello World")
}
    
# fux()

#parameter and argument
def add(x, y ):{
    print(x + y)
}
    
# add(2,4)

# multiple parameter
def name(*name):{
    # print("Name is: ",name[1])
    print(f"Welcome to Data Analytics {name[0]}")
}   
# name("arsul","jawed")

# return 
def sub(x,y):
    return x-y

# print(sub(4,2))


# recursion function

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)    

# print(fact(5))

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2);

# print(fib(5))

# lambda function
# lambda arguments : expression
a = lambda x : x + 10
# print(a(5))

x = lambda a,b,c: (a+b)*c

# print(x(2,3,4))

# local variables and global variables
x = 25
print(f"This is global variables: {x}")
def hii():
    x = 30
    return f"This is local variables: {x}"

print(hii())



    



