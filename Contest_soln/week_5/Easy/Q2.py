"""
Q2. Write a program to rotate the characters in a string by a given number
of positions. For example, given the input "abcdef" and rotation of 2, the
output should be "efabcd".
Ask string and rotation from the user.
"""


def rotateChar(n: str, p: int):
    result = n[-p:] + n[:-p]
    print(result)


rotateChar("abcdef", 2)
rotateChar("abcdef", 3)
