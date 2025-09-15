"""
Q7.
Write a python program to ask a string from user. Then count the number of vowels and number of consonants in that string.
(User can type anything including symbols, spaces or anything else)
"""


def countVowelsConsonants(n: str):
    vowels_set = {"a", "e", "i", "o", "u"}
    vowels = 0
    consonants = 0

    for char in n.lower():  # Normalize to lowercase
        if char.isalpha():  # Only consider alphabetic characters
            if char in vowels_set:
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


# Ask user for input
user_input = input("Enter any string (can include symbols, spaces, digits): ")
vowel_count, consonant_count = countVowelsConsonants(user_input)

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
