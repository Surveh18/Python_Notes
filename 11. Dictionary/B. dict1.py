marks = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "adult": False,
    "Phone_num": [987636738, 983636728],
}
print(marks)
# {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89, 'adult': False, 'Phone_num': [987636738, 983636728]}
print(type(marks))
# <class 'dict'>

# Keys are always immutable
# Keys can be int,str,tuple.
# list is not allowed.
a = {
    1: 2,
    2: False,
    "abc": "Harshal",
    (1, 2, 3): "Surve",
    "abc": "Python",  # this line will overwrite the 20 abc
}
