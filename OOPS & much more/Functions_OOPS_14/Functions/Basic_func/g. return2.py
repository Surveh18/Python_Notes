"""
Ask 2 num from user
calculate total of 2 numbers
print if the sum is odd or even

add() check()

"""


def add(n1, n2):
    total = n1 + n2
    return total


def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


x = int(input("Enter num1: "))
y = int(input("Enter num2: "))
s = add(x, y)
print(check(s))
