# Number pattern
#Example: 1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

#Example: 2
# for i in range(1,6):
#     for j in range(i, 0, -1): #here i is start and 0 is stop and -1 is step: example when come 1 then print then 1-1=0 then reach stop 0 .
#         print(j, end=" ")
#     print()



                  # star pattern

#Example: 1
# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*", end=" ")
#     print()

#Example: 2
# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# Example: 3
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print("@", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

#Example: 4
# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
# for i in range(5, 0, -1):
#     for k in range(1, i-1):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()



# r = 5
# for i in range(1, r+1):

#     for j in range(r-i):
#         print("@", end="")

#     for k in range(1, i+1):
#         print("*", end=" ")
#     print()


# rows = 5
# for i in range(1, rows+1):
#     # print spaces
#     for j in range(rows-i):
#         print(" ", end="")

#     # print stars
#     for k in range(1, i+1):
#         print("*", end=" ")

#     # move to next line
#     print()


# r = 5
# for i in range(1, r):
#     for j in range(r-i):
#         print("@", end="")

#     for k in range(1, i+1):
#         print("*", end=" ")
#     print()


# rows = 5
# for i in range(1, rows+1):
#     # spaces
#     for j in range(rows-i):
#         print("@", end="")

#     # stars (no extra space)
#     for k in range(1, 2*i):
#         print("*", end="")

#     print()



# rows = 5

# for i in range(1, rows+1):
#     # spaces
#     for j in range(rows-i):
#         print(" ", end="")

#     # stars
#     for k in range(1, 2*i):
#         print("*", end="")

#     print()

# for i in range(rows, 0, -1):
#     # spaces
#     for j in range(rows-i):
#         print(" ", end="")

#     # stars
#     for k in range(1, 2*i):
#         print("*", end="")

#     print()


