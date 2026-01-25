#qs1

# list = []
# num1 = int(input("enter the data:"))
# num2 = int(input("enter the data:"))
# num3 = int(input("enter the data:"))
# num4= int(input("enter the data:"))

# list.append(num1)
# list.append(num2)
# list.append(num3)
# list.append(num4)

# print(tuple(list))


#qs2
# color_list = ["Red","Green","White" ,"Black"]

# print(color_list[0],color_list[3])

# #EXAMPLE:qs3
# # Define a tuple called 'exam_st_date' containing the exam start date in the format (day, month, year)
# exam_st_date = (11, 12, 2014)

# # Print the exam start date using string formatting
# # The '%i' placeholders are filled with the values from the 'exam_st_date' tuple
# print("The examination will start from : %i / %i / %i" % exam_st_date)



# n = 7

# sum = 0

# i = 1

# while i <= n:
#     sum +=i
#     i +=1
# print("The total sum:", sum)

n = int(input("enter the n:"))
# n = 5

fact = 1



for val in range(1, n+1):
    fact *= val
   
    print("the factorial is: ",fact)
   