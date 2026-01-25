# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)


# fruits = ["apple","mango","banana","lichi"]

# print_list(fruits)


# def list(n, idx=0):
#     if(idx == len(n)):
#         return
#     print(n[idx]) #This is printing the value of the list at the index idx
#     list(n, idx+1) #This is calling the function recursively with the next index value


# fruits = ["apple","mango","banana","lichi"]
# list(fruits) #This is calling the function with the list of fruits


def call_fun(n, idx=0):
    if(idx == len(n)):
        return
    n[idx]
    print(n[idx])
    call_fun(n, idx+1)

fruits = ["apple","mango","banana","lichi"]
call_fun(fruits) #This is calling the function with the list of fruits
   

