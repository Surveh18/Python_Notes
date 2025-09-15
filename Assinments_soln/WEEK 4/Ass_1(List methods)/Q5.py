"""
Q5. Write a program to put all the common elements (in 2 lists) in another
list and print it using function.


lst1 = [34, 1, 91, 59, 33, 22]
lst2 = [78, 14, 23]
x = common(lst1, lst2)
print(x)

# Output
[]

lst1 = [34, 1, 91, 59, 33, 22]
lst2 = [11, 78, 14, 23, 34]
x = common(lst1, lst2)
print(x)

# Output
[34, 11]
"""

from typing import List


def isCommon(lst1: List[int], lst2: List[int]) -> List:
    result = []
    for i in lst1:
        if i in lst2:
            result.append(i)
    return result


lst1 = [34, 1, 91, 59, 33, 11, 22]
lst2 = [11, 78, 14, 23, 34]
x = isCommon(lst1, lst2)
print(x)
