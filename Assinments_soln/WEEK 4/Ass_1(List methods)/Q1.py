"""
Q1. Make a list of your own. Make two more empty list like odd and even.
Put all the even numbers from original list to even and odd numbers to
odd and print both lists. (Don't remove anything from original one).
"""

from typing import List


def oddEvenList(my_list: List[int]) -> None:
    even = []
    odd = []

    for i in my_list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(f"Even numbers: {even}")
    print(f"Odd numbers: {odd}")


my_list = [1, 2, 3, 4, 5, 6, 7, 8]
oddEvenList(my_list)
