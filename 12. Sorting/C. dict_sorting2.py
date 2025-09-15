details = [
    {"Name": "Anirudh", "Age": 67, "Gender": "Male"},  # <--x | x["Age"]
    {"Name": "Sakshi", "Age": 18, "Gender": "Female"},
    {"Name": "Aiyshaa", "Age": 25, "Gender": "Female"},
    {"Name": "Raj", "Age": 22, "Gender": "Male"},
]
print(len(details))  # 4
# If i want to print raj ka gender
print(details[3])
# {'Name': 'Raj', 'Age': 22, 'Gender': 'Male'}
print(details[3]["Gender"])  # Male
print(details[3].get("Gender"))  # Male

print(details[1]["Name"])  # Sakshi

# Sort age wise
new_details = sorted(details, key=lambda x: x["Age"])
print(new_details)
"""
[
    {'Name': 'Sakshi', 'Age': 18, 'Gender': 'Female'},
    {'Name': 'Raj', 'Age': 22, 'Gender': 'Male'},
    {'Name': 'Aiyshaa', 'Age': 25, 'Gender': 'Female'}, 
    {'Name': 'Anirudh', 'Age': 67, 'Gender': 'Male'}
]
"""
# Now if i want to print in structured manner
for index in range(0, len(details)):
    d = details[index]
    print(f"Name = {d["Name"]}, Age = {d["Age"]}, Gender = {d["Gender"]}")
"""
Name = Anirudh, Age = 67, Gender = Male
Name = Sakshi, Age = 18, Gender = Female
Name = Aiyshaa, Age = 25, Gender = Female
Name = Raj, Age = 22, Gender = Male
"""
