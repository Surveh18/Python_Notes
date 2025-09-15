"""
Q2. Make a function named checkPalindrome which accepts an integer n
from the user. Return True or False if the number is palindrome or not.
DO NOT USE STRINGS.

#  Examples
checkPalindrome(91 )
checkPa1indrome(1221)
checkPaIindrome(9854)
checkPa1indxome(123454321)

# OUTPUT
FALSE
TRUE
FALSE
TRUE
"""


def reverse(num):
    total = 0
    while num > 0:
        last_digit = num % 10
        total = (total * 10) + last_digit
        num = num // 10
    return total


def checkPalindrome(num):
    reversed_num = reverse(num)
    if reversed_num == num:
        return True
    else:
        return False


print(checkPalindrome(12321))
print(checkPalindrome(121))
print(checkPalindrome(12371))
