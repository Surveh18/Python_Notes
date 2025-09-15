"""
Ask 4 numbers from user. Make sure all the numbers entered by user
are different. Print which number is the smallest.
"""

num1 = 9
num2 = 8
num3 = 7
num4 = 6

# Initializing smallest_number variable with the first number.
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

print(f"The smallest number is : {smallest_num}")
