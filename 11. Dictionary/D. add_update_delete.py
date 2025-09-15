marks = {
    "sci": 78,
    "eng": 91,
    "math": 55,
    "hindi": 89,
}
print(marks)
# {'sci': 78, 'eng': 91, 'math': 55, 'hindi': 89}

# Update \ Add
# If key exists
marks["eng"] = 78
print(marks)
# {'sci': 78, 'eng': 78, 'math': 55, 'hindi': 89}

# If key NOT exists - new pair will be added
marks["xyz"] = 28
print(marks)
# {'sci': 78, 'eng': 78, 'math': 55, 'hindi': 89, 'xyz': 28}

# Delete
# If key exists
del marks["xyz"]
print(marks)
# {'sci': 78, 'eng': 78, 'math': 55, 'hindi': 89}

# If key NOT exists
del marks["abc"]  # keyerror
print(marks)
