marks = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    "married": None,
}
# Pop hmare hissab se value to remove kr dega but it can also store
# also we target pop using key but it returns the value
x = marks.pop("hindi")
print(x)  # 89
print(marks)  # {'sci': 78, 'eng': 91, 'math': 55, 'married': None}
