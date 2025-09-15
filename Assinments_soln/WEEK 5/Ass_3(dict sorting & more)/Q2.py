"""
Q2. Write a Python program to count number of items in a dictionary value that is a list.
Sample Output
Dict = { 'M1' : [67, 79, 90, 73, 36], 'M2' : [89, 67, 84], 'M3' : [82, 57] }
Number of Items in a Dictionary : 10
"""

my_dict = {
    "M1": [67, 79, 90, 73, 36],
    "M2": [89, 67, 84],
    "M3": [82, 57],
}

total = int()
for values in my_dict.values():
    for v in values:
        total += 1
print(f"Number of Items in a Dictionary : {total}")
