"""
Q6. Write a program to remove the nth index element from a list using a
function.


lst = [34, 11, 91, 59, 33, 22]
removeNth(lst, 3)

# Output
[34, 11, 91, 33, 22]

lst = [34, 11, 91, 59, 33, 22]
removeNth(lst, 3)
# Output
(Do not throw error instead) display this if index does not exists.
Index does not exists.
"""

from typing import List


def removeNth(lst: List, n: int) -> None:
    if 0 <= n < len(lst):
        lst.pop(n)
    else:
        print(f"Index does not exist.")

lst = [34, 11, 91, 59, 33, 22]
removeNth(lst, 10)
print(lst)
