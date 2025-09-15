"""
Q9. In this challenge, establish if a given integer num is a Curzon number. If
1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num,
then num is a Curzon number.

Given a non-negative integer num, implement a function that returns True
if num is a Curzon number, or False otherwise.

The condition states: 2^n + 1 is divisible by 2n+ 1 without remainder.

# Examples
• is_curzon(5) -> True
2**5 + 1 = 33
2 * 5 + 1 = 11
-> 33 ÷ 11 = 3 (perfectly divisible)

• is_curzon(10) -> False
2**10 + 1 = 1025
2 * 10 + 1 = 21
-> 1025 ÷ 21 = 48.8095
"""


def is_curzon(num: int) -> bool:
    numerator = 2**num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0


print(is_curzon(5))
print(is_curzon(10))
print(is_curzon(14))
