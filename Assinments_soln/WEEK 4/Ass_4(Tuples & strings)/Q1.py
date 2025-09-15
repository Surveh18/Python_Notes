"""
Q1.
Write a Python program to get the 4th element from the last element of a tuple.
"""

from typing import Tuple


def fourth_last_element(my_tuple: Tuple):
    if len(my_tuple) < 4:
        print("Not enough elements.")
        return

    print(f"The fourth last element is {(my_tuple[-4])}")


my_tuple = (1, 2, 3, 4, 5, 67, 54, 2, 56, 9)
fourth_last_element(my_tuple)
