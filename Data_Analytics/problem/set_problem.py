# -------------- Example:1 --------------------------
#write a program to find the common elements in three list using sets

# a = [1,5,6,7,2]
# b = [4,5,6,7]
# c = [1,9,6,2,5]

# print(set(a) & set(b) & set(c))

# -------------- Example:1 --------------------------

a = [1,5,6,7,2]
b = [4,5,6,7]

# print(a.difference(b))

# -------------- Example:2 --------------------------
#write a program to find max and min in a set
a = {12,13,55,40,20}
# print(max(a))
# print(min(a))


# -------------- Example:2 --------------------------
#write a program to find comman element in three lists using set
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
c = {5,6,7,8,9,10}

first = a.intersection(b)
res = first.intersection(c)
# print(res)

# print(set(a) & set(b) & set(c))

# -------------- Example:2 --------------------------
#write a program to find difference between two sets

a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}

# print(a.difference(b))

# -------------- Example:2 --------------------------
#write a python program to remove an item from a set if is present in the set.
a = {1,2,3,4,5,6}
a.discard(4)
print(a)
# -------------- Example:2 --------------------------
#write a python program to check if a set is a subset of another set.

a = {1,2,3,4,5,6,7,8}
b = {2,3,4}

print(b.issubset(a))

