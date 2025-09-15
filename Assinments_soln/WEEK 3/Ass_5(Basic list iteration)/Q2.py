"""
Q2. Given a number, return a list containing the two halves of the number-
If the number is odd, make the rightmost number higher.

Examples:
number_split(4) → [2,2]
number_split(10) → [5,5]
number_split(11) → [5,6]

All numbers will be integers.
You can expect negative numbers too.
"""


def number_split(num):
    left_half = num // 2
    right_half = num - left_half
    return [left_half, right_half]


print(number_split(4))
print(number_split(10))
print(number_split(11))
print(number_split(-9))
