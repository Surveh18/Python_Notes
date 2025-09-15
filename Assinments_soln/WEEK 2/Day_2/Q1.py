"""
QI. Create a function that takes three numbers as parameters and returns
the largest among them. Also if no arguments are passed, make sure the
parameters take default value as None and return answer as -1.
"""


def find_largest(a=None, b=None, c=None):
    if a is None and b is None and c is None:
        return -1
    else:
        largest = a
        if b is not None and b > largest:
            largest = b
        if c is not None and c > largest:
            largest = c
        return largest


print(find_largest(3, 55, 8))
