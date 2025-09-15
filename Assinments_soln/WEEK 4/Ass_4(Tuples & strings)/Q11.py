"""
Q11.
Ask a string from user. Print how many spaces are there in that string.

- 32              |            | Space (not visible, but printable)
"""


def spaceCount(n: str) -> int:
    spaces_count = int()
    for ch in n:
        ascii_value = ord(ch)
        if ascii_value == 32:
            spaces_count += 1
    return spaces_count


print(spaceCount("Harshal Surve"))  # 2
print(spaceCount("NoSpacesHere"))  # 0
print(spaceCount("    Leading"))  # 4

"""
optimize
def spaceCount(n: str) -> int:
    return n.count(" ")

def spaceCount(n: str) -> int:
    return sum(1 for ch in n if ch == " ")
"""
