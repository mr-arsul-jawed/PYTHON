#Function : block of statements that perform a specific task.
# here: input is parameter
#function call inside that called (arguments)


#function defination
# def calc_sum(a,b): #here: a and b is parameters
#     sum = a+b
#     print(sum)

#     return sum



# calc_sum(10,10) #function call; arguments

# calc_sum(40,20)

# calc_sum(100,5)



# def solution(s):
#     for i in range(len(s)):
#         if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u" or s[i] == "A" or s[i] == "E" or s[i] == "I" or s[i] == "O" or s[i] == "U":
#             print(i, end=" ")

# # Example usage:
# solution("Hello WORLD")  # Output: 1 4 7 


# def vowel(anyname):
#    for i in range(len(anyname)):
#       if anyname[i] == "a" or  anyname[i] == "e" or  anyname[i] == "i" or  anyname[i] == "o" or  anyname[i] == "u" or  anyname[i] == "A" or anyname[i] == "E" or \
#       anyname[i] == "O" or anyname[i] == "U":
#          print(i, end=" ")

# result = vowel("arsul")
# print(result)

# def check(any):
#     if(any.find(" ")):
#         print("Space Detected")
#     else:
#         print("Space not detected ")

# check("arsul")






# def findnum(arr):
#     for i in arr:
#         if (i == 5):
#             print("5 is found")

#         else:
#             print("5 is not found")
# array = [2,3,5]

# findnum(array)


# str = " "
def check(any):
    for i in range(len(any)):
        # print(i)
        if(any[i] == " "):
            print("Space Detected",any[i])
        else:
            print("Not Space",any[i])

check("a rs ul")



    

