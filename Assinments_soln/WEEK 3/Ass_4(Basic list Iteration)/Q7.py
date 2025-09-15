"""
Q7. Create a function findLargest that accepts an List of Integers and
returns the largest number from the list.

my_list = [34, 11, 91, 59, 33, 22]
x = findLargest(my_list)
print(x)

# Output
91
"""


def findLargest(my_list):
    largest = my_list[0]
    for i in range(0, len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest


my_list = [34, 11, 91, 59, 33, 22]
x = findLargest(my_list)
print(x)
