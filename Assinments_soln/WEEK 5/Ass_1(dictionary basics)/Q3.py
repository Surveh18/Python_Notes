"""
Q3. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject
which has marks more than passing marks (above 33).
"""

my_dict = {
    "phy": 31,
    "chem": 89,
    "math": 56,
    "bio": 78,
}


for sub, marks in my_dict.items():
    if marks > 33:
        print(f"{sub} = {marks}")
