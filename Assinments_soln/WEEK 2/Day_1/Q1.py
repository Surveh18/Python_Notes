"""
QI. Write a Python function to find the Maximum and minimum of three
numbers. use 3 parameters. Make 2 different functions named as maxi and
mini.
"""

a = int(input("Enter num_a: "))
b = int(input("Enter num_b: "))
c = int(input("Enter num_c: "))


def maxi(a, b, c):
    maxi = a
    if b > maxi:
        maxi = b

    if c > maxi:
        maxi = c
    print(f"Maximum number is {maxi}")


def mini(a, b, c):
    mini = a
    if b < mini:
        mini = b

    if c < mini:
        mini = c
    print(f"Minimum number is {mini}")


maxi(a, b, c)
mini(a, b, c)
