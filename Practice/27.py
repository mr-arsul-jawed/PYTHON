# Find the maximum element in a list without using max()

def find_max_element(lst):
    min_element = lst[0]  # Initialize with the first element
    for element in lst:
        if element < min_element:
            min_element = element
    return min_element

# Example usage
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5,0]
print(find_max_element(sample_list))  