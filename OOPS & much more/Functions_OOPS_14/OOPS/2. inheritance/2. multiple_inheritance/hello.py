class Father:
    def __init__(self):
        print("father init")

    father_name = ""

    def displayFatherName(self):
        print(self.father_name)


class Mother:
    def __init__(self):
        print("mother init")

    mother_name = ""

    def displayMotherName(self):
        print(self.mother_name)


class Child(Mother, Father):
    def __init__(self):
        super().__init__()
        print("child init")

    child_name = ""

    def displayChildName(self):
        print(self.child_name)


s1 = Child()
s1.father_name = "Nareshbhai"
s1.mother_name = "Pramilaben"
s1.child_name = "Krupal"
s1.displayFatherName()
s1.displayMotherName()
s1.displayChildName()
