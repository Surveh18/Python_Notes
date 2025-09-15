"""
Q3. Python Program to remove all duplicates from a given string.
"""


def removeDuplictes(n: str):
    result = []
    for ch in n:
        if ch not in result:
            result.append(ch)
    print(f"Result = {"".join(result)}")


removeDuplictes("Harshal")  # Result = Harshl
removeDuplictes("Level")  # Result = Levl
