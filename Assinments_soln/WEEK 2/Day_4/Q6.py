"""
Q6.Don't create a function, just print the following pattern
1 11 111 1111 11111.....n times.(Ask n from user).
"""


def Pattern_1(n):
    i = 1
    x = 1
    while i <= n:
        print(x, end=" ")
        x = x * 10 + 1
        i += 1


n = int(input("Enter n: "))
Pattern_1(n)
