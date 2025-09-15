"""
Q9. Create a function updateOddEven that accepts an List of Integers and
update all the even numbers to O and update all the odd numbers to 1.


my_list = [34, 11, 91, 59, 33, 22]
updateOddEven(my_list)
print(my_list)

# Output
[0, 1, 1, 1, 1, 0]
"""


def updateOddEven(my_list):
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            my_list[i] = 0
        else:
            my_list[i] = 1


my_list = [34, 11, 91, 59, 33, 22]
updateOddEven(my_list)
print(my_list)
