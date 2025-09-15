my_list = [543, "surve", 22, 90, True, -21]
print(my_list)
# [543, 'surve', 22, 90, True, -21]

# append add the value in the end of the list. It could be anything.
# Hover on the append method it wants only an object. Object can be any type of data.
my_list.append(122)
print(my_list)
# [543, 'surve', 22, 90, True, -21, 122]

# Hover on the insert method it wants index and object.
# if we add object outside the range that object will be added at last.
my_list.insert(0, -11)
print(my_list)
# [-11, 543, 'surve', 22, 90, True, -21, 122]

my_list.clear()
print(my_list)
# []


