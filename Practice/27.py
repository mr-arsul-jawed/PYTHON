# Find the maximum element in a list without using max()

def find_max_element(lst):
    print(lst)
    min_element = lst[0] # Initialize with the first element
    print(min_element)
    for element in lst:
        if element > min_element:
            min_element = element
    return f"The maximum element is: {min_element}" 

# Example usage
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5,0]
print(find_max_element(sample_list))  

# def find_max_element(lst):
#     lst.sort()
#     print(lst)
#     x = lst[-1]
#     return f"The maximum element is: {x}" 








# sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5,0]

# print(find_max_element(sample_list))
