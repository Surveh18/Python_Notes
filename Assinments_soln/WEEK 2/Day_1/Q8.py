"""
Q8. Create a function named simple_calculator that takes three
parameters: two numbers and an operation (addition or subtraction
represented by '+' or '-1), and prints the result of the operation.
"""

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
Operation = input("Enter opertion to be performed: ")


def simple_calc(num1, num2, Operation):
    if Operation == "+":
        result = num1 + num2
    elif Operation == "-":
        result = num1 - num2
    elif Operation == "*":
        result = num1 * num2
    elif Operation == "/":
        result = num1 / num2
    else:
        print("Invalid Operation")

    print(f"The result of {num1} {Operation} {num2} is: {result}")


simple_calc(num1, num2, Operation)
