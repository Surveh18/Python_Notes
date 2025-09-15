"""
Q9. Create a function named calSum which takes an 2 integer (nl and n2)
as an argument. Calculate the sum of all the numbers divisible by 5
between nl and n2 and return that sum. (Make sure that nl is less than n2).


# Example 1
ans = catSum(1,10)
print (ans)

# Output
15

# Example 1
ans = catSum(43,68)
print (ans)

# Output
275

"""

n1: int = int(input("Enter n1: "))
n2: int = int(input("Enter n2: "))


def calSum(n1: int, n2: int):
    if n1 > n2:
        print("n1 should be less than n2")
        return None
    total: int = 0
    i: int = n1
    while i <= n2:
        if i % 5 == 0:
            total += i
        i += 1
    return total


x = calSum(n1, n2)
if x is not None:
    print(f"The sum of number from {n1} to {n2} is {x}. ")
