#Example: using nested loop


# age = int(input("enter the age:"))
# doc_num = int(input("enter your verified doc_num: "))

# if(age >= 18):
#     if(doc_num>=5):
#      print("verified")
#      print("you can drive")
#     else:
#        print("you have not all document please go and take all document")
# elif(age <= 18):
#     print("not verified")
#     print("you can't drive")


light = int(input("Enter the light number: "))


if(light>=1 and light<=5):{
    print("RED IS ACTIVE"),
    print("Message: Please wait for the green light!")
}
   
elif(light>=6 and light<=10):{
    print("YELLOW IS ACTIVE!"),
    print("Message: Be prepared to stop!")
}
elif(light>=11 and light<=15):{
    print("GREEN IS ACTIVE"),
    print("Message: Go ahead!")
}
else:{
    print("WRONG INPUT WAIT FOR RIGHT INPUT AND NEXT TIME TRY AGAIN")
}