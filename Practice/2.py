# previous_num = 0

# for val in range(1,10):
#     sum = previous_num + val
    
#     # Here: both print is same work.
#     # print("current_val=",val, "previos_num=",previous_num, "sum=",sum)
#     print(f"current_num = {val} previous_num = {previous_num} sum = {sum}")
#     previous_num = val





# previos_num = 0

# for val in range(1,10):
#     result = val + previos_num
#     print(f"current_num:{val}, previous_num:{previos_num}, result:{result}")
#     previos_num = val


def pre_curr(val):
    previous_num = 0
    for val in range(1,val):
        result = val + previous_num
        print(f"current_num:{val}, previous_num:{previous_num}, result:{result}")
        previous_num = val

pre_curr(10)



