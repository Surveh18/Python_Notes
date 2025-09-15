"""
Check if the num entered by user is divisible by 3 or not.
"""

user_number: int = int(input("Enter a number: "))

# Check if the number is divisible or not.
if user_number % 3 == 0:
    print(f"{user_number} is divisible by 3.")
else:
    print(f"{user_number} is not divisible by 3")

"""
sample input
1.user_number = 30
2.user_number = 5

Output
1. 30 is divisible by 3.
2. 5 is not divisible by 3.
"""
