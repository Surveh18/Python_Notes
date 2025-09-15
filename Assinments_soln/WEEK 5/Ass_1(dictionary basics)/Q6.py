"""
Q7. Python program to find the size of a Dictionary.
Basically print how many total key-value pair are there.
"""

my_dict = {
    "phy": 31,
    "chem": 89,
    "math": 56,
    "bio": 78,
}
n = len(my_dict)
print(f"Total key-value pairs are {n}")
# print("Total key-value pairs are", len(list(my_dict.keys())))
# print("Total key-value pairs are", my_dict.__len__())

