"""
Q8. Create a function findSmallest that accepts an List of Integers and
returns the smallest number from the list.

my_list = [34,11,91,59,33,22]
x = findSmallest(my_list)
print(x)

# Output
11
"""


def findSmallest(my_list):
    smallest = my_list[0]
    for i in range(0, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest


my_list = [34, 11, 91, 59, 33, 22]
x = findSmallest(my_list)
print(x)
