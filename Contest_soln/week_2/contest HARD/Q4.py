"""
Q4. Make a function named checkArmstrong which accepts an integer n
from the user. Return True or False if that number is an armstrong number.

# Example 1
checkArmstrong (153)

# Output
True

# Reason
1^3 + 5^3 + 3^3 = 153

# Example 2
checkArmstrong (407)

# Output
True

# Reason
4^3 + 0^3 + 7^3 = 407
"""


def checkArmstrong(num):
    original_Num = num
    order = len(str(num))
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit**order
        num //= 10
    if sum == original_Num:
        return True
    else:
        return False


print(checkArmstrong(153))
print(checkArmstrong(407))
