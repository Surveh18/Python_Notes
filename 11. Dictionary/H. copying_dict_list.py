my_dict = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "married": None,
}

xyz = my_dict
print(id(my_dict))  # 2552286290112 same id dono ki
print(id(xyz))  # 2552286290112
print(f"my_dictionary = {my_dict}")
print(f"xyz = {xyz}")
print("------------")

xyz["hindi"] = 100
print(f"my_dictionary = {my_dict}")
print(f"xyz = {xyz}")

"""
# Before
my_dictionary = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'married': None}
xyz = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'married': None}
------------
# After - As we can say dono mai hindi update huva hai means ye same reference pass kr rhe hai copy nhi huvaa
my_dictionary = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 100, 'married': None}
xyz = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 100, 'married': None}
"""
# Using .copy() \ shallow copy
my_dict1 = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "married": None,
}

abc = my_dict1.copy()
print(id(abc))  # 1166878047552
print(id(my_dict1))  # 1166878044288
# Dono ki id same nhi hai dono alag ho chuke hai abhi
# Agr abc mai change karu to my_dict1 mai vo changes reflect nhi honge
