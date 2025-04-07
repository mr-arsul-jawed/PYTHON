names = ["roman", "ramu", "shayam"]

def my_function(Rank):
    for val in range(len(names)):
        if val == Rank:  # Check if the current index matches Rank
            print("Found at index", val, ":", names[val])
            break  # Stop the loop when the Rank is found
        print(names[val])

my_function(1)  # Call the function with Rank = 1




# name = ["roman","ramu","shayam"]
# x = 1
# i = 0
# while i < len(name):
#     if(i==x+1):
#         break
   
#     print(name[i])
#     i += 1


# name = ["roman", "ramu", "shayam"]
# i = 0
# while i < len(name):
#     if i == 2:  # Check if the index is 2
#         print("Found at index 2:", name[i])
#         break  # Exit the loop when index 2 is reached
#     print(name[i])
#     i += 1




