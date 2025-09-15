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
    sum_evn: int = 0
    sum_odd: int = 0
    n = len(my_list)
    for i in range(0, n):
        if my_list[i] % 2 == 0:
            sum_evn += my_list[i]
        else:
            sum_odd += my_list[i]
    print(f"Even numbers sum = {sum_evn}")
    print(f"Odd numbers sum = {sum_odd}")


my_list = [34, 11, 91, 59, 33, 22]
sumCountOddEven(my_list)
