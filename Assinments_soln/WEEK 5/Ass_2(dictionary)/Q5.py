"""
Q5. Given a dictionary, write a function that returns a new dictionary containing only the keys that have values of type str.
Input:
{
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "birthday": "May 5",
}

Output:
{
    "name": "Alice",
    "city": "New York",
    "birthday": "May 5",
}
"""

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "birthday": "May 5",
}

filtered_dict = {}
for key, value in my_dict.items():
    if type(value) == str:
        filtered_dict[key] = value
print(filtered_dict)
# {'name': 'Alice', 'city': 'New York', 'birthday': 'May 5'}
