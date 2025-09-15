a = "AHKJyfkhKHDWAKJ43298789$&#(*$&dwada  DaD)"
result = str()
# - 97-122          | a to z     | Lowercase letters
# - 65-90           | A to Z     | Uppercase letters
# 65 + 32 = 97(a), 97-32 = 65(A)
# print(chr(97))  # a
# print(ord("A"))  # 65

for ch in a:
    ascii_val = ord(ch)
    if 97 <= ascii_val <= 122:  # lowercase
        result += chr(ascii_val - 32)  # make uppercase
    elif 65 <= ascii_val <= 90:  # uppercase
        result += chr(ascii_val + 32)  # make lowercase
    else:
        result += ch  # keep numbers/symbols as is

print(result)
