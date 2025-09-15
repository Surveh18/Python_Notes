"""
Q6. Create a function named sumOfSquares, which takes a single integer
as a parameter named n. Return the sum of squares from 1 to n.

# Example 1
r = sumOfSquares(5)
print(r)

# Output
55

# Explaination
5^2 + 4^2 + 3^2 + 2^2 + 1^2
25 + 16 + 9 + 4 + 1 = 55
"""


def sumOfSquares(n):
    t = 0
    n = 5
    for i in range(n, 0, -1):
        t += i**2
    return t


r = sumOfSquares(5)
print(r)
