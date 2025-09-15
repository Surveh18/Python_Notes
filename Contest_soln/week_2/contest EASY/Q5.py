"""
Q5. Make a function named sumPattern that takes an integer n as an
argument from the user. And then calculate the sum of the following
pattern.

! means factorial of that number.

# Example 
sumPattern(5)

Means
1/1! + 1/2! + 1/3! + 1/4! + 1/5!

# Output
1.7166666666666668
"""


def sumPattern(n):
    totalsum = 0
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i  # Calculate factorial iteratively
        totalsum = totalsum + 1 / fact  # Add 1/fact to the total
    return totalsum


# Example usage
print(sumPattern(5))
