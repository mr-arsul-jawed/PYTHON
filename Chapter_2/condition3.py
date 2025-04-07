#Example:3
marks= int(input("enter your marks:"))

if(marks >= 90):
    print("Grade:A")
elif(marks>=80 and marks<90):
    print("Grade:B")
elif(marks>70 and marks<=80):
    print("Grade:c")
elif(marks<70):
    print("D")
else:
    print("fail")