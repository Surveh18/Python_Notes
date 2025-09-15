"""
✅ What are Dunder Methods?
"Dunder" is short for “double underscore”, referring to special methods in Python
that start and end with double underscores, like __init__, __str__, __len__, etc.
this kind of methods are only in python.

These methods are also called:
1. Magic methods
2. Special methods

They're used to override or customize the behavior of Python built-in operations such as:
- Creating objects
- Representing objects
- Adding, comparing, etc.
"""


class Father:
    def __init__(self):
        self.father_name = input("Enter father name: ")
        self.bank_balance = int(input("Enter father bank balance: "))
        self.phone_model = input("Enter phone model: ")

    def __str__(self):
        return f"Father name = {self.father_name}\nBank balance = {self.bank_balance}\nphone model = {self.phone_model}"


obj = Father()
# obj.displayFather()
print(obj)
