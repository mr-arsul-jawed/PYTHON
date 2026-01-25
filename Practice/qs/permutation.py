# def getpermutation(arr, idx):
#     if idx == len(arr): # base case
#         print(arr, end = " ")
#         return
#     for i in range(idx, len(arr)):
#         arr[idx], arr[i] = arr[i], arr[idx]
#         getpermutation(arr, idx + 1)
#         arr[idx], arr[i] = arr[i], arr[idx]

    
# val = [1,2,3,4]
# getpermutation(val, 0)



# from itertools import combinations 
 
# def get_combinations(arr, r):
#     for comb in combinations(arr, r):
#         print(comb)

# val = [1, 1, 3, 4]
# r = 2
# get_combinations(val, r) 

from itertools import combinations
def com(arr,r):
    for comb in combinations(arr,r):
        print(comb)


val = [1,2,3,4]
com(val,2)