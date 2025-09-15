# Dictionary is mutable,ordered
marks = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
    1: 5,
}
print(marks["sci"])  # 78
print(marks[1])  # 5
print(marks["science"])  # keyerror
