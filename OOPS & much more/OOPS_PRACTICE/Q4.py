"""
4. Internal Calculations
Create a class Rectangle that takes length and width.
Add a method to calculate and return the area when called.
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc(self):
        return self.length * self.width


q1 = Rectangle(10, 20)
area = q1.calc()
print(f"Area of the rectangle is {area}")
