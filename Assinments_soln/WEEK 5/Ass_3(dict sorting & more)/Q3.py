"""
Q3. Write a Python program to print a dictionary line by line.
Sample Output
Dict = {
            "Sam" : {"M1" : 89, "M2" : 56, "M3" : 89},
            "Suresh" : {"M1" : 49, "M2" : 96, "M3" : 89}
        }

Sam
M1 : 89
M2 : 56
M3 : 89

Suresh
M1 : 49
M2 : 96
M3 : 89
"""

my_dict = {
    "Sam": {"M1": 89, "M2": 56, "M3": 89},
    "Suresh": {"M1": 49, "M2": 96, "M3": 89},
}
for name, marks in my_dict.items():
    print(name)
    for subject, score in marks.items():
        print(f"{subject} : {score}")
    print()
"""

Sam
M1 : 89
M2 : 56
M3 : 89

Suresh
M1 : 49
M2 : 96
M3 : 89
"""
