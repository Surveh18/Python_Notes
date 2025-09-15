"""
Q3. Ask x and n from user and then calculate the following answer.
# Example 1
pattern (x=6, n=4)

# Output
6/1 + 6/3 + 6/5 + 6/7
10.057142857142857 (OUTPUT)


# Example 2
pattern (x=9, n=11)

# Output
9/1 + 9/3 + 9/5 + 9/7 + 9/9 .... upto n times
19.627871200007426 (OUTPUT)
"""


def x_n(x, n):
    total = 0
    for i in range(n):
        total = total + (x / (2 * i + 1))
    print(total)


x_n(6, 4)
x_n(9, 11)
