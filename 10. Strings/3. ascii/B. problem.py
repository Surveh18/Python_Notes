char = "Hhj438&*&$*#(       AHWUuda121&*(^$#*&))"
"""
Capital letters = 
Small letters = 
Digits = 
Spaces = 
Symbols = 
"""
capital_letters, small_letters, Digits, Spaces, Symbols = 0, 0, 0, 0, 0
for ch in char:
    ascii_code = ord(ch)
    if ascii_code >= 48 and ascii_code <= 57:
        Digits += 1
    elif ascii_code >= 65 and ascii_code <= 90:
        capital_letters += 1
    elif ascii_code >= 97 and ascii_code <= 122:
        small_letters += 1
    elif ascii_code == 32:
        Spaces += 1
    else:
        Symbols += 1
print(f"Capital letters = {capital_letters}")
print(f"Small letters = {small_letters}")
print(f"Digits = {Digits}")
print(f"Spaces = {Spaces}")
print(f"Symbols = {Symbols}")
"""
Capital letters = 5
Small letters = 5
Digits = 6
Spaces = 7
Symbols = 17
"""
