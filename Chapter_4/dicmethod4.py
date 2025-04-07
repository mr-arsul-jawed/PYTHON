#mydic.get("key")

student = {
    "name" : "Rashid",
    "subject" : {
           "math" : 96,
           "hindi" : 90,
           "software" : 96, 
           },
    "age" : 22,
    "mobile" : 9838424920,
    "address" : "kolkata"
}

# #you this key access another method so why i m using this because first look the code 
print(student.get("name")) # This is give me output according to this code is (Rashid) simple but i'm change key of ("name2") then it's give me NONE

print(student["name"]) # This is give me also same output (Rashid) but i'm change key of ("name2") then it's give me error and affect the code

#let's check