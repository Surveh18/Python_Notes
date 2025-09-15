"""
Q10. Store name as a Key, and 5 marks in a List as a value in dictionary.
Store details of at least 5 students.
Print the total marks with percentage of each and every student.
"""

students = {
    "Alice": [78, 82, 91, 85, 89],
    "Bob": [65, 70, 72, 68, 74],
    "Charlie": [88, 90, 85, 92, 87],
    "David": [55, 60, 58, 62, 59],
    "Eva": [95, 98, 92, 97, 94],
}
for student, marks in students.items():
    total = 0
    for mark in marks:
        total += mark
    percentage = (total / (len(marks) * 100)) * 100  # percentage
    print(f"{student}: Total = {total}, Percentage = {percentage:.2f}%")
