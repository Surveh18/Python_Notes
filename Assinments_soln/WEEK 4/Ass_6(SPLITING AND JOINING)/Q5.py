"""
Q5.Write a function which accepts a String as a parameter and
return each word being in reverse.

"""


def reverseChar(string: str) -> str:
    words = string.split()
    return " ".join(i[::-1] for i in words)


print(reverseChar("Python is great"))
# nohtyP si taerg
