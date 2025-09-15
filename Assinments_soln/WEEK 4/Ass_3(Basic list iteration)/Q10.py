"""
Q1O. Create a function updateOddEven that accepts an List of Integers
and update all the even numbers to increment by 1 and update all the odd
numbers to decrement by 1.

my_list = [34, 11, 91, 59, 33, 22]
updateOddEven(my_list)
print(my_list)

# Output
[35, 10, 90, 58, 32, 23]
"""


def updateOddEven(my_list):
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] += 1
        else:
            my_list[i] -= 1


my_list = [34, 11, 91, 59, 33, 22]
updateOddEven(my_list)
print(my_list)

# Output - [35, 10, 90, 58, 32, 23]