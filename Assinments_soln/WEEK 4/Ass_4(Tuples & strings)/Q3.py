"""
Q3.Write a Python program to check whether an element exists within a tuple.
Ask something from user, if that exists in tuple, then print “YES” else print “NO”.
"""

from typing import Tuple


def elementExistInTuple(t: Tuple):
    n = int(input("Enter num: "))
    if n in my_tuple:
        return f"Yes"
    else:
        return f"No"


my_tuple = 22, 34, 8, 3, 1, 34, 68, 22, 45, 7, 9, 0, 22
print(elementExistInTuple(my_tuple))

"""
Alternate:


def elementExistsInTuple(element, t):
    return element in t


my_tuple = (1, 2, 3, 4, 5)

e = int(input("Enter an element = "))

if elementExistsInTuple(e, my_tuple):
    print("YES")
else:
    print("NO")

"""
