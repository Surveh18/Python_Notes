"""
Q4. Make a function named factorial(), which takes an integer n. Return the
factorial of that number.

# Example 1
r = factorial (5)
print(r)

# output
120

# Explaination
5 * 4 * 3 * 2 * 1 is = 120

# Example 2
r = factorial (3)
print(r)

# output
6

# Explaination
3 * 2 * 1 is = 6
"""


def factorial(n):
    t = 1
    for i in range(1, n + 1):
        t = t * i
    print(t)


factorial(3)
factorial(5)
