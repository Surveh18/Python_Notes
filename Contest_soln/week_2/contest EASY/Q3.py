"""
Q3. Create a function named sumNum(), which takes 2 parameters as nl
and n2. Calculate and return the sum of all the numbers divisible by and 2
and 7 between nl to n2. Also if the sum is O, then return -1.

# Example 1
r = sumNum(1,30)
print(r)

# Output
42

# Explaination
14 + 28

# Example 2
r = sumNum(1,10)
print(r)

# Output
-1

# Explaination
No numbers are divisible by 2 & 7 between 1 to 10
"""


def sumNum(n1, n2):
    total = 0
    for i in range(n1, n2 + 1):
        if i % 2 == 0 and i % 7 == 0:
            total += i
    if total == 0:  # If no numbers were found, return -1
        return -1
    return total  # Otherwise, return the total sum


# Example usage
n1, n2 = 1, 30
r = sumNum(n1, n2)
if r == -1:
    print(f"No numbers are divisible by 2 & 7 between {n1} to {n2}")
else:
    print(f"Sum of all numbers divisible by 2 & 7 between {n1} and {n2} is {r}")
