"""
Q1. Make your own list of numbers. Ask a start and end position from user.
Print the list from start position to end position without using slicing.
"""

from typing import List


def ListSlice(my_list: List, start: int, end: int):
    result: List = []
    for i in range(start, end + 1):
        result.append(my_list[i])
    print(result)


my_list = [22, 1, 45, 23, 90, 71, 56, 33]
ListSlice(my_list, 2, 6)
