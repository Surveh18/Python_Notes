# in python every thing is object.
class Student:
    # Following (id,name all are )attributes/class variables.
    id = 0
    name = ""
    gender = "" 
    age = ""

    def __init__(self):
        self.id = int(input(f"Enter id = "))
        self.name = input(f"Enter name = ")
        self.gender = input(f"Enter gender = ")
        self.age = int(input(f"Enter age = "))

    def setdetails(self):
        self.id = int(input(f"Enter id = "))
        self.name = input(f"Enter name = ")
        self.gender = input(f"Enter gender = ")
        self.age = int(input(f"Enter age = "))
    #     phone = int(input("Enter number: "))  # Local variable
    #     # here phone does not require self as like we can create discount like also.

    # Method - when we declare a function inside class it will be method.
    def display(self):
        print(f"Id = {self.id}")
        print(f"name = {self.name}")
        print(f"gender = {self.gender}")
        print(f"age = {self.age}")


# here s1 is object we can create as many as we want like s1,s2,s3 and vice versa.
s1 = Student() #here s1 object is created.
s1.setdetails()  # if we dont call setdetails default attributes will be called.
s1.display()

# INIT method is a constructor which runs itself when and object is created.