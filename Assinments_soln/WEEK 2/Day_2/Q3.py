"""
Q3. Ask 3 numbers from user. Make a function which returns the middle of
those 3 numbers. Then make a function to check if that middle number is
divisible by both 3 and 4. Make 2 functions for reusability.
"""

""" Logic for middle number is that middle will be greater than or equal to 
the smallest number & less than or equal to the largest number. 

Example: a-4, b-8, c-2.
we know that middle number is 4.

Applying logic conditions.
1.(4>=2) Firstly 4 is greater than or equal to 2.
2.(4<=8) 4 is less than or equal to 8.
"""


# Function to find the middle number of 3.
def find_middle(num1: int, num2: int, num3: int) -> int:
    if (num1 <= num2 and num1 >= num3) or (num1 >= num2 and num1 <= num3):
        return num1
    elif (num2 <= num1 and num2 >= num3) or (num2 >= num1 and num2 <= num3):
        return num2
    else:
        return num3


# Function for checking if middle_num is divisible by 3 and 4.
def isDivisible(number: int) -> int:
    if number % 3 == 0 and number % 4 == 0:
        return True
    return False


# Taking user_input.
num1: int = int(input("Enter num1: "))
num2: int = int(input("Enter num2: "))
num3: int = int(input("Enter num3: "))

# finding the middle number.
middle_num = find_middle(num1, num2, num3)
print(f"The middle number of {num1}, {num2}, & {num3} is {middle_num}.")

# Checking Divisibility with 3 & 4.
if isDivisible(middle_num):
    print(f"The middle number {middle_num} is divisible by 3 & 4.")
else:
    print(f"The middle number {middle_num} is Not divisible by 3 & 4.")
