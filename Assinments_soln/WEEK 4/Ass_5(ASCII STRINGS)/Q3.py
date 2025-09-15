"""
Q3.
Implement a function in Python to check if a string is alphanumeric by examining the ASCII values of its characters.
Input: "Var123"
Output: True
"""


def countAlphanumeric(n: str):
    for ch in n:
        ascii_code = ord(ch)
        if ascii_code >= 48 and ascii_code <= 57:
            return False
        return True

# Optimize
# def countAlphanumeric(n: str) -> bool:
#     return bool(ch.isalnum() for ch in n)


print(countAlphanumeric("Var123"))
print(countAlphanumeric("123"))
