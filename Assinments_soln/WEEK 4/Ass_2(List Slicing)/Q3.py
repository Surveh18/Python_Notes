"""
Q3. Make your own list of numbers. Ask a start and end position from User.
Make another different list which will contain number from start to end
position. Use slicing logic. (Same as previous question), but now print the
result in reverse:

Example
my_list = [10, -5, 8, 3, -1, -9, 7, 2]

Enter start position = 2
Enter end position = 5

Output: [-9, -1, 3, 8]
"""

# my_list = [10, -5, 8, 3, -1, -9, 7, 2]
# start = 2
# end = 5
# result = my_list[end : start - 1 : -1]
# print(result)

from typing import List


def reverseList(my_list: List, start: int, end: int):
    result = my_list[end : start - 1 : -1]
    print(result)


my_list = [10, -5, 8, 3, -1, -9, 7, 2]
reverseList(my_list, 2, 5)
# Output = [-9, -1, 3, 8]
