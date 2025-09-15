"""
Q6.
Write a Python program that computes the sum of the ASCII values of all characters in a string.
Input: "abc"
Output: 294 (sum of ASCII values for 'a', 'b', 'c')
"""

# def computeSum(n: str):
#     result = int()
#     for ch in n:
#         result += ord(ch)
#     print(result, end=" ")


def computeSum(n: str):
    return sum([ord(ch) for ch in n])


print(computeSum("abc"))
