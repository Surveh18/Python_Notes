"""
Q9. Make a list. Write a simple program for addition of the 2nd element from start 
and 2nd element from the end.
"""

from typing import List


def additionElement(my_list: List[int]):
    if len(my_list) == 1:
        print("Cannot add 2nd and last 2nd element as not enough elements in list")
        return
    print(my_list[1] + my_list[-2])


my_list = [23, 45, 67, 89]
additionElement(my_list)
