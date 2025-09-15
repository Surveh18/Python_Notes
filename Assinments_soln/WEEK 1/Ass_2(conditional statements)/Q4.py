"""
Q4. Write a python program that takes a student's score input and
prints the corresponding grade. Use the following grading scale:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
E: Below 60

"""

# Taking input for the student's score
score: int = int(input("Enter student's score: "))

# Validate the input
if score > 100 or score < 0:  # Added a condition for scores less than 0 as well
    print("Wrong input: Score must be between 0 and 100.")
else:
    # Determine the grade
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "D"
    else:
        grade = "F"

    # Print the result
    print(f"The student score is {score} & has obtained grade {grade}.")
