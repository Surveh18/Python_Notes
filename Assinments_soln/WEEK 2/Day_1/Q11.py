"""
Qll. Write a function named calculate_interest that takes the principal,
rate of interest, and time as parameters and prints the simple interest
calculated.
"""

principal: int = int(input("Enter principal_amount: "))
Rate_of_interest: int = int(input("Enter Rate_of_interest amount: "))
time: int = int(input("Enter time: "))


def calculate_interest(principal, Rate_of_interest, time):
    result = (principal * Rate_of_interest * time) / 100
    print(f"Calculate simple interest is {result}")


calculate_interest(principal, Rate_of_interest, time)
