"""
Q4.Nested dictionary:
students = {
    "John": {"Math": 85, "Science": 90},
    "Alice": {"Math": 75, "Science": 88}
}
👉 Approach likho: kaise sirf John ke Science marks print karoge?
"""

students = {
    "John": {"Math": 85, "Science": 90},
    "Alice": {"Math": 75, "Science": 88},
}
print(students["John"]["Science"])
