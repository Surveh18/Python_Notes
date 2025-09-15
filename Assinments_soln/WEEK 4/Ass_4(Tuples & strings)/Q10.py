"""
Q10.
Ask a string from user. Print the count of alphabets (a-z or A-Z) in that string.

"Hello123"
"Python 3.10!"
"12345"

- 97-122          | a to z     | Lowercase letters
- 65-90           | A to Z     | Uppercase letters

"""

# print(ord("A"))  # 65
# print(chr(87))  # w


def countAplhabets(n: str):
    alphabets = 0
    for ch in n:
        ascii_code = ord(ch)
        if (65 <= ascii_code <= 90) or (97 <= ascii_code <= 122):
            alphabets += 1
    return alphabets


# alphabets = sum(1 for ch in n if ch.isalpha())


print(countAplhabets("Hello123"))
print(countAplhabets("Python 3.10!"))
print(countAplhabets("12345"))
