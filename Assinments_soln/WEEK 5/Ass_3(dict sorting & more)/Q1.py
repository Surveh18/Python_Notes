"""
Q1. Write a Python script to sort (ascending and descending) a dictionary by value.
Sample
Output dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Ascending order = {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
Descending order = {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

"""

my_dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Ascending sort by value
asc_dict = dict(sorted(my_dictionary.items(), key=lambda x: x[1]))

# Descending sort by value
desc_dict = dict(sorted(my_dictionary.items(), key=lambda x: x[1], reverse=True))

print("Original dictionary =", my_dictionary)
print("Ascending order =", asc_dict)
print("Descending order =", desc_dict)
