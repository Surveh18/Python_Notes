"""
Q4. Create a function named pattern which takes an integer as an input
and print the following pattern.

# Example 1
pattern(4)

# Output
10 20 30 40


# Example 2
pattern(11)

# Output
10 20 40 50 60 70 80 90 l00 110

"""


def pattern(n):
    i = 1
    num = 10
    while i <= n:
        print(num, end=" ")
        num += 10
        i += 1
    print()


n = int(input("Enter the number: "))
print(pattern(n))
"""
Alternate soln:
def pattern(n):
    i = 1
    while i <= n:
        print(num*10, end=" ")
        i += 1
"""