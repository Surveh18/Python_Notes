"""
Q4. Write a Python program to Convert two lists into a dictionary
Sample Output
keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
"""

keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
my_dict = {}
for i in range(0, len(keys)):
    my_dict[keys[i]] = values[i]
print(my_dict)
# {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
