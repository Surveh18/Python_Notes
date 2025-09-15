marks = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "married": None,
}
# To print keys - isse kuch kr nhi skte bs keys dekhne k liye
print(marks.keys())
# dict_keys(['sci', 'eng', 'math', 'hindi', 'married'])

print(type(marks.keys()))
# <class 'dict_keys'>

all_keys = marks.keys()
# print(all_keys[0])
# TypeError: 'dict_keys' object is not subscriptable

for k in all_keys:
    print(k, marks[k], end=" ")
"""
sci 78 eng 91 math 55 hindi 89 married None
"""
# print(f"Key = {k}, Value = {marks[k]}")
"""
Step by step:

k = "sci" → marks["sci"] = 78
→ prints sci 78

k = "eng" → marks["eng"] = 91
→ prints eng 91

k = "math" → marks["math"] = 55
→ prints math 55

k = "hindi" → marks["hindi"] = 89
→ prints hindi 89

k = "married" → marks["married"] = None
→ prints married None
"""

for v in marks.values():
    print(f"Values = {v}")

print(marks.items())
# dict_items([('sci', 78), ('eng', 91), ('math', 55), ('hindi', 89), ('married', None)])

for k, v in marks.items():
    print(k, v)
"""
sci 78
eng 91
math 55
hindi 89
married None
"""
