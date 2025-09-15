"""
Q8. Create a Python function to reverse a dictionary (swap keys and values).
Make sure the values are dierent.
Original dictionary: {'a': 1, 'b': 2, 'c': 3}
Reversed dictionary: {1: 'a', 2: 'b', 3: 'c'}
"""

Original_dictionary = {"a": 1, "b": 2, "c": 3}
reverse_dict = {}

for key, value in Original_dictionary.items():
    reverse_dict[value] = key

print(reverse_dict)  # {1: 'a', 2: 'b', 3: 'c'}


def reverseDict(n: dict) -> dict:
    reverse_dictionary = {}
    for key, value in Original_dictionary.items():
        reverse_dictionary[value] = key
    return reverse_dictionary


print(reverseDict({"a": 1, "b": 2, "c": 3}))
