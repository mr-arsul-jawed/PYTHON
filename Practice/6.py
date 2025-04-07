num_1 = int(input("enter your num: "))
num_2 = int(input("enter your num: "))
num_3 = int(input("enter your num: "))
num_4 = int(input("enter your num: "))

val = []
val.append(num_1)
val.append(num_2)
val.append(num_3)
val.append(num_4)

def first_last(list):

    print("Given num",list)
    
    first_num = val[0]
    last_num = val[-1]

    if first_num == last_num:
        print("True")
    else:
        print("False")



print(first_last(val))