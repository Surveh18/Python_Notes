"""
Q7.Write a function which accepts a String and another string
(which will be a single character) as a parameter.
Join that string along with that character but in reverse.
"""


def reverseWords(string: str, str2: str) -> str:
    words = string.split()
    words = words[::-1]
    return str2.join(words)


print(reverseWords("python is great", " & "))  # great & is & python
