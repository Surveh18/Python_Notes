"""
Q3 – Filter dictionary
marks = {"Sam": 56, "Suresh": 89, "Ravi": 45, "Anita": 90}


Task: Find students who scored more than 80.

Tumhe sochna hai: iterate keys/values → compare → store matching keys.
"""

marks = {
    "Sam": 56,
    "Suresh": 89,
    "Ravi": 45,
    "Anita": 90,
}
high_scorers = []

for student, score in marks.items():
    if score > 80:
        high_scorers.append(student)

print("Students scoring more than 80:", high_scorers)
