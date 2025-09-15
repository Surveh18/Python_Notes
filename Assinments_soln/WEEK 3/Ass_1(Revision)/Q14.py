"""
Q14. Create a function that takes two parameters and, if both parameters
are strings, add them as if they were integers or if the two parameters are
integers, concatenate them.
• stupid_addition(l, 2) -> "12"
• stupid_addition("l", "2") -> 3
• stupid_addition("l", 2) —> None
If the two parameters are different data types, return None.
All parameters will either be strings or integers.
"""


def stupid_addition(a: int | str, b: int | str) -> int | str | None:
    if type(a) == int and type(b) == int:
        return str(a) + str(b)
    elif type(a) == str and type(b) == str:
        return int(a) + int(b)
    return None


print(stupid_addition(1, 2))
print(stupid_addition("1", "2"))
print(stupid_addition("1", 2))
