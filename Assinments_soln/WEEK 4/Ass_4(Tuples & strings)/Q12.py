"""
Q12.
Ask a string from user. Print how many characters are there which are not alphabets.
Example 1: abc%$#gyhy
Output: 3
Example 2: AB788&*(^%&*%^&aaaa
Output: 13
Example 3: 1233^&*(* 0000011
Output: 17
Example 4: abcdABCD
Output: 0
Q13.
"""


def nonAlphabetCount(n: str) -> int:
    count = int()
    for ch in n:
        ascii_val = ord(ch)
        if (ascii_val >= 97 and ascii_val <= 122) or (
            ascii_val >= 65 and ascii_val <= 90
        ):
            count += 1
    return len(n) - count


print(nonAlphabetCount("abc%$#gyhy"))
print(nonAlphabetCount("AB788&*(^%&*%^&aaaa"))
print(nonAlphabetCount("1233^&*(* 0000011"))
print(nonAlphabetCount("abcdABCD"))

"""
def nonAlphabetCount(n: str) -> int:
    count = 0
    for ch in n:
        if not ch.isalpha():   # anything that's NOT a-z or A-Z
            count += 1
    return count
"""
