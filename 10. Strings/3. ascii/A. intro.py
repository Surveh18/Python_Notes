"""
=> Decimal Range  | Characters | Description
- 32              |            | Space (not visible, but printable)
- 33-47           | ! to /     | Punctuation and special symbols
- 48-57           | 0 to 9     | Digits
- 58-64           | : to @     | More punctuation
- 65-90           | A to Z     | Uppercase letters
- 91-96           | [ to `     | Brackets and grave accent
- 97-122          | a to z     | Lowercase letters
- 123-126         | { to ~     | Final printable symbols
"""

char = "djwkal479832hdkwjaBCNMZ^%*&(^*&1212)"
count = 0
for ch in char:
    ascii_code = ord(ch)
    if ascii_code >= 48 and ascii_code <= 57:
        count += 1
print(count)  # 10

# ord(ch) Returns the ASCII/Unicode code point of that character
# means like A holds value of 65 so ord will convert into it
# ord(A) = 65
