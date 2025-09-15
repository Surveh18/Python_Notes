"""
Q10. Write a Python program to sort a dictionary by its keys in ascending order.
Original dictionary: {'b': 2, 'a': 1, 'c': 3}
Sorted dictionary by keys: {'a': 1, 'b': 2, 'c': 3}
"""

Original_dictionary = {"b": 2, "a": 1, "c": 3}

new_dict = sorted(Original_dictionary.items(), key=lambda x: x[0])
print(dict(new_dict))

# {'a': 1, 'b': 2, 'c': 3}
