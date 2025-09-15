"""
Q2. A student will not be allowed to sit in exam if his/her attendance is less
than 75%-
Take following input from user
• Number of classes held( total_classes)
• Number of classes attended.

1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not.
"""

# Taking input for total classes and classes attended
classes_held: int = int(input("Enter total classes: "))
classes_attended: int = int(input("Enter classes attended: "))

# Validate inputs
if classes_attended > classes_held:
    print("Invalid input: Classes attended cannot be more than total classes held.")
else:
    # Calculate attendance percentage
    attendance_percentage: float = (classes_attended / classes_held) * 100

    # Print the percentage with two decimal places
    print(f"Percentage of class attendance: {attendance_percentage:.2f}%")

    # Determine eligibility
    if attendance_percentage >= 75:
        print("The student is eligible for the exam.")
    else:
        print("The student is not eligible for the exam.")
