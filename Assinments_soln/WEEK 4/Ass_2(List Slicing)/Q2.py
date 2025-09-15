"""
Q2. Make your own list of numbers. Ask a start and end position from User.
Make another different list which will contain number from start to end
position. Use slicing logic.
"""

# my_list = [22, 1, 45, 23, 90, 71, 56, 33]
# start = 2
# end = 6
# print(my_list[start : end + 1])

from typing import List


def sliceLogic(my_list: List, start: int, end: int):
    print(my_list[start : end + 1])


my_list = [22, 1, 45, 23, 90, 71, 56, 33]
sliceLogic(my_list, 2, 6)
# Output = [45, 23, 90, 71, 56]
