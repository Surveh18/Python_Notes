"""
2. Default Values
Create a class Student with name, age, and grade.
Set default values for age and grade so you can create students with just a name too.
"""


class Student:
    def __init__(self, name, grade="Not Assigned", age=24):
        self.name = name
        self.age = age
        self.grade = grade

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


s1 = Student("Harshal", "Btech-CSE-AI")
s2 = Student("Yukta", "Btech-Core", 22)

print("--------------")
s1.show_info()
print("--------------")
s2.show_info()
