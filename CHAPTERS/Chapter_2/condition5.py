doc_num = int(input("Enter the doc_num:"))
age = int(input("Enter the age:"))


if(doc_num>1 or doc_num<5):
    if(doc_num>=5 and age>=18):
        print("You doc is verifed")
        print("You can drive a car")
    elif(age>=18  and age<50):
        print("age is correct")
        print("document missing")
else:
    print("THANK YOU")
      
 
