"""
Q5. Write a Python program to capitalize the first and last letters of each word in a given string.Input: python is a great languageOutput: PythoN ExerciseS PracticE SolutioN
Input: delhi is best city with 0 AQI
Output: DelhI IS BesT CitY WitH 0 AqI

"""

n = "delhi is best city with 0 AQI"
words = n.split()
result = ""

for word in words:
    if len(word) == 1:
        # If word is single character, just capitalize it
        new_word = word.upper()
    elif word.isdigit():
        # Keep numbers as is
        new_word = word
    else:
        # Capitalize first and last letters, keep middle as is
        new_word = word[0].upper() + word[1:-1] + word[-1].upper()

    result += new_word + " "

# Remove trailing space
result = result.strip()
print(result)
