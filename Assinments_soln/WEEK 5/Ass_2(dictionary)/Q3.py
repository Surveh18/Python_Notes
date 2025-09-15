"""
Q3. Write a function that updates the values of a dictionary by multiplying
them by a given factor only if the value is an integer

Initial Dictionary:
{
    "A":3,"B":"hello","C":7.5,"D":10,
}

Factor: 2 (Ask input from user)
Output Dictionary:
{'A': 6, 'B': 'Hello', 'C': 7.5, 'D': 20}

"""


def Factor(dict1: dict):
    f = int(input("Enter Factor: "))
    for letter in my_dict:
        if isinstance(my_dict[letter], int):
            my_dict[letter] *= f
    return my_dict


my_dict = {
    "A": 3,
    "B": "Hello",
    "C": 7.5,
    "D": 10,
}
print(Factor(my_dict))
