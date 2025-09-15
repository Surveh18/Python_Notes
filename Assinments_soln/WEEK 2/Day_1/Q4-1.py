"""
Q4. Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7)
using function.
"""

# Question 6 will be solved here.


def find_smallest(num1, num2, num3, num4):
    # Initialize smallest_number variable with the first number.
    smallest_num = num1

    # Check and update if the second number is smaller
    if num2 < smallest_num:
        smallest_num = num2

    # Check and update if the third number is smaller
    if num3 < smallest_num:
        smallest_num = num3

    # Check and update if the fourth number is smaller
    if num4 < smallest_num:
        smallest_num = num4

    # Print the smallest number
    print(f"The smallest number is: {smallest_num}")


# Ask 4 numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Call the function to find and print the smallest number
find_smallest(num1, num2, num3, num4)
