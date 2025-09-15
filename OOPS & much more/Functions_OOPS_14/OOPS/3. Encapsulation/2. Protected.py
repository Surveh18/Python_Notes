# Protected access modifier


class Father:
    def __init__(self):
        self.father_name = input("Enter father name: ")
        self._bank_balance = int(input("Enter father bank balance: "))
        self.__phone_model = input("Enter phone model: ")
        # phone model is private usko dusri class mai use nhi kiya jaa skta

    def displayFather(self):
        print(f"Father name = {self.father_name}")
        print(f"Bank balance = {self._bank_balance}")
        print(f"phone model = {self.__phone_model}")


class Child(Father):
    def __init__(self):
        super().__init__()
        self.child_name = input("Enter child name: ")

    def displayChildInfo(self):
        print(f"Child name = {self.child_name}")
        print(f"My father has {self._bank_balance} amount.")


child = Child()
child.displayChildInfo()

# This is called Data hiding
