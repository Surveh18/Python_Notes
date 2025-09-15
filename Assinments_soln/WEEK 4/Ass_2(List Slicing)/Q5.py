"""
Q5. Make your own list. Write a Python program that takes an integer as an
input, and make a new list containing the last n elements of the original list
but in reverse order. Using slicing logic.

my_list = [10, -5, 8, 3, -1, -9, 7, 2]

Enter n = 4
result = [2, 7, -9, -1]
"""

# my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# l = len(my_list)
# n = 4
# result = my_list[l - n :]
# result.reverse()
# print(result)

from typing import List


def reverseList(my_list: List, n: int):
    l = len(my_list)
    print(my_list[: l - n - 1 : -1])


my_list = [10, -5, 8, 3, -1, -9, 7, 2]
reverseList(my_list, 4)
