"""
Q3.Write a function which accepts a String as a parameter
and return the reversed words as a String.

# Example 1
my_string = "python is great"
w = reverseWords (my_string)
print(w)
# Output
great is python
"""


def reverseWords(string: str) -> str:
    words = string.split()
    words = words[::-1]
    return " ".join(words)


print(reverseWords("python is great"))
# great is python
