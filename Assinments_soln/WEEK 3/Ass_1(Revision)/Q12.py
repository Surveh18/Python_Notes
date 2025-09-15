"""
Q12. Create a function that takes three arguments a, b, c and returns the
sum of the numbers that are evenly divided by c from the range a, b
inclusive.

# Examples:
• evenly_divisible(1, 1O, 20) -> O
# No number between 1 and 10 can be evenly divided by 20.

• evenly_divisible(1, 1O, 2) -> 30
# 2 + 4 + 6 + 8 + 1O = 30

• evenly_divisible(1, 1O, 3) -> 18
# 3 + 6 + 9 = 18

Return O if there is no number between a and b that can be evenly divided
by c.
"""


def evenly_divisible(a: int, b: int, c: int) -> str | int:
    total_sum: int = 0
    for i in range(a, b + 1):
        if i % c == 0:
            total_sum += i
    return total_sum


print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
print(evenly_divisible(1, 10, 3))
