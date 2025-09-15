"""
Q2.
Write a Python program to fi nd repeated items in a tuple
"""

from typing import Tuple


def findRepeatedElements(t: Tuple):
    repeated_tuple = []

    for i in range(0, len(my_tuple)):
        if my_tuple[i] in my_tuple[i + 1 :] and my_tuple[i] not in repeated_tuple:
            repeated_tuple.append(my_tuple[i])
    return repeated_tuple


my_tuple = 22, 34, 8, 3, 1, 34, 68, 22, 45, 7, 9, 0, 22
r = findRepeatedElements(my_tuple)

if len(my_tuple) > 0:
    print(f"Repeated items are {r}")
else:
    print(f"No Repeated items found.")
