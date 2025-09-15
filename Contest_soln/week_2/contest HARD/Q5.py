"""
Q5. Make a function named sumOfFirstAndLastDigit which accepts an
integer n from the user. Calculate the sum of first and last digit of a
number and return it.

# Examples
sumOfFirsttAndLastDigit(1234)
sumOfFirstAndLastDigit(8471)
sumOfFirstAndLastDigit(5)
sumOfFirstAndLastDigit(99)
"""


def sumOfFirstAndLastDigit(n: int) -> int:
    total_digit: int = len(str(n))

    # Extract the last digit.
    last_digit: int = n % 10

    # Extract the first digit
    first_digit: int = n // 10 ** (total_digit - 1)

    # Sum of first & last digit
    sum: int = first_digit + last_digit
    return sum


print(sumOfFirstAndLastDigit(1234))
print(sumOfFirstAndLastDigit(8471))
print(sumOfFirstAndLastDigit(5))
print(sumOfFirstAndLastDigit(99))
