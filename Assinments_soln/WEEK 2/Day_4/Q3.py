"""
Q3. Create a function named factorial which takes a integer as an input and
returns the factorial of that number.
Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120
"""


def factorial(num):
    fact = 1
    while num >= 1:
        fact *= num
        num -= 1
    return fact


num = int(input("Enter the number: "))
print(f"The factorial of the number is {factorial(num)}.")
