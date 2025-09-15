"""
Q3. Write a Python program to convert a given string to all uppercase if it
contains at least 2 uppercase characters in the first 4 characters.
Input: pyTHon
Output: PYTHON

Input: helLo
Output: helLo

Input: gOOD
Output: GOOD
"""

# - 97-122          | a to z     | Lowercase letters
# - 65-90           | A to Z     | Uppercase letters
# if it contains at least 2 uppercase characters

n = "python"


def convertString(s: str):
    first_four = s[:4]
    upper_chars = [ch for ch in first_four if ch.isupper()]
    if len(upper_chars) >= 2:
        s = s.upper()
        return s
    else:
        return "Upper characters are less than 2"


print(convertString("pyTHon"))
print(convertString("python"))
