"""
Q6. Write a Python program to find the maximum and minimum value in a dictionary.
"""

my_dict = {
    "banana": 10,
    "mango": 25,
    "orange": 30,
    "apple": 45,
    "grapes": 60,
}

max_key = max(my_dict.items(), key=lambda x: x[1])
min_key = min(my_dict.items(), key=lambda x: x[1])

print("Maximum pair:", max_key)
print("Minimum pair:", min_key)
