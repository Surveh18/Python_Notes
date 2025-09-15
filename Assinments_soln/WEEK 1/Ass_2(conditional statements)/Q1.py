"""
Write a program that takes two numbers as input and checks if the first number is divisible by the second.
"""

num_1: int = int(input("Enter number_1: "))
num_2: int = int(input("Enter number_2: "))

# checks if number_1 is divisible by number_2
# in 1st if condition it checks whether the input is zero or not.
if num_1 and num_2 != 0:
    if num_1 % num_2 == 0:
        print(f"{num_1} is divisible by {num_2} ")
    else:
        print(f"{num_1} is not divisible by {num_2}")
else:
    print("Division by zero is not allowed")

"""
Sample input:
1.num_1 = 10  num_2 = 5
2.num_1 = 10   num_2 = 30
3.num_1 = 0   num_2 = 0
4.num_1 = 2   num_2 = 0

Output:
1.10 is divisible by 5 
2.10 is not divisible by 30
3.Division by zero is not allowed
4.Division by zero is not allowed

"""
