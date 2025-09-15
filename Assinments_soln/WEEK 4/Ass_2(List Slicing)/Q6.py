"""
Q6. Make your own list. Write a Python program to reverse that list using
slicing.
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
print(my_list[::-1])


from typing import List


def reverseSlicing(my_list: List):
    print(my_list[::-1])


my_list = [10, -5, 8, 3, -1, -9, 7, 2]
reverseSlicing(my_list)
