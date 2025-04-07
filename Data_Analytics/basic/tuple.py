#----------------- EXAMPLE:1 ----------------
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# print(x)


#----------------- EXAMPLE:2 ----------------
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

#----------------- EXAMPLE:3 ----------------

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#----------------- EXAMPLE:3 ----------------