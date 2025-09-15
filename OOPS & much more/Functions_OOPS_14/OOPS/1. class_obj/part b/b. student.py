class Student:
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))

    def display_info(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")

    def change_name(self, new_name: str):
        self.name = new_name


s1 = Student()
print("-----------------")
s1.display_info()
print("-----------------")
s1.change_name("sakshi")
s1.display_info()
