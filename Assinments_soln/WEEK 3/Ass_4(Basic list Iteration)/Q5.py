"""
Q5. Create a function countOddEven that accepts an List of Integers and
print how many even and odd numbers are there.

my_lst = [34, 11, 91, 59, 33, 22]
countOddEven(my_lst)

# Output
Total even numbers = 2
Total odd numbers = 4
"""


def countOddEven(my_list):
    evn_cnt = 0
    odd_cnt = 0
    n = len(my_list)
    for i in range(0, n):
        if my_list[i] % 2 == 0:
            evn_cnt += 1
        else:
            odd_cnt += 1
    print(f"Total even numbers = {evn_cnt}")
    print(f"Total odd numbers = {odd_cnt}")


my_list = [34, 11, 91, 59, 33, 22]
countOddEven(my_list)
