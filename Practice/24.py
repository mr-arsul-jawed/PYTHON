# # qs: first and last element interchange in the list

# my_list = [1,2,3,4,5]

# my_list[0],my_list[-1] = my_list[-1], my_list[0]

# print(my_list)


#qs: first and last element interchange in the list using function

def swaping(new_list):
    size = len(new_list)

    temp1 = new_list[0]
    new_list[0] = new_list[size - 1]
    new_list[size - 1 ] = temp1


    temp2 = new_list[2]
    new_list[2] = new_list[size - 3]
    new_list[size - 3] = temp2

    temp3 = new_list[3]
    new_list[3] = new_list[size-2]
    new_list[size - 2] = temp3
    return new_list


arsul = [12,15,10,5]

print(swaping(arsul))




   





