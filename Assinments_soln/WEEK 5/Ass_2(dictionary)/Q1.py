"""
Q1. Write a function that takes a dictionary and a key,
and returns True if the key is found in the dictionary, otherwise False.
"""

from typing import Union, Dict

# Without function
my_dict = {
    "phy": 34,
    "chem": 89,
    "math": 56,
    "bio": 78,
}

x = my_dict.get("bio", -1)
print(x)


# With function
def key_exists(my_dict: Dict[str, int], n: Union[int, str]) -> Union[int, str, None]:
    return n in my_dict


my_dict = {
    "phy": 31,
    "chem": 89,
    "math": 56,
    "bio": 78,
}

print(key_exists(my_dict, "chem"))  # True
print(key_exists(my_dict, "eng"))  # False
