"""
Q6.
Write a python program to ask a string from user.
Then count the number of vowels and number of consonants in that string.
(Make sure there are no spaces in string when you enter in terminal
and also do not type any special characters except from alphabets)

- Vowels (5 letters):
A - 65   a - 97
E - 69   e - 101
I - 73   i - 105
O - 79   o - 111
U - 85   u - 117

- Consonants (21 letters):
B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z
"""

# print(ord("A"))  # 65
# print(chr(97))  # a


def countVowelsConsonants(n: str):
    vowels = int()
    consonants = int()
    for v in n:
        if v in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            vowels += 1
        else:
            consonants += 1
    return vowels, consonants


print(countVowelsConsonants("Python"))
print(countVowelsConsonants("Jalebi"))