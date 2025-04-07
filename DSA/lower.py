arr = [15, 2, 30, 40, 10, 5]

min_val = arr[0] #initialize min_val to the first element of the array means first value: 15 then check then 2 then 30 then 40 then 10 then 5.

for i in arr:
    if i < min_val:
        min_val = i
        print("Updated min_val:", min_val) 
print("Final min_val:", min_val)


