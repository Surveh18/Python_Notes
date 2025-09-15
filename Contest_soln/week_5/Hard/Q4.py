"""
Q4. Convert Snake case to Pascal case.
Input: python_is_great
Output: PythonIsGreat

Input: we_are_learning_python_programming
Output: WeAreLearningPythonProgramming
"""

n = "python_is_great"

# Step 1: split by underscore
words = n.split("_")

# Step 2: capitalize each word and join
pascal_case = ""
for word in words:
    pascal_case += word.capitalize() + " "

print(pascal_case)

# Converts only the first character of the string to uppercase,
# and all other characters to lowercase.
