"""
Q6.Write a function which accepts a String and another string
(which will be a single character) as a parameter. Join that string along with that character.
"""


def reverseChar(string: str, str2: str) -> str:
    words = string.split()
    return str2.join(i for i in words)


print(reverseChar("python is great", "#"))  # python#is#great
print(
    reverseChar("hmse interview crack hojaayega", "*")
)  # hmse*interview*crack*hojaayega
