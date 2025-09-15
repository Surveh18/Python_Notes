"""
Input = "Python is good"
output = "good is python"
"""


def reverseWords(string: str) -> str:
    words = string.split()
    words = words[::-1]
    return " ".join(words)


# return " ".join(i for i in string.split()[::-1])
# alternative instead of those 3 lines.


print(reverseWords("Python is good"))  # good is Python
