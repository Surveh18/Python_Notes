"""
Q6. Make a password strength function. It will accept a string from user.
Return True if it is a strong password.Strong password has these characteristics.
Minimum 8 character
Minimum 1 uppercase alphabet
Minimum 1 lowercase alphabet
Contains at least 1 special symbol (any symbol)
Minimum 1 digit
"""


def check_password(pwd: str) -> bool:
    # Requirement flags
    has_upper = any(ch.isupper() for ch in pwd)
    has_lower = any(ch.islower() for ch in pwd)
    has_digit = any(ch.isdigit() for ch in pwd)
    has_symbol = any(not ch.isalnum() for ch in pwd)  # symbol => not alphanumeric

    # Warnings
    if len(pwd) < 8:
        print("❌ Minimum 8 characters required")
    if not has_upper:
        print("❌ At least 1 uppercase letter required")
    if not has_lower:
        print("❌ At least 1 lowercase letter required")
    if not has_digit:
        print("❌ At least 1 digit required")
    if not has_symbol:
        print("❌ At least 1 special symbol required")

    # Final check
    is_strong = len(pwd) >= 8 and has_upper and has_lower and has_digit and has_symbol
    if is_strong:
        print("✅ Strong Password")
    else:
        print("⚠️ Weak Password")

    return is_strong


print(check_password("Surveh"))
