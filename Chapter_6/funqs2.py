#write a program to list in single line
# movies = ["venom","animal","stree","tiger"]

# def print_out(list):
#     for items in list:
#         print(items, end=" ")

# print_out(movies)


movies = ["venom","animal","stree","tiger"]

def print_out(list):
    for items in range(len(list)):
        # print(items, end= " ")
        print(list[items], end=" ")


print_out(movies)