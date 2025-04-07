#---------------------------Example:1 -----------------------------------
a = {"ironman","hulk","thor","america"}
# print(a)

# print(type(a))

# for x in a:
#     print(x)

#---------------------------Example:2 -----------------------------------
#method: add(), pop(), remove(), discard(), copy(), 


# This will add Daxit
people = {"Jay", "Idrish", "Archi"}
# people.add("Daxit")
# print(people)

         #pop()

# people.pop()
# print(people)

        #remove()

# people.remove("Jay")
# print(people)

        #discard()

# people.discard("Jay")
# print(people)

        # copy()

# copy = people.copy()
# print(copy)

        #clear()
# people.clear()
# print(people)

#---------------------------Example:3 -----------------------------------

# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
# print(s)

# values of a set cannot be changed
# s[1] = "Hello"
# print(s)

#---------------------------Example:4 -----------------------------------

s = {"Geeks", "for", 10, 52.7, True}
# print(s)

#---------------------------Example:5 (union()) -----------------------------------

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

# Union using union()
# function
population = people.union(vampires)

# print("Union using union() function")
# print(population)

# Union using "|"
# operator
population = people|dracula

# print("\nUnion using '|' operator")
# print(population)


#---------------------------Example:6 (intersection()) -----------------------------------
set1 = set()
set2 = set()

for i in range(5):
    set1.add(i)
   

for i in range(3,9):
    set2.add(i)
   

# Intersection using
# intersection() function
set3 = set1.intersection(set2)

# print("Intersection using intersection() function")
# print(set3)

# Intersection using
# "&" operator
set3 = set1 & set2

# print("\nIntersection using '&' operator")
# print(set3)



#---------------------------Example:6 -----------------------------------

# isdisjoint(), issubset(), issuperset(), update(),

a = {"ironman","hulk","thor"}
b = {"superman","batman","wonder-women"}
c = {"hulk", "thor"}

# print(a.isdisjoint(b))
# print(c.issubset(a))
# print(a.issuperset(c))
# a.update(b)
# print(a)