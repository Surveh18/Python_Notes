# Q4.Write a python program to find sum and average of list in py.
from typing import List


def sumAndAverage(lst: List[int | float]):
    sum = 0
    for i in lst:
        sum += i
    print(f"Sum = {sum:.2f}")

    avg = sum / len(lst)
    print(f"Average = {avg:.2f}")


lst: List[int | float] = [2, 3, 4, 5, 9, 99.1]
sumAndAverage(lst)
