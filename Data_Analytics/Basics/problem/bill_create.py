while True:
    Name = input("enter your name: ")
    total = 0
    while True:
        print ("enter you amount or quantity ")
        amount = float(input("enter your amount: "))
        quantity = int(input("enter your quantity: "))
        total += amount * quantity
        repeat = input("do you add more items: ")
        if repeat == "no" or repeat == "No":
           break 
    

    print("-"*40)
    print("Name",Name)
    print("Amount",total)
    print("-"*40)
    repeat1 = input("do you want to go next customer: ")
    if repeat1 == "no" or repeat1 == "No":
        break


print("******************Happy Shopping*****************")