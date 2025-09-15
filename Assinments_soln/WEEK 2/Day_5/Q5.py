"""
Q5. Create a function addDigits() that takes an integer as an argument.
Calculate the sum of digits of that number.

#Example - 1
addDigits(123)

6(OUTPUT)

#Example - 1
addDigits(47321)

17(OUTPUT)
"""


def add(num: int) -> int:
    n: int = num
    total = 0
    while n > 0:
        total = total + (n % 10)  # n%10 gives us last digit
        n = n // 10  # Remove the last digit
    return total


print(add(123))
print(add(47321))
"""
For add(123) :
1.Extract: 123 % 10 = 3
  Add: total = O + 3 = 3
  Remove: 123 // 1O = 12

2.Extract: 12 % 10 = 2
  Add: total = 3 + 2 = 5
  Remove: 12 // 10 = 1

3.Extract: 1 % 10 = 1
  Add: total = 5 + 1 = 6
  Remove: 1 // 1O = O

"""
