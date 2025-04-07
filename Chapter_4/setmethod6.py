#set.intersection(set2) #cobines common values & return new
# set1 = {1,2,3,4,5}
# set2 = {6,7,8,2,3}

# result = set1.intersection(set2)

# print(result)


#Here: All set method - add() , remove() , clear() , pop() , union() , intersection()


# info = set()
info = {1,2,3,4,5}
info2 = {1,2,5,6,8}

# info.add((1,2,3,4,5))
# info.remove(3)
# info.clear()
# info.pop()

# info.union(info2)
info.intersection(info2)
print(info)