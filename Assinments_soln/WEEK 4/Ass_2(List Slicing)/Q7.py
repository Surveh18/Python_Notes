"""
Q7. Write a python program to interchange first and last elements in a list.
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# method - 1
my_list[0], my_list[-1] = my_list[-1], my_list[0]
print(my_list)
# method - 2
temp = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp
print(my_list)
