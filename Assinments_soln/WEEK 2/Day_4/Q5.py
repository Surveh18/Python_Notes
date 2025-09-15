"""
Q5. Create a function named pattern which takes an integer as an input
and print the following pattern.

# Example 1
pattern (4)

# output
1 2 4 8

# Example 2
pattern(7)

# output
1 2 4 8 16 32 64 #Basically print upto 7 numbers.

"""


def multi_pattern(n):
    i = 1
    x = 1
    while i <= n:
        print(x, end=" ")
        x *= 2
        i += 1


multi_pattern(7)
