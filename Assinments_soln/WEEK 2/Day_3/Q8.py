"""
Q8. Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number up to 10
numbers.

# Example 1
multiplication Table (13)

# Output
13 x 1 = 13
13 x 2 = 26
...
13 x 9 = 117
13 x 10 = 130


# Example 2
multiplication Table (231)

# Output
231 x 1 = 231
231 x 2 = 462
...
231 x 9 = 2079
231 x 10 = 2310
"""

num = int(input("Enter the multiplicationTable number: "))
print()  # Adds 1 line of gap.


def multiplicationtable(num):
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}\n")
        i += 1


multiplicationtable(num)
