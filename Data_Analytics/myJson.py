#Example: 1
# import json
# # student = {"name": "Arsul", "age": 20, "marks":80}

# # # print(type (student)) # this is provide me dictionary

# # Data = json.dumps(student)
# # print(type(Data)) #this is provide me string

#Example: 2

# import json

#access the value of age from the given JSON data.

# student = '{"name": "Arsul", "age": 20, "marks":80}'

# data = json.loads(student) 
# print('The age is:', data["age"])
# # print(student["age"])

#Example: 3
#pretty print following JSON data

# import json
# Student = '{"name": "Arsul", "age": 20, "marks":80}'
# Data = json.dumps(Student,indent=4, separators=(",","="))
# print(Data)

#Example: 4

#Sort the following JSON keys and write them into a file

# import json

# Student = {"name": "Arsul", "age": 20, "marks":80}
# data = json.dumps(Student,indent=4, sort_keys = True)
# f = open("demo.json","w")
# f.write(data)
# print(data)

# another example

# import json

# Student = {"name": "Arsul", "age": 20, "marks":80, "id":"arsul123"}
# # data = json.dumps(Student,indent=4, sort_keys = True)
# data = json.dumps(Student,indent=4, sort_keys=True)
# f = open("demo.json","w")
# f.write(data)
# print(data)



# #Example: 4

# import json
# student_data = """{ 
# "student" :{
#     "grade":{
#     "name": "arsul",
#     "marks":{
#     "math": 90 
#       }
#      }
#     }

# }"""

# data = json.loads(student_data)
# print(data["student"]["grade"]["marks"]["math"])


import json

student = {"name": "Arsul", "age": 20, "marks":80}
student2 = {"name": "jawed", "age": 20, "marks":80}

data = json.dumps(student, indent=4, sort_keys=False)
data2 = json.dumps(student2, indent=4, sort_keys=False)

# print(data)

f = open("demo.json","w")
f.write(data)
print(data)





