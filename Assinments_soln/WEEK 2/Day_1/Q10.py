"""
QIO. Write a function named is_odd_even that determines if a number is
odd or even without using the modulo operator (%). Hint: Use division or
subtraction.
"""

num: int = int(input("Enter the num: "))


# The basic idea is to keep subtracting 2 from the number until you reach either 0 (even) or 1 (odd).
def is_odd_even(num):
    # Divide the number by 2 and check if it's equal to the original number when multiplied by 2
    if (num // 2) * 2 == num:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")


# Example usage
is_odd_even(num)

# 10 is even and 7 is odd
