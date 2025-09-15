"""
Q6. Write a Python program to generate two strings from a given string.
For the first string, use the characters that occur only once, and for the
second, use the characters that occur multiple times in the said string.

Input: aabbccegh
Output
string1 = egh
string2 = abcf
Input: heello
Output
string1 = ho
string2 = el
"""

s = "aabbccegh"  # Example input

# Step 1: Initialize empty strings
string1 = ""  # Characters that occur only once
string2 = ""  # Characters that occur multiple times

# Step 2: Loop through each character
for ch in s:
    count = s.count(ch)  # Count how many times the character occurs
    if count == 1:
        if ch not in string1:  # Avoid duplicates
            string1 += ch
    else:
        if ch not in string2:  # Avoid duplicates
            string2 += ch

print("string1 =", string1)
print("string2 =", string2)
