# def sort(arr): 
#     n = len(arr)
#     for i in range(n):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:  # Swap if the element is greater than the next
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr  # Return the sorted array

# arr = [2, 3, 1, 4, 6, 2, 10]
# sorted_arr = sort(arr)
# print(sorted_arr)  
#   # Output: [1, 2, 2, 3,

# arr = [2, 3, 1, 4, 6, 2, 10]

# n = len(arr)
# # print(n) #here: 7

# for i in range(n):
#     # print(i) #Here: 0, 1, 2, 3, 4, 5, 6
#     for j in range(n - i - 1): #here: 6, 5, 4, 3, 2, 1, 0
#         # print('this is end')
#         # print(arr[j], arr[j + 1])
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j+1] = arr[j+1],arr[j]
# print(arr)


# def sort(arr):
#     for i in range(len(arr)): # len(arr) = 7
#         # print(i)
#         for j in range(len(arr) - 1): 
#             # print(j) 
#             if (arr[j] > arr[j + 1]):
#                 arr[j], arr[j+1] = arr[j +1], arr[j]
#     return arr
    

# arr = [2, 3, 1, 4, 6, 2, 10 , 5,7,9,3,2,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 


# print(sort(arr))
# print(len(arr)) #30









