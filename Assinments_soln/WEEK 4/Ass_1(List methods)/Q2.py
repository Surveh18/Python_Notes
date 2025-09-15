# Q2.Write a function to remove duplicates from a list and print them.
from typing import List


def removeDuplicates(my_list: List[int]):
    result = []
    """
    Method - 1
    for i in range(0, len(my_list)):
        if my_list[i] not in result:
            result.append(my_list[i])
    """
    for i in my_list:
        if i not in result:
            result.append(i)
    print(result)


my_list = [34, 96, 34, 34, 51, 27, 96, 96, 11, 34]
removeDuplicates(my_list)
