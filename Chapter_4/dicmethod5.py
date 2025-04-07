#mydict.update function simply update the data

# student = {
#     "name" : "Shahid ansari",
#     "subject" : {
#            "math" : 96,
#            "hindi" : 90,
#            "software" : 96, 
#            },
#     "age" : 22,
#     "mobile" : 9838424920,
#     "address_1" : "kolkata"
# } 

# student.update({"address" : "delhi"}) #this is update the address
# student.update({"mobile":123456766}) #this is update the mobile
# new_dict = {"alternate_phone" : 923728913}
# student.update(new_dict)
#here: student["adress"] = "delhi" just change the address also work same.
# student["address"] = "delhi"

# print(student)


#keys()
#values()
#items
#get()
#update()


#write a code with dic use all methods.

info = {
    "name":"arsul",
    "roll":"bca223015",
    "subject":{
        "computer":"amina",
        "os":"zafar",
        "dsa":"zeenat"
    }
}

print(info.keys())
print(info.values())
print(info.get("name"))
print(info["name"])

# info.update({"roll":"abc1234"})
# print(info)


# val = {}

# val["name"] = "arsul"
# val["roll"] = "bca223015"
# print(val)