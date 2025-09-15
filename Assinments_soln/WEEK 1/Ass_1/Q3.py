"""
Ask 3 num from user and calculate average.
"""

num1: float = float(input("Enter num1: "))
num2: float = float(input("Enter num2: "))
num3: float = float(input("Enter num3: "))
# Calculation of average
Avg = (num1 + num2 + num3) / 3
print(f"Average of {num1}, {num2}, {num3} is {Avg}.")
