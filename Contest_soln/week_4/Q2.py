"""
Q2. Keep asking characters from user until he presses q on the keyboard.
Change all the capital letters to small, and all the small letters to capital.
(Don’t use swapcase().
- 97-122          | a to z     | Lowercase letters
- 65-90           | A to Z     | Uppercase letters

"""

result = []  # empty list to store characters

while True:
    n = input("Enter character: ")
    if n == "q" or n == "Q":
        break
    # convert character
    ascii_val = ord(n)
    if 97 <= ascii_val <= 122:  # lowercase (a-z)
        result += chr(ascii_val - 32)  # convert to uppercase
    elif 65 <= ascii_val <= 90:  # uppercase (A-Z)
        result += chr(ascii_val + 32)  # convert to lowercase
    else:
        result += n  # keep as it is if not alphabet

print("Result =", "".join(result))
