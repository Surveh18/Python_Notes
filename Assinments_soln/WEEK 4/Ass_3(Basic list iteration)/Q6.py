"""
Q6. Create a function sumCountOddEven that accepts an List of Integers
and calculate sum of even and odd numbers.

my_list = [34,11,91,59,33,22]
sumCountOddEven(my_list)

# Output 
Even numbers sum = 56
Odd numbers sum = 194
"""


def sumCountOddEven(my_list):
    even = 0
    odd = 0
    for i in my_list:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    print(f"even num sum  = {even}")
    print(f"odd num sum = {odd}")


my_list = [34, 11, 91, 59, 33, 22]
(sumCountOddEven(my_list))
