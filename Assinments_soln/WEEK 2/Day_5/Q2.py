"""
Q2. Write a program to display the n terms of a harmonic series and their
sum.
1 + 1/2 + 1/3 + 1/4 + 1/5...1/n terms
Lets suppose n = 5
1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334
"""


def harmonic(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (1 / i)
    print(f"{total:.6f}")


harmonic(5)
