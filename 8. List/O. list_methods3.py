my_list = [546, 90, 99, 66, 90, 22]
print(my_list)
# [546, 90, 99, 66, 90, 22]

# Hover on pop method it wants index num of list to remove the element of list.
# Else by default the value will be -1. and return int.
my_list.pop(1)
print(my_list)
# [546, 99, 66, 90, 22]

my_list = [546, "sure", True, 90, 99, 66, 90, 22]
x = my_list.pop(0)
print(x)  # 546
print(my_list)
# ['sure', True, 90, 99, 66, 90, 22]

# remove method wants value to remove element and 
# if the value repeats more than once it will delete th 1st occurence.
my_list.remove(90)
print(my_list)
