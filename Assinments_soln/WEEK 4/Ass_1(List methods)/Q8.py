"""
Q8. Take 10 integer inputs from user and store them in a list. Now, copy all
the elements in another list but in reverse order.
"""

from typing import List

num: List[int] = []

for i in range(10):
    nums = int(input(f"Enter the num {i+1}: "))
    if nums == 0:
        break
    num.append(nums)

reversed_list = []

for i in range(len(num) - 1, -1, -1):
    reversed_list.append(num[i])

print(reversed_list)
