"""
Q8.Write a function pattern which accepts an integer n as a n argument.
Then print the following pattern.

#Example: 1
pattern(4)

# Output
1 4 9 16

#Example: 2
pattern(10)

# Output
1 4 9 16 25 36 49 64 81 100

"""


def pattern_n(n):
    i = 1
    x = 1
    while i <= n:
        print(x**2, end=" ")
        x += 1
        i += 1


n = int(input("Enter the number: "))
pattern_n(n)
