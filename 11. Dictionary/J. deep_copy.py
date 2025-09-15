import copy

my_dict = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "gender": ["Male", "Female"],
}
# axy = copy.copy(my_dict)  # shallow copy
axy = copy.deepcopy(my_dict)  # Deep copy

print(id(my_dict["gender"]))
print(id(axy["gender"]))

print(f"my_dictionary = {my_dict}")
print(f"xyz = {axy}")
print("------------")

axy["gender"][0] = "gg"
print(f"my_dictionary = {my_dict}")
print(f"xyz = {axy}")
"""
# Before
my_dictionary = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['Male', 'Female']}
xyz = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['Male', 'Female']}
------------
# After - As we can say my_dict mai koi changes nhi huve
my_dictionary = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['Male', 'Female']}
xyz = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['gg', 'Female']}
"""
