"""
Q1. Create a python function named isPalindrome which accepts a string as a parameter
and return True if its a palindrome. Palindrome are words which is same when read from start
and same when read from the end.

Examples:
-MOM
-CIVIC
-LEVEL
"""

# n = "mom"
# reverse = n[::-1]
# if reverse == n:
#     print(True)
# else:
#     print(False)

# # in one-line
# v = "dsa"
# print(n == n[::-1])

# h = "MOM"
# result = str()
# for i in range(len(h) - 1, -1, -1):
#     result += h[i]
# if h == result:
#     print(True)
# else:
#     print(False)


def isPalindrome(n: str) -> bool:
    return n == n[::-1]


print(isPalindrome("mom"))  # True
print(isPalindrome("civic"))  # True
print(isPalindrome("python"))  # False
