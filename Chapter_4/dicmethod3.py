#mydict.item() return all(KEY,VALUES) pairs as tuples
student = {
    "name" : "rashmikaa",
    "subject" : {
           "math" : 96,
           "hindi" : 90,
           "software" : 96, 
           },
    "age" : 22,
    "mobile" : 9838424920,
    "address" : "kolkata"
}

# #this is simple print all items
# print(list(student.items()))


#after use pairs then it is print only access items 
# pairs1 = list(student.items())
# pairs2 = list(student)
# print(pairs1[0])
# print(pairs2)

p1 = list(student.items())
p2 = list(student.items())

print(p1[0])
print(p2[1])