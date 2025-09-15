"""
Q1. Create a function named oddCharacters which takes a string as a parameter.
Now return a list of characters which appears odd times in that string.

print (oddCharacters ("hello"))
# Output
['h','e','o']

print (oddCharacters ("aeroplane"))
# Output
['r','o','p','l','n']
"""


def oddCharacters(s: str):
    freq = {}  # frequency map
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    return [ch for ch, count in freq.items() if count % 2 != 0]


print(oddCharacters("hello"))
print(oddCharacters("aeroplane"))
