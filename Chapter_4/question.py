#Question---1
# dic = {
#     "table": ["a piece of furniture","list of facts & figure"],
#     "cat" : "a small animal"
# }

# print(dic)
# print(type(dic))

# #Question---2
# set = {"python","java","java","java","c","c++","c++","javascript","python","python"}

# print(set)
# print(len(set))

#Question---3

# sub1 =int(input("enter the sub1 marks: "))
# sub2 =int(input("enter the sub2 marks: "))
# sub3 =int(input("enter the sub3 marks: "))

# marks={}
# marks["math"] = sub1
# marks["phy"] = sub2
# marks["chem"] = sub3

# print(marks)

#another  rules same question but use method of .update()
# marks = {}
# x = int(input("enter phy: "))
# # marks.update({"phy": x })
# marks.update({"phy": x })

# x = int(input("enter math: "))
# marks.update({"math": x })

# x = int(input("enter eng: "))
# marks.update({"eng": x })

# print(marks)# 


marks = {}
x = int(input("enter the py: "))
marks.update({"py": x})
x = int(input("enter the math: "))
marks.update({"math": x})
x = int(input("enter the chem: "))
marks.update({"chem":x})

print(marks)


