"""
Ask a num from user. print if the num is odd or even.
"""

# numbers which are divisible by 2 are even numbers
# not divisible by 2 are odd numbers.
user_number: int = int(input("Enter the number: "))

# Calculating if number is EVEN or ODD.
if user_number % 2 == 0:
    print(f"{user_number} is an EVEN number.")
else:
    print(f"{user_number} is an ODD number")

"""
Sample input
1.user_number = 4
2.user_number = 51

Output:
1. 4 is an EVEN number.
2. 51 is an ODD number.

"""
