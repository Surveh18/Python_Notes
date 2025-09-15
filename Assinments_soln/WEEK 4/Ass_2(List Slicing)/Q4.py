"""
Q4. Make your own list. Write a Python program that takes an integer as an
input, and make a new list containing the last n elements of the original
list. Using slicing logic.

my_list = [10, -5, 8, 3, -1, -9, 7, 2]

Enter n = 3
result = [-9,7,2]
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
my_list = [10, -5, 8, 3, -1, -9, 7, 2]
l = len(my_list)
n = 3
print(my_list[l - n :])

from typing import List


def ListLastNSlice(my_list: List, n: int):
    l = len(my_list)
    print(my_list[l - n :])


my_list = [10, -5, 8, 3, -1, -9, 7, 2]
ListLastNSlice(my_list, 3)
# Output = [-9, 7, 2]
