# Encapsulation is used for data hiding.
from random import randint


# Access modifier
class Bank:
    def __init__(self):
        self.name = input("Enter name: ")
        self.__account_num = randint(100000, 999999)
        self.__balance = 0

    def display(self):
        print(f"Account number = {self.__account_num}")
        print(f"Name = {self.name}")
        print(f"Balance = {self.__balance}")


# Before applying access modifier to variables.
obj = Bank()
obj.display()
obj.account_num = 223345
obj.display()
"""
Suppose its a real bank ka application but the problem is hum account_num ya balance ko bahar bhi access
kr k unki value change kr paa rhe hai jo ki nhi hona chaiye here comes the access modier in game
account_num, balance jese variable ko hme bahar access nhi dena uska access sirf ussi class k andr rhega

# Types of access modifier:- 
1. Public - which is by default we are using
2. Private - koi bhi varaible ko private bnane k liye uske aage just underscore lagado.
private variable ka access uski class k andr tak hi rehta hai
ex. __balance, __Sum (double-underscore)

3. Protected - Protected variable ka access uski class k andr to rehta hi hai but jo usko inherit karega 
usko pass bhi rehta hai 
ex. _balance, _Sum (single-underscore)
example in another file



"""
