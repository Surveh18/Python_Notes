"""
Q7. Create a Python program to find the diffrence between two dictionaries.
First dictionary: {'a': 1, 'b': 2, 'c': 3}
Second dictionary: {'b': 2, 'c': 4, 'd': 5}
Second dictionary: {'b': 2, 'c': 4, 'd': 5}
OUTPUT:
Keys present only in the first dictionary: ['a']
Keys present only in the second dictionary: ['d']
"""

# Dry Run
First_dictionary = {"a": 1, "b": 2, "c": 3}
Second_dictionary = {"b": 2, "c": 4, "d": 5}

a = set(First_dictionary.keys())
b = set(Second_dictionary.keys())

l1 = list(a.difference(b))
l2 = list(b.difference(a))

print(f"Keys present only in the first dictionary: {l1}")
print(f"Keys present only in the second dictionary: {l2}")

# More clear version
first_dict = {"a": 1, "b": 2, "c": 3}
second_dict = {"b": 2, "c": 4, "d": 5}

# convert keys to sets
keys1, keys2 = set(first_dict), set(second_dict)

# difference
only_in_first = keys1 - keys2
only_in_second = keys2 - keys1

print("Keys present only in the first dictionary:", list(only_in_first))
print("Keys present only in the second dictionary:", list(only_in_second))
