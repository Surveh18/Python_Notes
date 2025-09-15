"""
Q2. Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but
using function. Try calling function with different years as a parameter and
check the output.
"""

year = int(input("Enter year: "))


def is_leap(year):
    if year % 4 == 0:  # Check if divisible by 4
        if year % 100 == 0:  # Check if divisible by 100
            if year % 400 == 0:  # Check if divisible by 400
                print(f"{year} is a Leap Year.")
            # this printf is common for all if's condition
            else:
                print(f"{year} is NOT a Leap Year.")
        else:
            print(f"{year} is a Leap Year.")  # Divisible by 4 but not 100
    else:
        print(f"{year} is NOT a Leap Year.")  # Not divisible by 4


is_leap(year)
