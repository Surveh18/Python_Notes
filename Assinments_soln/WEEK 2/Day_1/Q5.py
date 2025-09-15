"""
Q5.Write a function named personal_greet that takes a name as a
parameter and prints a greeting message with that name. For example,
personal_greet("Alice") should print "Hello, Alice!"

"""

name = input("Enter name: ")


def personal_greet(name):
    print(f'"Hello, {name}!"')


personal_greet(name)
