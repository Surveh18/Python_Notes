"""
Q6. Write a function named is_even that takes a number as a parameter
and prints "Even" if the number is even and "Odd" if the number is odd.
"""

num = int(input("Enter num: "))


def is_even(num: int) -> str:
    if num % 2 == 0:
        return f"{num} is an Even number."
    return f"{num} is an Odd number."


is_even(num)
