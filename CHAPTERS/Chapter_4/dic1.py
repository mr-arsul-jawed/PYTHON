# #Dictinonary in python
# #Example:1
info = {
    "name" : "arsul",
    "subject" : ["python","c","c++","java"],
    "topics" : ("dict","set"),
    "Leaning" : "coding",
    "age" : 20,
    "is_student" : True,
    "marks" : None
}

# print(info)
# print((info["name"]))
# print(type(info)) # when you find type of info then it give dict. 
# print(type (info["age"])) # when you find type of info["age"] then it give int.
print(info["Leaning"])
info['Leaning'] = "programing"
print(info["Leaning"])



