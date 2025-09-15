"""
Q2 – Nested Dictionary Average
students = {
    "John": {"Math": 85, "Science": 90, "English": 80},
    "Alice": {"Math": 75, "Science": 88, "English": 92},
    "Bob": {"Math": 90, "Science": 85, "English": 78}
}
Task: Calculate average marks for Alice only.
Tumhe sochna hai: outer dict → inner dict → values → sum/len.
"""

students = {
    "John": {"Math": 85, "Science": 90, "English": 80},
    "Alice": {"Math": 75, "Science": 88, "English": 92},
    "Bob": {"Math": 90, "Science": 85, "English": 78},
}
alice_marks = students["Alice"]
v = alice_marks.values()
ans = sum(v) / len(v)
print(ans)
