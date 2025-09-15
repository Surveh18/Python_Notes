"""
Q1. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the highest marks scored
"""

my_dict = {
    "phy": 34,
    "chem": 89,
    "math": 56,
    "bio": 78,
}


highest_marks: int = 0

for marks in my_dict.values():
    if marks > highest_marks:
        highest_marks = marks

print(f"Highest marks are {highest_marks}")
