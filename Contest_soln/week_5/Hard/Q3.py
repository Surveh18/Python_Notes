"""
Q3. Given a string S, containing numeric words, the task is to convert the given string to the actual number.
Input: S = “zero four zero one”
Output: 0401
Input: S = “four zero one four”
Output: 4014
"""

s = "four zero one four"
words = s.split()

word_to_num = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

number_str = ""  # Initialize empty string

for word in words:
    word_lower = word.lower()  # Make lowercase to match dictionary keys
    digit = word_to_num[word_lower]  # Get corresponding number
    number_str += str(digit)  # Append to result string

print(number_str)
