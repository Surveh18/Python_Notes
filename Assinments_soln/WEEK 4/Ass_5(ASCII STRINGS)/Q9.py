"""
Q9.
Develop a Python program that finds the character with the maximum ASCII value in a given string.
Input: "hello"
Output: 'o' (highest ASCII character in the string)
"""


def maxValue(n: str):
    for ch in n:
        ascii_value = ord(ch)
        maximum = int()
        if ascii_value > maximum:
            maximum = ascii_value
    return chr(maximum)


print(maxValue("hello"))  # o
