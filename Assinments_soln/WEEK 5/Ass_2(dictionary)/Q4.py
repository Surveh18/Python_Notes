"""
Q4. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
and the values are squares of the keys.
"""

my_dict = {}

for i in range(1, 16):  # numbers from 1 to 15
    my_dict[i] = i * i  # key = number, value = square

print(my_dict)
"""
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""
