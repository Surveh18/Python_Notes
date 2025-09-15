"""
QI. Create a function named divs, which will take two parameters nl and
n2. Return the count of how many numbers from 1 to n1 are divisible by n2.
"""


def divs(n1: int, n2: int):
    i: int = 1
    count: int = 0
    while i <= n1:
        if i % n2 == 0:
            count += 1
        i += 1
    return count


n1: int = 50
n2: int = 9
print(f"The count of numbers divisible by n2 is {divs(n1,n2)}")
