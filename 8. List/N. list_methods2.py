# here using count method we are count that how many times a value in list
# is appearing.
my_list = ["True", 32, -09.8, 22.1, "Surve"]
x = my_list.count("True")
print(x)  # 1

my_list.append([2, 3, 4, 12])
print(my_list)
# ['True', 32, -9.8, 22.1, 'Surve', [2, 3, 4, 12]]
# list k andr list aajegi

my_list.extend([22, 11, 21, 34])
print(my_list)
# ['True', 32, -9.8, 22.1, 'Surve', [2, 3, 4, 12], 22, 11, 21, 34]
# extend is iterable by iterating values it adds.

my_list.reverse()
print(my_list)
# [34, 21, 11, 22, [2, 3, 4, 12], 'Surve', 22.1, -9.8, 32, 'True']

# For sort the list the list should contains only float or int.
# internally sort compares everything so an int cannot be compare by str.
my_list.sort()
print(my_list)
