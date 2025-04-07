def reverse(arr):
    first = []
    second = []
    f_pro = 1
    s_pro = 1
    for i in range(0, len(arr)):   
        if (arr[i]<4):
            f_pro *= arr[i] 
            first.append(i)
        elif (arr[i]>3):
            s_pro *= arr[i]
            second.append(i)
    if f_pro < s_pro: 
        arr.reverse()
        return arr 
    else:
        return "Array not changed"

val = [1, 2, 3, 4, 5, 6]
print(reverse(val))  


