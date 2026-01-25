# alphabet = ['A','B','C','D','E']

# for i in range(len(alphabet)):
#     for j in range(i+1):
#         print(alphabet[j],end=" ")
#     print() # new line


al = ["A","B","C","D","E"]

n = len(al)

for i in range(n):
    for j in range(i+1):
        print(al[j],end=" ")
    print()