"""
Q7.
Implement a Python function that checks if a string contains any special characters (non-alphanumeric) by using ASCII codes.
Input: "password123!"
Output: True

- 48-57           | 0 to 9     | Digits
- 65-90           | A to Z     | Uppercase letters
- 97-122          | a to z     | Lowercase letters

"""


def hasSpecialChar(n: str) -> bool:
    for ch in n:
        ascii_val = ord(ch)
        # Check: digits (48–57), uppercase (65–90), lowercase (97–122)
        if not (
            (48 <= ascii_val <= 57)
            or (65 <= ascii_val <= 90)
            or (97 <= ascii_val <= 122)
        ):
            return True  # found a special character
    return False


# Example usage
print(hasSpecialChar("password123!"))  # True
print(hasSpecialChar("Hello123"))  # False
