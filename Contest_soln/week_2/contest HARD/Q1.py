"""
Q1. Make a function named reverse which accepts an integer n from the
user. Reverse the number passed as a parameter and return the reverse
number. Do not use STRINGS.

# Example 1
reverse(91)

# Output
19

# Example 2
reverse(1000)

# Output
1

# Example 3
reverse(1474)

# Output
4741
"""


def reverse(num):
    total = 0
    while num > 0:
        last_digit = num % 10
        total = (total * 10) + last_digit
        num = num // 10
    return total


print(reverse(91))
print(reverse(1000))
print(reverse(1474))
