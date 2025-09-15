"""
Q4.
Write a Python function that toggles the case of each letter in a string (converts uppercase to lowercase and vice versa) using ASCII values.
Input: "Python3.8"
Output: "pYTHON3.8"

- 65-90           | A to Z     | Uppercase letters
- 97-122          | a to z     | Lowercase letters
"""


def swapcase(n: str) -> str:
    result = str()
    for ch in n:
        ascii_val = ord(ch)
        if ascii_val >= 97 and ascii_val <= 122:
            result += chr(ascii_val - 32)
        elif ascii_val >= 65 and ascii_val <= 90:
            result += chr(ascii_val + 32)
        else:
            result += ch
    return result


print(swapcase("Python3.8"))
