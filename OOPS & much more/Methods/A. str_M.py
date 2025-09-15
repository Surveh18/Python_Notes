# Without __str__
class Person:  # class definition
    def __init__(self, name, age):  # __init__ is constructor method
        self.name = name  # instance attribute
        self.age = age  # instance attribute


p1 = Person("John", 36)  # object instance

print(p1)  # <__main__.Person object at 0x000001B1E7967230>


# With __str__
class person:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

    def __str__(self):
        return f"{self.Name}({self.Age})"


p2 = person("John", 36)

print(p2)  # John(36)
