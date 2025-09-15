"""
Input = "Python is good"
output = "nohtyp si doog"
"""

string = "Python is good"
# Split and unpack in one line
one, two, three = string.split()
# Print reversed words
print(one[::-1], two[::-1], three[::-1])


def reverseChar(string: str) -> str:
    words = string.split()
    return " ".join(i[::-1] for i in words)


# nohtyP si doog

"""
try this methods:
-count
-endswith
-startswith
-index,rindex
-find,rfind
-difference between find and index
-strip and types of strip(lstrip,rstrip)
-replace
"""
