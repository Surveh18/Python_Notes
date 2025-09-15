"""
Q7. Create a function named calSum() which takes 2 integers nl and n2 as a
argument. Calculate the sum of all the numbers from nl and n2 and
Also make sure that nl is smaller than n2. If it is not,
RETURN THAT SUM.
then return "nl should be smaller".

# Example 1
x = calsum(l, 10)
print(x)

# Output:
55

# Example 2
x = calsum(7, 3)
print(x)

# Output:
n1 should be smaller.

"""

num1: int = int(input("Enter n1: "))
num2: int = int(input("Enter n2: "))


def cal_sum(num1: int, num2: int):
    if num1 > num2:
        print("n1 should be smaller than n2")
        return None
    total: int = 0
    i: int = num1
    while i <= num2:
        total += i
        i += 1
    return total


x = cal_sum(num1, num2)
if x is not None:
    print(f"The sum of number from {num1} to {num2} is {x}. ")
