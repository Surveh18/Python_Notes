"""
Q1. Write a program to print absolute value of a number entered by user.

Example 1
Input = -18
Output = 18

Example 2
Input = 9
Output = 9
"""

number = int(input("Enter number:  "))

if number < 0:
    print(f"absolute value for {number} is {number * -1}")
else:
    print(f"absolute value for number {number} is {number} ")
