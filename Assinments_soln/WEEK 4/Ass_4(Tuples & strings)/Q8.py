"""
Q8.
Ask a string from user. Print the string with first 2 letters and last 2 letters.
Example string:
aeroplane
Output:
aene

If length is less than 3, print “INVALID”
"""


def firstAndLastTwoLetters(n: str) -> str:
    if len(n) < 3:
        return f"Invalid"  # Optional: handle very short strings
    return n[:2] + n[-2:]


# Ask user for input
user_input = input("Enter any string: ")
result = firstAndLastTwoLetters(user_input)

print("Output:", result)
