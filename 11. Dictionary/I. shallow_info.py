my_dict = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "gender": ["Male", "Female"],
}

xyz = my_dict.copy()
print(id(xyz))  # 1794690442752
print(id(my_dict))  # 1794690064576
# Hmne shallow copy use ki dono k id bhi different hai

print(f"my_dictionary = {my_dict}")
print(f"xyz = {xyz}")
print("------------")

xyz["gender"][0] = "gg"
print(f"my_dictionary = {my_dict}")
print(f"xyz = {xyz}")
"""
# Before
my_dictionary = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['Male', 'Female']}
xyz = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['Male', 'Female']}
------------
# After -As we can se hmne shallow copy fir bhi dono mai chnange huva hai cause list is immutable
and ache se copy nhi huva sirf baahar baahar se copy huva andr se nhi isliye ab karenge deepcopy
my_dictionary = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['gg', 'Female']}
xyz = {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'gender': ['gg', 'Female']}
"""
