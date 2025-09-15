"""
Q1.
Write a function in Python that counts the number of digits in a given string using ASCII codes.
Input: "Room 101"
Output: 3
"""


def digitCount(n: str) -> int:
    Digits = int()
    for ch in n:
        ascii_code = ord(ch)
        if ascii_code >= 48 and ascii_code <= 57:
            Digits += 1
    return Digits


n = "Room 101"
print(digitCount(n))  # 3

"""
def digitCount(n: str) -> int:
    return sum(ch.isdigit() for ch in n)
"""
