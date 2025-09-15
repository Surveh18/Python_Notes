"""
Q1.
Ask a string from user. If the length of string is
odd, then change all the capital letters to small and vice versa, but if the length of string is
even, reverse the string. Do this using a function and return the output.

Example 1
a = AEroPLane
r = changeString(a)
print (1)
# Output
aeROplANE

# Example 2
a = AEroPLanes
r = changeString(a)
print(r)
# Output
senaLPorEA

- 65-90           | A to Z     | Uppercase letters
- 97-122          | a to z     | Lowercase letters
"""


def changeString(a: str) -> str:
    result = str()
    if len(a) % 2 == 1:  # odd length
        for ch in a:
            ascii_val = ord(ch)
            if 65 <= ascii_val <= 90:  # uppercase → lowercase
                result += chr(ascii_val + 32)
            elif 97 <= ascii_val <= 122:  # lowercase → uppercase
                result += chr(ascii_val - 32)
            else:
                result += ch
    else:
        result = a[::-1]
    return result


print(changeString("AEroPLane"))  # aeROplANE
print(changeString("AEroPLanes"))  # senaLPorEA
