"""
3. Multiple Objects
Define a class Car with make, model, and year.
Create three different car objects and display their details.
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def details(self):
        print(f"Make = {self.make}")
        print(f"Model = {self.model}")
        print(f"Year = {self.year}")


c1 = Car("Toyota", "Corolla", 2020)
c2 = Car("Honda", "Civic", 2019)
c3 = Car("Ford", "Mustang", 2023)
print("-------------------------")
c1.details()
print("-------------------------")
c2.details()
print("-------------------------")
c3.details()
