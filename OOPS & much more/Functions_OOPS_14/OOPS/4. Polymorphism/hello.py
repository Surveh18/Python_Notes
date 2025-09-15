# Many Forms of method. Example sound


class Animal:
    def sound(self):
        print("Animal Speaking")


class Dog(Animal):
    def sound(self):
        print("Bhaw Bhaw Bhaw")


class Cat(Dog):
    def sound(self):
        print("Meow Meow Meow")


obj = Dog()
obj.sound()
"""
Yaha hmne dog class k sound method ko call kiya hai pr dog n Animal class dono k pass sound method hai 
to konsa call hoga is condition mai dog class ka sound method call hoga isse kehte hai method overriding.

python k andr method overloading nhi hai
"""
