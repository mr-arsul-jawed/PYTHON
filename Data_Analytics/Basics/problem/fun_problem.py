#example:1
def num():
    result = 1
    for i in range(1, 30):
        result *=  i
        # return result
        
    return result

# print(num())
# num()

#Example - 2
def create_ls():
    ls = []
    for i in range(1, 30):
        ls.append(i**2)
    return ls

# print(create_ls())

#Example -3 prime number check 

def check_prime(n):
    if n==1 :
        print(f"it is not a prime number")
    if n==2:
        print(f"it is a prime number")
    for i in range(2, n):
        if n%i == 0 :
            print(f"it is not a prime number")
            break
        else:
            print(f"it is a prime number")
            break

# check_prime(8)

#example:4
# ls_arr = []
def add(arr):
    val = 0
    for i in range(1, len(arr)+1):
        # print(i)
        val += i
    print(val)
        # ls_arr.append(val)
    # return( ls_arr)


# add([1,2,3,4,5])

#this answer use by recursion

def add(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + add(arr[1:]) 
    
# print(add([1,2,3,4,5]))

#Example:5
def fib(n):
    if n == 1 :
        return 0;
    elif n == 2:
        return 1
    else:
        return (fib(n-1) + fib (n-2))
    
print(fib(8))


