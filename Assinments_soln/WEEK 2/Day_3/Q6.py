"""
Q6. Create a function named div_by_3_and_5 which takes 2 integers as a
arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
nl and n2.
"""

n1 = int(input("Enter n1 number: "))
n2 = int(input("Enter n2 number: "))


def div_by_3_and_5(n1: int, n2: int):
    while n1 <= n2:
        if n1 % 3 == 0 and n1 % 5 == 0:
            print(n1, end=" ")
        n1 += 1


div_by_3_and_5(n1, n2)
