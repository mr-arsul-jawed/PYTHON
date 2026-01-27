#----------------- EXAMPLE:1 ----------------
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")

# if "banana" in thislist:
#   print("Yes, 'banana' is in the fruits list")
  
#----------------- EXAMPLE: 2   ----------------
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
# print(thislist)
#----------------- EXAMPLE: 3   ----------------

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
# print(thislist)

#----------------- EXAMPLE: 4   ----------------

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
# print(thislist)

#----------------- EXAMPLE: 5   ----------------

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
# print(thislist)

#----------------- EXAMPLE: 6   ----------------


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
# print(thislist)

#----------------- EXAMPLE: 7   ----------------

thislist = ["apple", "banana", "cherry"]
thislist.pop()
# print(thislist)

#----------------- EXAMPLE: 8   ----------------
# del this remove the element on the index.
thislist = ["apple", "banana", "cherry"]
del thislist[0]
# print(thislist)

#----------------- EXAMPLE: 9   ----------------


thislist = ["apple", "banana", "cherry"]
thislist.clear()
# print(thislist)

#----------------- EXAMPLE: 10   ----------------

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x: #interesting checking 
    newlist.append(x)

# print(newlist)


#----------------- EXAMPLE: 10   ----------------

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
# print(thislist)



#----------------- EXAMPLE: 10   ----------------
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)