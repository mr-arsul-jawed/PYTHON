#nested dictionary

student = {
    "name" : "arsul",
    "subject" : {
           "math" : 89,
           "hindi" : 90,
           "software" : 96, 
           },
    "age" : 22,
    "mobile" : {
        "personal-number": 7488619278,
        "alternate-number":892839912,

    },
    "address" : "kolkata"
}

student["age"] = 25

# print(student["name"]) #if you get name only follow this step
# print(student["age"])

# print(student["subject"]["math"]) #if you get inside and inside data then follow this step

# print(student["mobile"]["personal-number"])


# dic iteration
information = {
    "name":"arsul jawed",
    "roll":"Bca223015",
    "subject" : {
        "comouter science":"amina",
        "operating system":"zafar",
        "department":{
            "CSE":2022,
            "BCA":2022,
            "year":{
                "first Batch":2000,
                "second batch": 2001

            }
          
        }
    }

}

print(information["subject"]["department"]["year"]["first Batch"])
