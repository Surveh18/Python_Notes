"""
Q9. Write a function named check_number that takes a number and prints
whether it is positive, negative, or zero.
"""

num = int(input("Enter num: "))


def check_num(num):
    if num > 0:
        print(f"{num} is Positive number.")
    if num < 0:
        print(f"{num} is Negative number.")
    elif num == 0:
        print(f"{num} is Zero number.")


check_num(num)
