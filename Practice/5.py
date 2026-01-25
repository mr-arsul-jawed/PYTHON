# num = [10,20,30,10]
val = []
val.append(int(input("enter your num..1: ")))
val.append(int(input("enter your num..2: ")))
val.append(int(input("enter your num..3: ")))
val.append(int(input("enter your num..4: ")))

def first_last(list):
    print("Given list",list)
    first_num = list[0]
    last_num = list[-1]
    if(first_num == last_num):{
        print("True")
    }
    else:{
        print("False")
    }

print(first_last(val))









