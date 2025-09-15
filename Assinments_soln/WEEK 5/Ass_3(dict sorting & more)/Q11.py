"""
Q11. Write a Python program to sort a dictionary by the length of its keys.
Original dictionary: {'apple': 2, 'banana': 3, 'pear': 4, 'orange': 5}
Sorted dictionary by key length:
{'pear': 4, 'apple': 2, 'banana': 3, 'orange': 5}
"""

Original_dictionary = {"apple": 2, "banana": 3, "pear": 4, "orange": 5}

new_dict = sorted(Original_dictionary.items(), key=lambda x: len(x[0]))
print(dict(new_dict))
