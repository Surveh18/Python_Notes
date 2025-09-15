"""
Q3. Create a function that takes a base number and an exponent number
and returns the calculation.

# Examples:
calc_exponent(5,5) -> 3125
calc_exponent(10,10) -> 10000000000
calc_exponent(3,3) -> 27

-> All test inputs will be positive integers.
-> Don't forget to return the result.
"""


def calc_exponent(base: int, exponent: int) -> int:
    return base**exponent


print(calc_exponent(5, 5))
print(calc_exponent(10, 10))
print(calc_exponent(3, 3))
