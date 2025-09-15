"""
Q5. Create a Python function to sort a dictionary by its values.
And return that new dictionary.
"""

my_dict = {
    "apple": 45,
    "banana": 10,
    "mango": 25,
    "grapes": 60,
    "orange": 30,
}
new_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(new_dict)
# {'banana': 10, 'mango': 25, 'orange': 30, 'apple': 45, 'grapes': 60}
