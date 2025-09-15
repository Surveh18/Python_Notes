"""
Q5 calculate the factorial of a number using while loop
example n = 5
5 * 4 * 3 * 2 * 1
o/p = 120
"""

num = 5
result = 1
while num > 0:
    result = result * num
    num -= 1
print(f"The factorial of given number is {result}")
