"""
Q2. Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks scored.
"""

my_dict = {
    "phy": 34,
    "chem": 89,
    "math": 56,
    "bio": 78,
}


highest_subject = None
highest_marks: int = 0

for subject, marks in my_dict.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_subject = subject

print(f"Highest marks are {highest_marks} in {highest_subject}")
