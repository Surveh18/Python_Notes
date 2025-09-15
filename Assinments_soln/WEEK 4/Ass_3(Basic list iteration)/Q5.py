"""
Q5. Create a function countOddEven that accepts an List of Integers and
print how many even and odd numbers are there.

my_list = [34,11,91,59,33,22]
countOddEven(my_list)

# Output
Total Even num = 2
Total Odd num = 4
"""


def countOddEven(my_list):
    even = 0
    odd = 0
    for i in my_list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f"Total even numbers = {even}")
    print(f"Total odd numbers = {odd}")


my_list = [34, 11, 91, 59, 33, 22]
(countOddEven(my_list))
