"""
Q8.
Write a function in Python that removes all numeric characters from a string by checking their ASCII codes.
Input: "Abc123"
Output: "Abc"
- 48-57           | 0 to 9     | Digits
"""


def removeAlphanumeric(n: str):
    return "".join(ch for ch in n if ch.isalpha())


print(removeAlphanumeric("abc123"))  # abc
