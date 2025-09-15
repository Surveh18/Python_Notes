"""
Q5.
Write a Python script that replaces each non-alphabetic character in a string with a
space, using ASCII to determine character types.
Input: "Hello, World!"
Output: "Hello World "
"""


def nonAlphabetic(n: str) -> str:
    count = ""  # define once before loop
    for ch in n:
        ascii_val = ord(ch)
        if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):  # alphabets
            count += ch
        elif ascii_val == 32:
            count += ""
        else:  # everything else becomes space
            count += " "
    return count


n = "Hello, World!"
print(nonAlphabetic(n))
