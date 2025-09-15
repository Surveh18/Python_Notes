"""
Q2.
Develop a Python script that counts how many letters are in a string by checking ASCII values.
Input: "Year 2022!"
Output: 4
"""


def countLetters(n: str) -> int:
    return sum(ch.isalpha() for ch in n)


print(countLetters("Year 2022!"))  # 4
