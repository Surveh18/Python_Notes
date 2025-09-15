"""
Q3. Write a Python function that takes two lists and returns True if they
have at least one common element.

lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23]
x = func(lst1,lst2)
print(x)

# Output
False

lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23, 34]
x = func(lst1,lst2)
print(x)

# Output
True
"""

from typing import List


def isCommon(lst1: List, lst2: List) -> bool:
    for i in lst1:
        if i in lst2:
            return True
    return False


lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23, 34]
print(isCommon(lst1, lst2))
