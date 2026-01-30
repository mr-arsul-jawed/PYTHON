#------------------ Example:1 ---------------------
#qs= sort the values in dictionary
# a = {"a":12, "b":20,"c":22,"d":99}

# a = sorted(a.values())
# print(a)

#------------------ Example:2 ---------------------
#qs = square the values
# a = {}

# for i in range(1,16):
#    a[i] = i**2
   

# print(a)


#------------------ Example:3 ---------------------
#qs= multiply the values
# a = {"a":1, "b":2,"c":3,"d":4, "e":5}
# res = 1

# for i in a.values():
#     res *= i

# print(res)

#another way to solved it.

# a = {"a":1, "b":2,"c":3,"d":4, "e":5}

# res = 1

# for i in a:
#     res *= a[i]

# print(res)
    

#------------------ Example:4 ---------------------
#sort the dictionary key

a = {12:"a",11:"b",10:"c"}

a = sorted(a.keys())
print(a)


